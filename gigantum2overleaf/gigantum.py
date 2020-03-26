import os
from pathlib import Path

from gigantum2overleaf.utils import call_subprocess


class Gigantum:
    def __init__(self, overleaf_project_root: str):
        self.setup_gigantum_in_overleaf(overleaf_project_root)

    @staticmethod
    def get_project_root() -> str:
        """Method to get the project root directory

        Returns:
            str
        """
        return "/mnt/labbook"

    @staticmethod
    def get_gigantum_directory() -> str:
        """Method to get the .gigantum directory

        Returns:
            str
        """
        return os.path.join(Gigantum.get_project_root(), ".gigantum")

    @staticmethod
    def get_overleaf_root_directory() -> str:
        """Method to get the root overleaf directory

        Returns:
            str
        """
        return os.path.join(Gigantum.get_project_root(), "output/untracked/overleaf")

    @staticmethod
    def get_current_revision() -> str:
        """

        Returns:

        """
        return call_subprocess(['git', 'rev-parse', 'HEAD'], Gigantum.get_project_root()).strip()

    @staticmethod
    def setup_gigantum_in_overleaf(overleaf_project_root: str) -> None:
        """

        Returns:

        """
        directories = [Path(overleaf_project_root, 'gigantum'),
                       Path(overleaf_project_root, 'gigantum', 'metadata'),
                       Path(overleaf_project_root, 'gigantum', 'data'),
                       Path(overleaf_project_root, 'gigantum', 'subfiles'),
                       ]

        for d in directories:
            if not d.is_dir():
                d.mkdir()

        if not Path(overleaf_project_root, 'gigantum', 'README.txt').is_file():
            readme = """
            sdf
"""
            with open(Path(overleaf_project_root, 'gigantum', 'README.txt').as_posix(), 'wt') as rf:
                rf.write(readme)
