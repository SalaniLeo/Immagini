import shutil
from os import path
import creator.error

def copyIcon(icon,appDirPath,iconName, self):

    dst = appDirPath + iconName

    iconPath = icon

    if path.exists(iconPath):

        shutil.copy(icon, dst)

    
    else:
        creator.error.throwError(self, "could not copy icon", "icon file does't exist")
        # sys.exit("could not copy icon")