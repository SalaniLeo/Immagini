import os
import ntpath
from .creator.desktopFile import *
from .creator.AppDir import *
from .creator.AppRun import *
from .creator.copyExeFile import *
from .creator.copyIconFile import *
from .creator.builder.builder import *
from .creator.error import *

# name = None
# exe = None
# icon = None
# type = None
# categories = None

def start(name,exe,icon,type,categories,output,customAppRun,appRunLoc,folderMode,folderLoc, flatpak, self, mainWindow):

    # prints options for terminal output
    # print("[name] " + name)
    # print("[exe dir] " + exe)
    # print("[icon dir] " + icon)
    # print("[type] " + type)
    # print("[category] " + categories)
    # print("[output location] " + output)
    
    exeName = ntpath.basename(exe)
    iconName = ntpath.basename(icon)
    appDirPath = output + "/" + name + ".AppDir/"
    pFolderName =  os.path.basename(folderLoc)
    exePathFolderMode = compare(pFolderName,exe, self)
    shareFolder = output + "/" + name + ".AppDir/usr/share"

    os.makedirs(shareFolder)

    # creates initial .AppDir folder
    createAppDir(appDirPath,folderMode, self)
    
    # creates desktop file inside .AppDir folder
    createDesktopFile(name,exeName,iconName,type,categories,appDirPath)
    
    # copies icon file inside .AppDir
    copyIcon(icon, shareFolder, appDirPath, iconName, self, mainWindow)
    
    # checks if custom apprun is enabled
    if not(customAppRun):
            createAppRunFile(exeName,appDirPath,folderMode,exePathFolderMode,pFolderName, self)
    # if not
    elif(customAppRun):
        # checks if AppRun is named AppRun
        if(ntpath.basename(appRunLoc)!="AppRun"):
            # throws error in case
            throwError(self,"Rename the file to 'AppRun'", "AppRun file not valid", mainWindow)
            return 0
        # copies apprun if everything is ok
        copyAppRunFile(appRunLoc,appDirPath,self)
            
    # checks if foldermode is enabled
    if not(folderMode):
        # if foldermode is not enabled copies executable file normally
        copyExe(exe,appDirPath,exeName, self, mainWindow)
    elif(folderMode):
        # if foldermode is enabled moves the entire app inside .AppDir
        copyExePFolder(appDirPath,pFolderName,folderLoc,exe, self)


    # sets outputtxt to the appimagetool output
    outputtxt = initBuild(appDirPath,output,name,flatpak, mainWindow)

    return outputtxt


        
def compare(folderName, s2, self):
    if folderName:
        try:
            result = s2.split(folderName,1)[1]
            return result
        except IndexError:
            throwError(self, "The selected application parent folder does not contain selected executable file", "Parent folder does not contain executable")
    else:
        return None