import shutil
import os
from os import path
from ..ui.error import throwError
from PIL import Image
from ..ui.strings import *
import ntpath

def copyIcon(icon, sharePath, appDirPath, self, mainWindow):

    iconExtension = os.path.splitext(icon)[1]
    iconName = ntpath.basename(icon)

    if path.exists(icon):
        if iconExtension == ".png" or iconExtension == ".jpg" or iconExtension == ".jpeg":

            icon_file = icon
            with Image.open(icon_file) as img:
                width, height = img.size
                imageSize = (f"{width}x{height}")

            if check_icon_size(icon):

                    symbolicPath = sharePath + "/icons/hicolor/" + imageSize + "/"
                    dst = symbolicPath + iconName

                    os.makedirs(symbolicPath)
                    shutil.copy(icon, dst)
                    createIconSymlink(dst, appDirPath + iconName)

            else:
                throwError(self, invalidIconSizeSubtitle + ' ' + imageSize, invalidIconSizeTitle, mainWindow)

        elif iconExtension == ".svg":

            symbolicPath = sharePath + "/icons/hicolor/scalable/"
            dst = symbolicPath + iconName

            os.makedirs(symbolicPath)
            shutil.copy(icon, dst)
            os.symlink(dst, appDirPath + iconName)

    else:
        throwError(self, invalidIconTitle, invalidIconSubtitle, mainWindow)

def createIconSymlink(src, dst):
    os.symlink(src, dst)


def check_icon_size(filepath):
    valid_sizes = [8, 16, 32, 48, 64, 128, 256, 512]

    with Image.open(filepath) as img:
        width, height = img.size

        if width == height and width in valid_sizes:
            return True
        else:
            return False