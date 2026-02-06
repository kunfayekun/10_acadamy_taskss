def download_youtube_video(video_url: str) -> str:
    """Minimal, safe stub used to allow tests to run to TDD failure points.

    Returns a deterministic placeholder path for the given video URL.
    """
    if not isinstance(video_url, str):
        raise TypeError("video_url must be a string")
    return "downloads/example_video.mp4"
