from __future__ import annotations

import re


def to_vericode_prompt(problem: dict) -> str:
    entry = problem["entry_point"]
    return (
        "Implement the following Python function with verified Dafny code.\n\n"
        f"{problem['prompt'].rstrip()}\n\n"
        f"Requirements:\n"
        f"- The main Dafny method must be named `{entry}` (PascalCase `{to_pascal_case(entry)}` is OK).\n"
        f"- Define a pure recursive `function {to_pascal_case(entry)}Spec(...)` for semantics.\n"
        f"- Put postconditions on the method only: `ensures result == {to_pascal_case(entry)}Spec(...)`.\n"
        f"- No while loops inside functions; no ensures on functions.\n"
        f"- Method body must be `{{ assume false; }}` only.\n"
        f"- Compiled Python will be tested as `{entry}`."
    )


def to_pascal_case(snake: str) -> str:
    return "".join(part.capitalize() for part in snake.split("_"))


def list_static_methods(python_source: str) -> list[str]:
    return re.findall(r"@staticmethod\s*\n\s*def (\w+)\(", python_source)


def pick_impl_method(methods: list[str], entry_point: str) -> str | None:
    if not methods:
        return None

    lowered = {m.lower(): m for m in methods}
    if entry_point.lower() in lowered:
        return lowered[entry_point.lower()]

    pascal = to_pascal_case(entry_point)
    if pascal in methods:
        return pascal

    impl_candidates = [
        m
        for m in methods
        if m not in {"__init__"} and not m.endswith("Spec") and "Spec" not in m
    ]
    if len(impl_candidates) == 1:
        return impl_candidates[0]

    for name in impl_candidates:
        if name.lower() == entry_point.lower():
            return name

    for name in impl_candidates:
        if name.lower().replace("_", "") == entry_point.lower().replace("_", ""):
            return name

    return None
