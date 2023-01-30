import shutil
import os
from os import path
from .error import throwError
import shutil

# default copyExe option
def copyExe(exe,appDirPath,exeName, self):

    # exe file copy destination
    dst = appDirPath + "usr/bin/" + exeName

    # checks if exe file exists
    if path.exists(exe):
        shutil.copyfile(exe, dst)
        os.chmod(dst, 777)
    
    else:
        throwError(self, "could not copy the exe file", "exe file does't exist")
        # sys.exit("could not copy the exe file")
        
def copyExePFolder(appDirPath,pFolderName,parentFolder,exe, self):
    
    # gets parent folder name from complete directory
    parentFolder = parentFolder

    appDirPath = appDirPath + pFolderName
    if path.exists(parentFolder):
        shutil.copytree(parentFolder, appDirPath)
        os.chmod(exe , 777)
    else:
        throwError(self, "could not copy the exe file", "exe file does't exist")





        