import os
import imageCreator
import ui.errorWindow
from os import path

def createAppDir(appDirPath):

    folder = appDirPath + "usr/bin"

    if not path.exists(folder):
        os.makedirs(appDirPath + "usr/bin")
    else:
        ui.errorWindow.error_message("the folder already exists")
        