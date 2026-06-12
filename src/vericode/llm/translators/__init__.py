from __future__ import annotations

from vericode.llm.translators.base import Translator, TranslationResult
from vericode.llm.translators.python import PythonTranslator
from vericode.llm.translators.typescript import TypeScriptTranslator
from vericode.models import SourceLanguage

_TRANSLATORS: dict[SourceLanguage, Translator] = {
    "python": PythonTranslator(),
    "typescript": TypeScriptTranslator(),
    "javascript": TypeScriptTranslator(),
}


def get_translator(language: SourceLanguage) -> Translator:
    if language not in _TRANSLATORS:
        raise ValueError(f"No translator for language: {language}")
    return _TRANSLATORS[language]


__all__ = [
    "PythonTranslator",
    "TranslationResult",
    "Translator",
    "TypeScriptTranslator",
    "get_translator",
]
