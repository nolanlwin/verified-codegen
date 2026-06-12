from __future__ import annotations

import json
import os
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from vericode.models import SessionMeta, SessionStatus, SymbolContext, TaskContext


class SessionStore:
    def __init__(self, root: Optional[Path] = None) -> None:
        self.root = root or Path.cwd() / ".vericode" / "sessions"
        self.root.mkdir(parents=True, exist_ok=True)

    def create_session(
        self,
        prompt: str,
        *,
        spec_model: str = "gpt-4o-mini",
        codegen_model: str = "gpt-4o",
        max_verify_retries: int = 5,
        source_type: str = "nl",
        source_ref: str | None = None,
        verification_mode: str = "greenfield",
        focus_symbol: str | None = None,
        focus_language: str | None = None,
    ) -> SessionMeta:
        session_id = uuid.uuid4().hex[:12]
        session_dir = self.session_dir(session_id)
        session_dir.mkdir(parents=True, exist_ok=True)
        meta = SessionMeta(
            session_id=session_id,
            spec_model=spec_model,
            codegen_model=codegen_model,
            max_verify_retries=max_verify_retries,
            source_type=source_type,  # type: ignore[arg-type]
            source_ref=source_ref,
            verification_mode=verification_mode,  # type: ignore[arg-type]
            focus_symbol=focus_symbol,
            focus_language=focus_language,  # type: ignore[arg-type]
        )
        self.write_meta(meta)
        self.write_text(session_id, "prompt.txt", prompt)
        return meta

    def create_pr_session(
        self,
        context: TaskContext,
        prompt: str,
        *,
        spec_model: str = "gpt-4o-mini",
        codegen_model: str = "gpt-4o",
        max_verify_retries: int = 5,
    ) -> SessionMeta:
        focus_language = context.focus.language if context.focus else None
        meta = self.create_session(
            prompt,
            spec_model=spec_model,
            codegen_model=codegen_model,
            max_verify_retries=max_verify_retries,
            source_type="github_pr",
            source_ref=context.url or None,
            verification_mode="verify_pr",
            focus_symbol=context.verification_scope or None,
            focus_language=focus_language,
        )
        self.write_context(meta.session_id, context)
        self._write_source_snapshots(meta.session_id, context)
        from vericode.sources.symbol_context import analyze_symbol_context

        self.write_symbol_context(meta.session_id, analyze_symbol_context(context))
        return meta

    def write_context(self, session_id: str, context: TaskContext) -> Path:
        path = self.session_dir(session_id) / "context.json"
        path.write_text(context.model_dump_json(indent=2), encoding="utf-8")
        return path

    def read_context(self, session_id: str) -> TaskContext:
        return TaskContext.model_validate_json(
            (self.session_dir(session_id) / "context.json").read_text(encoding="utf-8")
        )

    def read_context_optional(self, session_id: str) -> TaskContext | None:
        path = self.session_dir(session_id) / "context.json"
        if not path.is_file():
            return None
        return self.read_context(session_id)

    def write_symbol_context(self, session_id: str, symbol_context: SymbolContext) -> Path:
        path = self.session_dir(session_id) / "symbol_context.json"
        path.write_text(symbol_context.model_dump_json(indent=2), encoding="utf-8")
        return path

    def read_symbol_context(self, session_id: str) -> SymbolContext:
        return SymbolContext.model_validate_json(
            (self.session_dir(session_id) / "symbol_context.json").read_text(encoding="utf-8")
        )

    def read_symbol_context_optional(self, session_id: str) -> SymbolContext | None:
        path = self.session_dir(session_id) / "symbol_context.json"
        if not path.is_file():
            return None
        return self.read_symbol_context(session_id)

    def _write_source_snapshots(self, session_id: str, context: TaskContext) -> None:
        source_dir = self.session_dir(session_id) / "source"
        source_dir.mkdir(parents=True, exist_ok=True)
        for fc in context.files:
            if fc.after:
                (source_dir / Path(fc.path).name).write_text(fc.after, encoding="utf-8")
            if fc.before:
                (source_dir / f"{Path(fc.path).name}.before").write_text(fc.before, encoding="utf-8")

    def write_critique(self, session_id: str, critique_md: str, critique_json: str) -> None:
        self.write_text(session_id, "critique.md", critique_md)
        self.write_text(session_id, "critique.json", critique_json)

    def session_dir(self, session_id: str) -> Path:
        return self.root / session_id

    def meta_path(self, session_id: str) -> Path:
        return self.session_dir(session_id) / "meta.json"

    def write_meta(self, meta: SessionMeta) -> None:
        meta.updated_at = datetime.now(timezone.utc)
        self.meta_path(meta.session_id).write_text(
            meta.model_dump_json(indent=2), encoding="utf-8"
        )

    def read_meta(self, session_id: str) -> SessionMeta:
        return SessionMeta.model_validate_json(
            self.meta_path(session_id).read_text(encoding="utf-8")
        )

    def write_text(self, session_id: str, name: str, content: str) -> Path:
        path = self.session_dir(session_id) / name
        path.write_text(content, encoding="utf-8")
        return path

    def read_text(self, session_id: str, name: str) -> str:
        return (self.session_dir(session_id) / name).read_text(encoding="utf-8")

    def read_text_optional(self, session_id: str, name: str) -> Optional[str]:
        path = self.session_dir(session_id) / name
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def exists(self, session_id: str) -> bool:
        return self.meta_path(session_id).exists()

    def list_sessions(self) -> list[SessionMeta]:
        sessions: list[SessionMeta] = []
        if not self.root.exists():
            return sessions
        for path in sorted(self.root.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True):
            meta_file = path / "meta.json"
            if meta_file.is_file():
                sessions.append(SessionMeta.model_validate_json(meta_file.read_text(encoding="utf-8")))
        return sessions

    def output_dir(self, session_id: str) -> Path:
        path = self.session_dir(session_id) / "output"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def copy_verified_spec(self, session_id: str) -> None:
        src = self.session_dir(session_id) / "draft_spec.md"
        dst = self.session_dir(session_id) / "verified_spec.md"
        shutil.copy2(src, dst)

    def update_status(self, session_id: str, status: SessionStatus, **kwargs: object) -> SessionMeta:
        meta = self.read_meta(session_id)
        meta.status = status
        for key, value in kwargs.items():
            setattr(meta, key, value)
        self.write_meta(meta)
        return meta

    def fail_session(self, session_id: str, message: str) -> SessionMeta:
        return self.update_status(
            session_id,
            SessionStatus.FAILED,
            error_message=message,
        )
