import os

def createAppRunFile(exeName,appDirPath):

  f = open(appDirPath + "AppRun", "w")

  f.writelines("#!/bin/sh")
  f.writelines("\nHERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"")
  f.writelines("\nEXEC=\"${HERE}/usr/bin/" + exeName + "\"")
  f.writelines("\nexec \"${EXEC}\"")
  f.close()


  os.system("chmod +x '" + appDirPath + "AppRun'")