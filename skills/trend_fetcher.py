from datetime import datetime


def fetch_trend(platform: str = "youtube", topic: str = "example") -> dict:
    """Minimal, safe stub used to allow tests to run to TDD failure points.

    Returns a trend dict matching the JSON schema in `specs/technical.md`.
    """
    return {
        "platform": platform,
        "topic": topic,
        "trend_score": 0.0,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
