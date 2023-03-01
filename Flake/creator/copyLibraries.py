import shutil
import os
from ..ui.error import throwError
import shutil

# default copyExe option
def copyLibraries(libraries, appDirPath, self, mainWindow):

    num = len(libraries)
    libArray = libraries.split('\n')

    x = 0

    for x in range(len(libArray)):

        if x == 0:
            src = '/'+libArray[x][1:]
        else:
            src = libArray[x][1:]

        if os.path.exists(src):
            dst = appDirPath + "usr/lib/" + os.path.basename(libArray[x])

            if x == 0:
                shutil.copy(src, dst)
            else:
                shutil.copy(src, dst)

            os.chmod(dst, 777)
        else:
            throwError(self, "could not copy library  '" + libArray[x][1:] + "'", "Library does not exist", mainWindow)
        # sys.exit("could not copy the exe file")






        