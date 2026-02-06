def transcribe_audio(audio_file_path: str) -> str:
    """Minimal stub: return a placeholder transcript for given audio path."""
    if not isinstance(audio_file_path, str):
        raise TypeError("audio_file_path must be a string")
    return "This is a placeholder transcript."
