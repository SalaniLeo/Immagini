import shutil
import os
from os import path
from .error import throwError
from PIL import Image

def copyIcon(icon, sharePath, appDirPath, iconName, self, mainWindow):

    iconPath = icon
    iconExtension = os.path.splitext(icon)[1]

    if path.exists(iconPath):

        if iconExtension == ".png" or iconExtension == ".jpg" or iconExtension == ".jpeg":

            icon_file = iconPath
            with Image.open(icon_file) as img:
                width, height = img.size
                folderName = (f"{width}x{height}")

            if check_icon_size(icon):

                    symbolicPath = sharePath + "/icons/hicolor/" + folderName + "/"
                    dst = symbolicPath + iconName

                    os.makedirs(symbolicPath)
                    shutil.copy(icon, dst)
                    os.symlink(dst, appDirPath + iconName)

            else:
                throwError(self, "The icon size must be 32x32, 48x48 etc.. not " + folderName, "Icon size not valid", mainWindow)

        elif iconExtension == ".svg":

            symbolicPath = sharePath + "/icons/hicolor/scalable/"
            dst = symbolicPath + iconName

            os.makedirs(symbolicPath)
            shutil.copy(icon, dst)
            os.symlink(dst, appDirPath + iconName)

    else:
        throwError(self, "could not copy icon", "icon file does't exist", mainWindow)
    

def check_icon_size(filepath):
    valid_sizes = [8, 16, 32, 48, 64, 128, 256, 512]

    with Image.open(filepath) as img:
        width, height = img.size

        if width == height and width in valid_sizes:
            return True
        else:
            return False