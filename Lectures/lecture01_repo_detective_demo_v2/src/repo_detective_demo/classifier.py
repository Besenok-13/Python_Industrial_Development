"""Very small classifier used to trace a behavior path."""
REFUND_MARKERS = ("refund", "money back", "return my money")

def classify(text: str) -> str:
    normalized = text.lower().strip()
    if any(marker in normalized for marker in REFUND_MARKERS):
        return "refund"
    return "other"
