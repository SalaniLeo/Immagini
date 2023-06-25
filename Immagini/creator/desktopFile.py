import os
import shutil
import ntpath

def createDesktopFile(name,exeName,iconName,type,categories,appDirPath):

  tmp = ntpath.basename(iconName)
  icon = os.path.splitext(tmp)[0]

  f = open(appDirPath + name + ".desktop", "w")

  f.writelines("[Desktop Entry]")
  f.writelines("\nName=" + name)
  f.writelines("\nExec=" + exeName)
  f.writelines("\nIcon=" + icon)
  f.writelines("\nType=" + type)
  f.writelines("\nCategories=" + categories)
  f.close()
  
def copyDesktopFile(file, dest):
  shutil.copy(file, dest)