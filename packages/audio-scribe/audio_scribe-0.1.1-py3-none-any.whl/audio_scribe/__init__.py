try:
    from alive_progress import alive_bar
    import psutil
    import GPUtil
    HAVE_PROGRESS_SUPPORT = True
except ImportError:
    HAVE_PROGRESS_SUPPORT = False

from .cli import (
    main,
    TranscriptionPipeline,
    TranscriptionConfig,
    AudioProcessor,
    TokenManager,
    DependencyManager,
    get_token,
    complete_path,
)

__version__ = "0.1.1"

__all__ = [
    "main",
    "TranscriptionPipeline",
    "TranscriptionConfig",
    "AudioProcessor",
    "TokenManager",
    "DependencyManager",
    "get_token",
    "complete_path",
    "HAVE_PROGRESS_SUPPORT",
]