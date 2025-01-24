import imageio_ffmpeg as ffmpeg # type: ignore

def is_ffmpeg_installed():
    """Check if FFmpeg is installed by trying to get its executable path."""
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()
    if ffmpeg_path:
        return True
    return False

def get_ffmpeg_path():
    """Return the path to FFmpeg executable."""
    return ffmpeg.get_ffmpeg_exe()
