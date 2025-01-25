import os
import sys
import time
import shutil
import streamlit as st
from .constants import PLATFORM, CACHE_LOC

def get_size_in_path(path="."):
        total_size = 0
        if os.path.exists(path):
            for d in os.scandir(path):
                if d.is_file() and not d.name.startswith(".") and not d.is_symlink():
                    total_size += d.stat().st_size
                elif d.is_dir():
                    total_size += get_size_in_path(d.path)
        return total_size


def get_file_info(path):
    stats = os.stat(path)
    total_size = get_size_in_path(path) / (1000 * 1000)
    return {
        'size': f"{ total_size:.2f} MB",
        'modified': time.ctime(stats.st_mtime),
        'type': 'Directory' if os.path.isdir(path) else 'File'
    }


def delete_item(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return True
    except Exception as e:
        st.error(f"Error deleting {path}: {str(e)}")
        return False


def get_platform():
    os_name = sys.platform
    if os_name not in PLATFORM:
        st.error(f"Not a supported platform ")
    return os_name


def hf_cache_loc():
    """
    Determine a platform-specific file location.

    Returns:
        str: The file location specific to the platform.

    Raises:
        ValueError: If the platform is not supported.
    """

    current_platform = get_platform()

    file_locations = {
        "darwin": CACHE_LOC["darwin"],
        "linux": CACHE_LOC["linux"],
        "win32": CACHE_LOC["win32"],
    }

    # Map sys.platform to user-friendly platform names if needed
    platform_map = {
        "darwin": "Darwin",
        "linux": "Linux",
        "win32": "Windows",
    }

    if current_platform not in file_locations:
        raise ValueError(f"Unsupported platform: {platform_map.get(current_platform, 'Unknown')}")
    return file_locations[current_platform]


# Example Usage
if __name__ == "__main__":
    try:
        file_loc = hf_cache_loc()
        print(f"Platform-specific file location: {file_loc}")
    except ValueError as e:
        print(f"Error: {e}")