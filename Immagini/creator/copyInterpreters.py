import os
from ..ui.error import throwError
import shutil

class copyInterpreters:
    def copyInterpreter(location, destination):
        if os.path.isdir(location):
            copyInterpreters.copyFolder(location, destination)
        elif os.path.isfile(location):
            copyInterpreters.copyFile(location, destination)

    def copyFolder(location, destination):
        shutil.copytree(location, destination)
        
    def copyFile(location, destination):
        shutil.copy(location, destination)
