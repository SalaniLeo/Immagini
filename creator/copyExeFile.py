import shutil
import os
from os import path
import ui.errorWindow

# default copyExe option
def copyExe(exe,appDirPath,exeName):

    # exe file copy destination
    dst = appDirPath + "usr/bin/" + exeName

    # checks if exe file exists
    if path.exists(exe):
        shutil.copyfile(exe, dst)
        os.chmod(dst, 777)
    
    else:
        ui.errorWindow.error_message("could not copy the exe file")
        # sys.exit("could not copy the exe file")
        
def copyExePFolder(appDirPath,exeName,parentFolder):
    
    # gets parent folder name from complete directory
    pFolderName = os.path.normpath(parentFolder)
    
    if path.exists(parentFolder):
        shutil.copyfile(parentFolder, appDirPath)
        os.chmod(appDirPath + pFolderName + exeName, 777)

        