import os
import ntpath
import creator.desktopFile
import creator.AppDir
import creator.AppRun
import creator.copyExeFile
import creator.copyIconFile
import creator.builder.builder
import ui.errorWindow

# name = None
# exe = None
# icon = None
# type = None
# categories = None

def start(name,exe,icon,type,categories,output,customAppRun,appRunLoc,folderMode,folderLoc):

    # prints options for terminal output
    print("[name] " + name)
    print("[exe dir] " + exe)
    print("[icon dir] " + icon)
    print("[type] " + type)
    print("[category] " + categories)
    print("[output location] " + output)
    
    exeName = ntpath.basename(exe)
    iconName = ntpath.basename(icon)
    appDirPath = output + "/" + name + ".AppDir/"

    # creates initial .AppDir folder
    creator.AppDir.createAppDir(appDirPath)
    # creates desktop file inside .AppDir folder
    creator.desktopFile.createDesktopFile(name,exeName,iconName,type,categories,appDirPath)
    
    # checks if custom apprun is enabled
    if not(customAppRun):
            creator.AppRun.createAppRunFile(exeName,appDirPath)
    # if not
    elif(customAppRun):
        # checks if AppRun is named AppRun
        if(ntpath.basename(appRunLoc)!="AppRun"):
            # throws error in case
            ui.errorWindow.error_message("AppRun file not valid. \nTry renaming the file to 'AppRun'")
            return 0
        # copies apprun if everything is ok
        creator.AppRun.copyAppRunFile(appRunLoc,appDirPath)
            
    # checks if foldermode is enabled
    if not(folderMode):
        # if foldermode is not enabled copies executable file normally
        creator.copyExeFile.copyExe(exe,appDirPath,exeName)
    elif(folderMode):
        # if foldermode is enabled moves the entire app inside .AppDir
        creator.copyExeFile.copyExePFolder(exe,appDirPath,exeName,folderLoc)
        
    # copies icon file inside .AppDir
    creator.copyIconFile.copyIcon(icon,appDirPath,iconName)


    # sets outputtxt to the appimagetool output
    outputtxt = creator.builder.builder.initBuild(appDirPath,output,name)

    return outputtxt