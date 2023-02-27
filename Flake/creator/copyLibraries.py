import shutil
import os
from ..ui.error import throwError
import shutil

# default copyExe option
def copyLibraries(libraries, appDirPath, self, mainWindow):

    num = len(libraries)
    libArray = libraries.split(',')

    print(libArray)

    for x in range(len(libArray)):

        if os.path.exists(libArray[x]):
            dst = appDirPath + "usr/lib/" + os.path.basename(libArray[x])
            print(libArray[x], dst)
            # shutil.copyfile(libArray[x], dst)
            os.chmod(dst, 777)
        else:
            print(libArray[x])
            throwError(self, "could not copy library '" + libArray[x] + "'", "Library does not exist", mainWindow)
        # sys.exit("could not copy the exe file")






        