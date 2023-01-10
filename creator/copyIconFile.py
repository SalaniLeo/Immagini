import shutil
from os import path
import ui.errorWindow

def copyIcon(icon,appDirPath,iconName):

    dst = appDirPath + iconName

    iconPath = icon

    if path.exists(iconPath):

        shutil.copy(icon, dst)

    
    else:
        ui.errorWindow.error_message("could not copy icon")
        # sys.exit("could not copy icon")