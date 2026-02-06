from datetime import datetime

def fetch_trend(platform: str = "youtube", topic: str = "example") -> dict:
    """Return a minimal trend dict matching `specs/technical.md` contract.

    Keys: platform, topic, trend_score, timestamp
    """
    return {
        "platform": platform,
        "topic": topic,
        "trend_score": 0.0,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
