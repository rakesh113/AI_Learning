from dataclasses import dataclass


@dataclass(frozen=True)
class LLMConfig:
    model_name: str
    max_tokens: int
    temperature: float


DEFAULT_LLM_CONFIG = LLMConfig(
    model_name="gpt-4o-mini",
    max_tokens=256,
    temperature=0.2
)
