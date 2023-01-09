import os
import shutil
import os
from os import path
import ui.errorWindow
import ntpath

def createAppRunFile(exeName,appDirPath):

  f = open(appDirPath + "AppRun", "w")

  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  f.writelines("\nexec \"${EXEC}\"")
  f.close()


  os.system("chmod +x '" + appDirPath + "AppRun'")
  
  
def copyAppRunFile(AppRun,appDirPath):

    dst = appDirPath + "AppRun"
        
    # if(ntpath.basename(AppRun) is not "AppRun"):
    #   ui.errorWindow.error_message("AppRun file not valid. \n Try renaming the file to 'AppRun'")
    #   exit

    if path.exists(AppRun):
        shutil.copyfile(AppRun, dst)
        print(AppRun)
        print(dst)
        os.chmod(dst, 777)
    
    else:
        ui.errorWindow.error_message("could not copy the AppRun file")
        # sys.exit("could not copy the exe file")
        