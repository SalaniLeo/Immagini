import os
import imageCreator
import ui.errorWindow
from os import path

def createAppDir(appDirPath,folderMode):

    folder = appDirPath + "usr/bin"

    if not path.exists(folder):
        if not folderMode:
            os.makedirs(appDirPath + "usr/bin")
        elif folderMode:
            os.makedirs(appDirPath)
    else:
        ui.errorWindow.error_message("the folder already exists")
        