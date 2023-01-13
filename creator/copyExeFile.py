import shutil
import os
from os import path
import ui.errorWindow
from distutils.dir_util import copy_tree
import shutil, errno

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
        
def copyExePFolder(appDirPath,pFolderName,parentFolder,exePathFolderMode):
    
    # gets parent folder name from complete directory
    parentFolder = parentFolder

    appDirPath = appDirPath + pFolderName
    if path.exists(parentFolder):
        shutil.copytree(parentFolder, appDirPath)
        os.chmod(appDirPath + exePathFolderMode , 777)




        