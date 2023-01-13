import os
import shutil
import os
from os import path
import ui.errorWindow
import ntpath

def createAppRunFile(exeName,appDirPath,folderMode,exe,pFolderName):

  f = open(appDirPath + "AppRun", "w")

  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  if not folderMode:
    f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  elif folderMode:
    f.writelines("\nEXEC=\"${HERE}/"+ pFolderName + compare(appDirPath,exe)+ "\"")
  f.writelines("\nexec \"${EXEC}\"")
  f.close()
  os.system("chmod +x '" + appDirPath + "AppRun'")

  print(compare(exe,appDirPath))
  
def copyAppRunFile(AppRun,appDirPath):

    dst = appDirPath + "AppRun"

    if path.exists(AppRun):
        shutil.copyfile(AppRun, dst)
        os.chmod(dst, 777)
    
    else:
        ui.errorWindow.error_message("could not copy the AppRun file")
        # sys.exit("could not copy the exe file")
        
        
def compare(s1, s2):
    result = s2.split("AppDir",1)[1]
    return result


