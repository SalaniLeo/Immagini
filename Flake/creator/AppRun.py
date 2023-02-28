import os
import shutil
import os
from ..ui.error import throwError
from os import path

def createAppRunFile(exeName,appDirPath,folderMode,exePathFolderMode,pFolderName, self):

  f = open(appDirPath + "AppRun", "w")

  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  if not folderMode:
    f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  elif folderMode:
    f.writelines("\nEXEC=\"${HERE}/usr/"+ pFolderName + exePathFolderMode + "\"")
  f.writelines("\nexec \"${EXEC}\"")
  f.close()
  os.system("chmod +x '" + appDirPath + "AppRun'")

  
def copyAppRunFile(AppRun,appDirPath, self, mainWindow):

    dst = appDirPath + "AppRun"

    if path.exists(AppRun):
        shutil.copyfile(AppRun, dst)
        os.chmod(dst, 777)
    
    else:
        throwError(self, "Selected file must be named 'AppRun'", "Could not copy the AppRun file", mainWindow)


