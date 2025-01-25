"""HAPM integration package module"""
from __future__ import annotations

from os import listdir, remove
from os.path import join
from pathlib import Path
from shutil import copyfile

from git import Repo
from github import Github

from hapm.color import ANSI_DIM, ANSI_YELLOW, ink
from hapm.git import get_release_file, get_tree_file
from hapm.package import BasePackage

FOLDER_NAME = "www/custom_lovelace"
RESOURCES_REDIRECT_URL = "https://my.home-assistant.io/redirect/lovelace_resources/"


class PluginPackage(BasePackage):
    """PluginPackage represent `.js` plugin packages"""

    repo: Repo

    kind = "plugins"
    extension = "js"

    def initialize(self) -> None:
        """Method will be called if the entity is created for the first time.
        It should initialise the files on the system"""
        self._download_script(self.version)

    def switch(self, version: str) -> None:
        """Method should switch the version of the installed package"""
        self._download_script(version)
        remove(self.path())
        self.version = version

    def export(self, path: str) -> None:
        """Method should offload the package payload to the specified folder"""
        copyfile(self.path(), f"{join(path, FOLDER_NAME, self.name)}.js")

    @staticmethod
    def pre_export(path: str):
        """This method is called when you starting
        exporting packages of a certain kind"""
        path_dir = Path(join(path, FOLDER_NAME))
        path_dir.mkdir(exist_ok=True, parents=True)

    @staticmethod
    def post_export(path: str):
        """Do nothing"""
        heading = (
            "To connect JS plugins, they must be specified on the Lovelace resources.\n"
            "Make sure those links are there:"
        )
        print(ink(heading, ANSI_YELLOW))
        plugins_dir = join(path, FOLDER_NAME)
        prefix = ink("*", effects=ANSI_DIM)
        for plugin in listdir(plugins_dir):
            print(f"{prefix} /local/custom_lovelace/{plugin}")
        print(ink(f"Resources URL: {RESOURCES_REDIRECT_URL}", effects=ANSI_DIM))

    def _download_script(self, version: str):
        content = self._get_script(version)
        with open(self.path(version), "wb") as file:
            file.write(content)

    def _get_script(self, version: str) -> str | None:
        plugin_file = f"{self.name}.js"
        if plugin_file.startswith("lovelace-"):
            plugin_file = plugin_file.replace("lovelace-", "")

        api = Github(self._api_token)
        repo = api.get_repo(self.full_name)
        content = get_tree_file(repo, version, f"dist/{plugin_file}")
        if content is not None:
            return content
        content = get_tree_file(repo, version, plugin_file)
        if content is not None:
            return content
        content = get_release_file(repo, version, plugin_file)
        if content is not None:
            return content
        return None
