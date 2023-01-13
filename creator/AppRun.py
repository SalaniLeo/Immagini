import os
import shutil
import os
from os import path
import ui.errorWindow

def createAppRunFile(exeName,appDirPath,folderMode,exePathFolderMode,pFolderName):

  f = open(appDirPath + "AppRun", "w")

  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  if not folderMode:
    f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  elif folderMode:
    f.writelines("\nEXEC=\"${HERE}/"+ pFolderName + exePathFolderMode + "\"")
  f.writelines("\nexec \"${EXEC}\"")
  f.close()
  os.system("chmod +x '" + appDirPath + "AppRun'")

  
def copyAppRunFile(AppRun,appDirPath):

    dst = appDirPath + "AppRun"

    if path.exists(AppRun):
        shutil.copyfile(AppRun, dst)
        os.chmod(dst, 777)
    
    else:
        ui.errorWindow.error_message("could not copy the AppRun file")
        # sys.exit("could not copy the exe file")



