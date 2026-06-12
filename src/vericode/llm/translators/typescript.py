from __future__ import annotations

import re

from vericode.llm.translators.base import Translator


class TypeScriptTranslator(Translator):
    language = "typescript"

    def unverifiable_patterns(self) -> list[str]:
        return [
            r"\basync\b",
            r"\bawait\b",
            r"\bimport\s+",
            r"\brequire\s*\(",
            r"\bdynamic\s+import\b",
            r"\beval\s*\(",
            r"\bfetch\s*\(",
            r"\bPromise\b",
        ]

    def system_prompt_name(self) -> str:
        return "translate_system_typescript.txt"

    def can_translate(self, symbol: str, source: str) -> tuple[bool, str]:
        if not source.strip():
            return False, f"Empty source for symbol {symbol}"
        for pattern in self.unverifiable_patterns():
            if re.search(pattern, source):
                return False, f"TypeScript pattern not supported in v1: {pattern}"
        name_pat = re.escape(symbol)
        if not re.search(
            rf"(?:function\s+{name_pat}\s*\(|const\s+{name_pat}\s*=)",
            source,
        ):
            return False, f"Symbol {symbol} is not a function/const in scoped source"
        return True, ""
