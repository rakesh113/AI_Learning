import re
from typing import List


def normalize_text(text: str) -> str:
    """
    Normalize text for LLM processing.
    - Trim whitespace
    - Collapse multiple spaces
    - Remove non-printable characters
    """
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = "".join(ch for ch in text if ch.isprintable())
    return text


def split_sentences(text: str) -> List[str]:
    """
    Split text into sentences in a simple, deterministic way.
    """
    return [s.strip() for s in text.split(".") if s.strip()]

def build_prompt(system: str, user: str) -> str:
    """
    Build a structured prompt with explicit roles.
    """
    system = normalize_text(system)
    user = normalize_text(user)

    return f"""
    SYSTEM:
    {system}

    USER:
    {user}
    """

def build_structured_prompt(
    system: str,
    context: str,
    task: str,
    constraints: str,
    output_format: str
) -> str:
    return f"""
SYSTEM:
{normalize_text(system)}

CONTEXT:
{normalize_text(context)}

TASK:
{normalize_text(task)}

CONSTRAINTS:
{normalize_text(constraints)}

OUTPUT FORMAT:
{normalize_text(output_format)}
""".strip()




if __name__ == "__main__":
    system_msg = "You are a precise AI assistant."
    user_msg = "   Explain what an AI agent is.   "

    prompt = build_structured_prompt(
        system="You are a precise AI assistant.",
        context="AI agents interact with environments to achieve goals.",
        task="Explain what an AI agent is.",
        constraints="Do not use examples. Do not exceed 2 sentences.",
        output_format="Plain text."
    )
    print(prompt)

