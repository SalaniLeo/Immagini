import shutil
import os
from os import path
import ui.errorWindow
import sys

def copyExe(exe,appDirPath,exeName):

    dst = appDirPath + "usr/bin/" + exeName

    exepath = exe

    if path.exists(exepath):
        shutil.copyfile(exe, dst)
        os.chmod(dst, 777)
    
    else:
        ui.errorWindow.error_message("could not copy the exe file")
        # sys.exit("could not copy the exe file")
        
def copyExePFolder(exe,appDirPath,exeName,parentFolder):
    
    dst = appDirPath + "usr/bin/" + exeName

        