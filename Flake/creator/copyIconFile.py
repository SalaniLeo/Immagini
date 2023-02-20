import shutil
from os import path
from .error import throwError

def copyIcon(icon,appDirPath,iconName, self):

    dst = appDirPath + iconName

    iconPath = icon

    if path.exists(iconPath):

        shutil.copy(icon, dst)

    
    else:
        throwError(self, "could not copy icon", "icon file does't exist")
        # sys.exit("could not copy icon")