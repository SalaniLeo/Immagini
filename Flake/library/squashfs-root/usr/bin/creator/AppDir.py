import os
from .error import throwError
from os import path

def createAppDir(appDirPath,folderMode, self):

    folder = appDirPath + "usr/bin"

    if not path.exists(folder):
        if not folderMode:
            os.makedirs(appDirPath + "usr/bin")
        elif folderMode:
            os.makedirs(appDirPath)
    else:
        throwError(self, "the folder already exists", "Can't create .AppDir folder")
        