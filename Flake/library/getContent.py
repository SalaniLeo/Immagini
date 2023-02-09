import os
import stat
import shutil

def extractAppImage(appImagePath):

    if os.path.exists('squashfs-root'):
        shutil.rmtree('squashfs-root')

    if not isExecutable(appImagePath):
        os.system("chmod 777 " + appImagePath) 

    os.popen(appImagePath + " --appimage-extract")

    shutil.copy2('/home/leo/Apps/Visual Studio Code/flake/Flake/library/squashfs-root/icon.svg', '/home/leo/Desktop')

def isExecutable(appImagePath):
    print(appImagePath)
    st = os.stat(appImagePath)
    return bool(st.st_mode & stat.S_IEXEC)

def getInfo(path):
    extractAppImage(path)
