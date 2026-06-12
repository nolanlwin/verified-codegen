from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from vericode.models import SourceLanguage


@dataclass
class TranslationResult:
    dafny_source: str
    gaps: list[str]


class Translator(ABC):
    language: SourceLanguage

    @abstractmethod
    def can_translate(self, symbol: str, source: str) -> tuple[bool, str]:
        """Return (ok, reason) for feasibility pre-check."""

    @abstractmethod
    def unverifiable_patterns(self) -> list[str]:
        ...

    @abstractmethod
    def system_prompt_name(self) -> str:
        ...
