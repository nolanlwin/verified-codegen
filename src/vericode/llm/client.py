from __future__ import annotations

import time
from pathlib import Path
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"


def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / name).read_text(encoding="utf-8")


class OpenAIClient:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        max_retries: int = 3,
        retry_delay: float = 2.0,
    ) -> None:
        self.client = OpenAI(api_key=api_key)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def complete(
        self,
        *,
        model: str,
        system: str,
        user: str,
        schema: type[T],
    ) -> T:
        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                response = self.client.beta.chat.completions.parse(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    response_format=schema,
                )
                parsed = response.choices[0].message.parsed
                if parsed is None:
                    raise ValueError("Model returned no parsed content.")
                return parsed
            except Exception as exc:  # noqa: BLE001 - retry on transient API errors
                last_error = exc
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
        raise RuntimeError(f"OpenAI request failed after {self.max_retries} attempts: {last_error}")
