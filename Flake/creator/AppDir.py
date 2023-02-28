import os
from ..ui.error import throwError
from os import path

def createAppDir(appDirPath,folderMode, self, mainWindow):

    folder = appDirPath + "usr/bin"

    if not path.exists(folder):
        if not folderMode:
            os.makedirs(appDirPath + "usr/bin")
    else:
        throwError(self, "the folder already exists", "Can't create .AppDir folder", mainWindow)
        