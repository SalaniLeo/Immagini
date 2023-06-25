import os
import shutil
import os
from pathlib import Path
from ..ui.error import throwError
from ..ui.strings import *
from os import path

def createAppRunFile(exeName,appDirPath,folderMode,exePathFolderMode,pFolderName, includeInterpreters, self):

  try:
    includePython = includeInterpreters[0]
    includeJava = includeInterpreters[1]
  except:
    None
    
  executeMethod = "exec"

  f = open(appDirPath + "AppRun", "w")
  
  try:
    if exeName.split('.')[1] == 'py':
      executeMethod = 'python'
      if includePython:
        executeMethod = '${HERE}/usr/bin/python'
      
    if exeName.split('.')[1] == 'jar':
      executeMethod = 'java --jar'
  except:
    None
    
  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  if not folderMode:
    f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  elif folderMode:
    path = Path(exePathFolderMode)
    if str(path.parent.absolute())[0:] == pFolderName:
      f.writelines("\nEXEC=\"${HERE}/usr/"+ pFolderName + exeName + "\"")
    else:
      f.writelines("\nEXEC=\"${HERE}/usr/"+ pFolderName + exePathFolderMode + "\"")
  f.writelines('\n' + executeMethod + " ${EXEC}")
  f.close()
  os.system("chmod +x '" + appDirPath + "AppRun'")

  
def copyAppRunFile(AppRun,appDirPath, self, mainWindow):

    dst = appDirPath + "AppRun"

    if path.exists(AppRun):
        shutil.copyfile(AppRun, dst)
        os.chmod(dst, 777)
    
    else:
        throwError(self, invalidAppRunSubTitle, invalidAppRunTitle, mainWindow)


