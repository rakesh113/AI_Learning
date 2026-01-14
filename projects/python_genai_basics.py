def normalize_text(text: str) -> str:
    """
    Clean and normalize text for LLM processing.
    """
    return text.strip().lower()


if __name__ == "__main__":
    sample = "  Hello AI Agent  "
    print(normalize_text(sample))
