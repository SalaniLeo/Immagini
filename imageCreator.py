import os
import ntpath
import creator.desktopFile
import creator.AppDir
import creator.AppRun
import creator.copyExeFile
import creator.copyIconFile
import creator.builder.builder
import ui.errorWindow

name = None
exe = None
icon = None
type = None
categories = None

def start(name,exe,icon,type,categories,output,customAppRun,appRunLoc):

    print("[name] " + name)
    print("[exe dir] " + exe)
    print("[icon dir] " + icon)
    print("[type] " + type)
    print("[category] " + categories)
    print("[output location] " + output)
    
    exeName = ntpath.basename(exe)
    iconName = ntpath.basename(icon)
    appDirPath = output + "/" + name + ".AppDir/"

    creator.AppDir.createAppDir(appDirPath)
    creator.desktopFile.createDesktopFile(name,exeName,iconName,type,categories,appDirPath)
    if not(customAppRun):
            creator.AppRun.createAppRunFile(exeName,appDirPath)
    elif(customAppRun):
        if(ntpath.basename(appRunLoc)!="AppRun"):
            ui.errorWindow.error_message("AppRun file not valid. \nTry renaming the file to 'AppRun'")
            return 0
        creator.AppRun.copyAppRunFile(appRunLoc,appDirPath)
            
        creator.copyExeFile.copyExe(exe,appDirPath,exeName)
        creator.copyIconFile.copyIcon(icon,appDirPath,iconName)



    outputtxt = creator.builder.builder.initBuild(appDirPath,output,name)

    return outputtxt