def download_youtube_video(video_url: str) -> str:
    """Minimal stub: return a placeholder local file path for given URL."""
    if not isinstance(video_url, str):
        raise TypeError("video_url must be a string")
    return "downloads/example_video.mp4"
