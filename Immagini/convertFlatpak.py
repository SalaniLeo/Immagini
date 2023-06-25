from .creator.desktopFile import createDesktopFile
from .creator.AppRun import createAppRunFile
from .creator.copyIconFile import createIconSymlink
from .creator.builder.builder import initBuild
from .ui.error import folderExistsError
from .ui.strings import *
from .ui.error import throwError
import os
import shutil

def startConvertingFlatpak(page, libraryLoc, appName, desktopFile, self):
    appDirPath = f'{libraryLoc}/{appName}.AppDir'
    iconLoc = f'{appDirPath}/{self.icon}'
    iconSource = f'{self.flatpakLocation}/{self.iconName}'
    shareFolder = f'{appDirPath}/usr/share'
    shareSource = f'{self.flatpakLocation}/{self.shareLoc}'
    libFolder = f'{appDirPath}/usr/lib'
    libSource = f'{self.flatpakLocation}/{self.libLoc}'
    binFolder = f'{appDirPath}/usr/bin'
    binSource = f'{self.flatpakLocation}/{self.binLoc}'

    if os.path.exists(appDirPath):
        folderExistsError(None, folderAlreadyExistsSubtitle, folderAlreadyExistsTitle, page, appDirPath)
    else:
        os.makedirs(appDirPath)
        os.symlink(f'{appDirPath}/usr', f'{appDirPath}/app')

        print(f'{self.currentLocation}{self.filesLoc}')        

        try:
            shutil.copytree(f'{self.currentLocation}{self.filesLoc}', f'{appDirPath}/usr')
        except:
            throwError(self, couldNotCopyFilesSubtilte, couldNotCopyFilesTitle, self.page, None)

        createDesktopFile(self.appName, self.command, self.icon, 'Application', 'GTK', f'{appDirPath}/')
        createAppRunFile(self.command, f'{appDirPath}/', False, None, None, False, self)
        createIconSymlink(iconSource, iconLoc)
        
        initBuild(appDirPath, self.imageLoc, self.appName, self.flatpak, self.page, None)
        