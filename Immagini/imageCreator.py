import os
import ntpath
from .creator.desktopFile import *
from .creator.AppRun import *
from .creator.copyExeFile import *
from .creator.copyIconFile import *
from .creator.builder.builder import *
from .creator.copyLibraries import *
from .creator.copyInterpreters import *
from .ui.error import *
from .ui.strings import *

def startCreatingImage(name, 
          exe, 
          icon, 
          type, 
          categories, 
          output, 
          useCustomAppRun, 
          appRunLoc, 
          useFolderMode, 
          folderLoc, 
          includeLibraries, 
          librariesPath, 
          includeInterpreters,
          flatpak, 
          self, 
          mainWindow):

    exeName = ntpath.basename(exe)
    appDirPath = output + "/" + name + ".AppDir/"
    pFolderName =  os.path.basename(folderLoc)
    exePathFolderMode = compare(pFolderName, exe, self, mainWindow, useFolderMode)
    binFolder = output + "/" + name + ".AppDir/usr/bin"
    shareFolder = output + "/" + name + ".AppDir/usr/share"
    libFolder = output + "/" + name + ".AppDir/usr/lib"

    createBase(appDirPath, shareFolder, libFolder, binFolder)

    pyLocation = '/usr/bin/python'
    javaLocation = '/usr/bin/java'

    includePython = includeInterpreters[0]
    includeJava = includeInterpreters[1]

    # creates desktop file inside .AppDir folder
    createDesktopFile(name,exeName,type,categories,appDirPath)

    # copies icon file inside .AppDir
    copyIcon(icon, shareFolder, appDirPath, self, mainWindow)

    # checks if custom apprun is enabled
    if not(useCustomAppRun):
        createAppRunFile(exeName,appDirPath,useFolderMode,exePathFolderMode,pFolderName, includeInterpreters, self)
    elif(useCustomAppRun):
        # checks if AppRun is named AppRun
        if(ntpath.basename(appRunLoc)!="AppRun"):
            # throws error in case
            throwError(self, invalidAppRunSubTitle, invalidAppRunTitle, mainWindow)
            return 0
        # copies apprun if everything is ok
        copyAppRunFile(appRunLoc,appDirPath,self, mainWindow)

    # checks if foldermode is enabled
    if not(useFolderMode):
        # if foldermode is not enabled copies executable file normally
        copyExe(exe,appDirPath,exeName, self, mainWindow)
    elif(useFolderMode):
        # if foldermode is enabled moves the entire app inside .AppDir
        copyExePFolder(appDirPath,pFolderName,folderLoc,exe, self, mainWindow)

    if(includeLibraries):
        copyLibraries(librariesPath, appDirPath, self, mainWindow)

    if includeJava:
        copyInterpreters.copyInterpreter(javaLocation, binFolder)
        
    if includePython:
        copyInterpreters.copyInterpreter(pyLocation, binFolder + '/python')

    # sets outputtxt to the appimagetool output
    outputtxt = initBuild(appDirPath,output,name,flatpak, mainWindow)

    return outputtxt

def compare(folderName, s2, self, mainWindow, folderMode):
    if folderMode:
        try:
            result = s2.split(folderName,1)[1]
            return result
        except IndexError:
            throwError(self, invalidAppFolderSubtitle, invalidAppFolderTitle, mainWindow)
    else:
        return None
    
def createBase(appDirPath, shareFolder, libFolder, binFolder):
    os.makedirs(appDirPath)
    os.makedirs(shareFolder)
    os.makedirs(libFolder)
    os.makedirs(binFolder)