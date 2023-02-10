import os
import pathlib

# import shutil

def initBuild(appDirPath, output, name):
    # os.system("ARCH=x86_64 ./creator/builder/appimagetool-x86_64.AppImage " + "'" + appDirPath + "'" + " " + output + "/" + name + "-x86_64.AppImage")
    # shutil.move(name + "-x86_64.AppImage", output + "/" + name + "-x86_64.AppImage")

<<<<<<< Updated upstream:Flake/library/squashfs-root/usr/bin/creator/builder/builder.py
    toolDir = "bin/creator/builder/tool/AppRun"
=======
    # toolDir = "/app/bin/Flake/creator/builder/tool/AppRun"
    toolDir = "data/creator/builder/tool/AppRun"
>>>>>>> Stashed changes:Flake/creator/builder/builder.py

    # os.chmod(toolDir, 777)

    buildoutput = os.popen("ARCH=x86_64 " + toolDir + " '" + appDirPath + "'" + " '" + output + "/" + name + "-x86_64.AppImage' ").read()

    return buildoutput
