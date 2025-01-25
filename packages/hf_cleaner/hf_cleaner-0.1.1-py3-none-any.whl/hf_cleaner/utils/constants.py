import os

PLATFORM = ["darwin", "linux", "windows"]

CACHE_LOC = {
        "darwin": os.path.expanduser("~/.cache/huggingface/hub"),
        "linux": os.path.expanduser("~/.myapp"),
        "win32": os.path.expandvars("%APPDATA%\\MyApp"),
    }
