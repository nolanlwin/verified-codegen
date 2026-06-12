from __future__ import annotations

import re

from vericode.llm.translators.base import Translator


class PythonTranslator(Translator):
    language = "python"

    def unverifiable_patterns(self) -> list[str]:
        return [
            r"\basync\s+def\b",
            r"\bawait\b",
            r"\bimport\s+\w+",
            r"\bfrom\s+\w+\s+import\b",
            r"\beval\s*\(",
            r"\bexec\s*\(",
            r"\bgetattr\s*\(",
            r"\bopen\s*\(",
            r"\brequests\.",
            r"\burllib\.",
        ]

    def system_prompt_name(self) -> str:
        return "translate_system_python.txt"

    def can_translate(self, symbol: str, source: str) -> tuple[bool, str]:
        if not source.strip():
            return False, f"Empty source for symbol {symbol}"
        for pattern in self.unverifiable_patterns():
            if re.search(pattern, source):
                return False, f"Python pattern not supported in v1: {pattern}"
        if not re.search(rf"\bdef\s+{re.escape(symbol)}\s*\(", source):
            return False, f"Symbol {symbol} is not a top-level def in scoped source"
        return True, ""
