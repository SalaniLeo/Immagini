import os

def createDesktopFile(name,exeName,iconName,type,categories,appDirPath):

  icon = os.path.splitext(iconName)[0]

  f = open(appDirPath + name + ".desktop", "w")

  f.writelines("[Desktop Entry]")
  f.writelines("\nName=" + name)
  f.writelines("\nExec=" + exeName)
  f.writelines("\nIcon=" + icon)
  f.writelines("\nType=" + type)
  f.writelines("\nCategories=" + categories)
  f.close()