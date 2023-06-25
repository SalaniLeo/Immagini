import os
from os import path
from ..ui.error import throwError
from ..ui.strings import *
import shutil

# default copyExe option
def copyExe(exe,appDirPath,exeName, self, mainWindow):

    # exe file copy destination
    dst = appDirPath + "usr/bin/" + exeName

    # checks if exe file exists
    if path.exists(exe):
        shutil.copyfile(exe, dst)
    else:
        throwError(self, invalidExeSubtitle, invalidExeTitle, mainWindow)

def copyExePFolder(appDirPath,pFolderName,parentFolder,exe, self, mainWindow):

    appDirPath = appDirPath + 'usr/' + pFolderName


    if path.exists(parentFolder):
        shutil.copytree(parentFolder, appDirPath)
        os.chmod(exe , 777)
    else:
        throwError(self, invalidExeSubtitle, invalidExeTitle, mainWindow)
