from abc import ABC
from dataclasses import dataclass
from hf_cleaner.utils.file_utils import get_platform


@dataclass
class BaseTemplate(ABC):
    template_name: str = "Default"
    title: str = "HF Cleaner"
    platform: str = ""

    @staticmethod
    def get_os():
        os_name = get_platform()
        print(os_name)

