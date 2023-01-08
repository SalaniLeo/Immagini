import os
import ntpath
import creator.desktopFile
import creator.AppDir
import creator.AppRun
import creator.copyExeFile
import creator.copyIconFile
import creator.builder.builder

name = None
exe = None
icon = None
type = None
categories = None

def start(name,exe,icon,type,categories,output):

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
    creator.AppRun.createAppRunFile(exeName,appDirPath)
    creator.copyExeFile.copyExe(exe,appDirPath,exeName)
    creator.copyIconFile.copyIcon(icon,appDirPath,iconName)


    outputtxt = creator.builder.builder.initBuild(appDirPath,output,name)

    return outputtxt