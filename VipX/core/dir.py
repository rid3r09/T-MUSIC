import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir("VipX"):
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("🪅𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐢𝐞𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐝.")
