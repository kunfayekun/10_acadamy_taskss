def transcribe_audio(audio_file_path: str) -> str:
    """Minimal, safe stub used to allow tests to run to TDD failure points.

    Returns a short placeholder transcript for the provided audio path.
    """
    if not isinstance(audio_file_path, str):
        raise TypeError("audio_file_path must be a string")
    return "[placeholder transcript]"
