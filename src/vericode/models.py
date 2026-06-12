from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, Field


class SessionStatus(str, Enum):
    DRAFT_SPEC = "draft_spec"
    AWAITING_REVIEW = "awaiting_review"
    VERIFIED_SPEC = "verified_spec"
    GENERATING_DAFNY = "generating_dafny"
    VERIFYING = "verifying"
    COMPILING = "compiling"
    DONE = "done"
    DONE_WITH_FINDINGS = "done_with_findings"
    FAILED = "failed"


SourceType = Literal["nl", "github_pr"]
VerificationMode = Literal["greenfield", "verify_pr"]
SourceLanguage = Literal["python", "typescript", "javascript", "unknown"]


class SessionMeta(BaseModel):
    session_id: str
    status: SessionStatus = SessionStatus.DRAFT_SPEC
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    spec_model: str = "gpt-4o-mini"
    codegen_model: str = "gpt-4o"
    verified: bool = False
    verify_attempts: int = 0
    max_verify_retries: int = 5
    error_message: Optional[str] = None
    revision_feedback: list[str] = Field(default_factory=list)
    source_type: SourceType = "nl"
    source_ref: Optional[str] = None
    verification_mode: VerificationMode = "greenfield"
    focus_symbol: Optional[str] = None
    focus_language: Optional[SourceLanguage] = None


class ReviewComment(BaseModel):
    author: str = ""
    body: str
    path: Optional[str] = None
    line: Optional[int] = None


class FileChange(BaseModel):
    path: str
    language: SourceLanguage = "unknown"
    patch: str = ""
    before: str = ""
    after: str = ""
    status: str = "modified"


class ScopedSymbol(BaseModel):
    path: str
    name: str
    language: SourceLanguage
    kind: str = "function"
    source: str = ""
    start_line: int = 1


class TaskContext(BaseModel):
    repo: str = ""
    pr_number: int = 0
    title: str = ""
    body: str = ""
    author: str = ""
    url: str = ""
    base_sha: str = ""
    head_sha: str = ""
    files: list[FileChange] = Field(default_factory=list)
    comments: list[ReviewComment] = Field(default_factory=list)
    review_comments: list[ReviewComment] = Field(default_factory=list)
    focus: Optional[ScopedSymbol] = None
    verification_scope: str = ""
    intent_summary: str = ""
    scope_notes: list[str] = Field(default_factory=list)
    pr_shape: str = "unknown"


class AbstractParameter(BaseModel):
    dafny_name: str
    dafny_type: str
    replaces_python_param: Optional[str] = None
    reason: str = ""


class ExternalConstant(BaseModel):
    name: str
    defining_path: str
    marker: str
    value_preview: str = ""


class TestOracle(BaseModel):
    condition: str
    expectation: str
    source_path: str = ""


class SymbolContext(BaseModel):
    """Evidence-derived interface for spec formalization and faithful translation."""
    abstract_parameters: list[AbstractParameter] = Field(default_factory=list)
    external_constants: list[ExternalConstant] = Field(default_factory=list)
    test_oracles: list[TestOracle] = Field(default_factory=list)
    unresolved_names: list[str] = Field(default_factory=list)


class CritiqueOutcome(str, Enum):
    PROVED = "PROVED"
    SPEC_REJECTED = "SPEC_REJECTED"
    SPEC_UNFORMALIZABLE = "SPEC_UNFORMALIZABLE"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    TRANSLATION_GAP = "TRANSLATION_GAP"
    PROOF_FAILED = "PROOF_FAILED"
    SPEC_CODE_MISMATCH = "SPEC_CODE_MISMATCH"
    RESOURCE_LIMIT = "RESOURCE_LIMIT"
    INHERENTLY_UNVERIFIABLE = "INHERENTLY_UNVERIFIABLE"


class CritiqueFinding(BaseModel):
    category: str = ""
    message: str
    spec_clause: Optional[str] = None
    pr_location: Optional[str] = None


class CritiqueReport(BaseModel):
    outcome: CritiqueOutcome
    summary: str
    findings: list[CritiqueFinding] = Field(default_factory=list)
    focus_symbol: Optional[str] = None
    verified: bool = False


class SpecAgentResponse(BaseModel):
    internal_dafny: str
    nl_summary: str
    notes: list[str] = Field(default_factory=list)


class CodegenAgentResponse(BaseModel):
    dafny_source: str


class DafnyError(BaseModel):
    line: Optional[int] = None
    column: Optional[int] = None
    message: str
    error_type: Optional[str] = None


class VerificationResult(BaseModel):
    ok: bool
    stdout: str = ""
    stderr: str = ""
    errors: list[DafnyError] = Field(default_factory=list)
    returncode: int = 0


class BuildResult(BaseModel):
    ok: bool
    stdout: str = ""
    stderr: str = ""
    output_dir: Optional[str] = None
    main_py: Optional[str] = None
    returncode: int = 0
