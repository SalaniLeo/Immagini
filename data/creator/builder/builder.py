import os
import pathlib

# import shutil

def initBuild(appDirPath, output, name):
    # os.system("ARCH=x86_64 ./creator/builder/appimagetool-x86_64.AppImage " + "'" + appDirPath + "'" + " " + output + "/" + name + "-x86_64.AppImage")
    # shutil.move(name + "-x86_64.AppImage", output + "/" + name + "-x86_64.AppImage")

    toolDir = "/app/bin/data/creator/builder/tool/AppRun"

    # os.chmod(toolDir, 777)

    buildoutput = os.popen("ARCH=x86_64 " + toolDir + " '" + appDirPath + "'" + " '" + output + "/" + name + "-x86_64.AppImage' ").read()

    return buildoutput