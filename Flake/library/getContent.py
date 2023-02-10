import os
import stat
import shutil
<<<<<<< Updated upstream

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
=======
import glob
import time
import pathlib
import gi
import threading
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

def createElements(path, imageList):

    desktopFile = glob.glob('squashfs-root/*.desktop')

    name = getContent.getName(path, desktopFile)

    if name is None or "":
        name = "a"

    button = Gtk.Button()
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    # image = Gtk.Image.new_from_file(getContent.getIcon(path))
    # box.append(image)
    label = Gtk.Label()
    label.set_text(name)
    box.append(label)
    button.set_size_request(100,50)
    button.set_child(box)
    button.connect('clicked', buttonClicked, path, imageList)

    return button

def extractAppImage(imageLoc):

    if not isExecutable(imageLoc):
        os.system("chmod 777 " + imageLoc) 

    os.popen(imageLoc + " --appimage-extract *.desktop").read
    

def isExecutable(path):
    st = os.stat(path)
    return bool(st.st_mode & stat.S_IEXEC)


class getImages(list):
    def __init__(self, list, loc): 

        i = 0
        self.appimages = 0
        self.names = []

        for x in list:
            file = pathlib.Path(list[i-1])
            i += 1
            self.file_extension = file.suffix
            if(self.file_extension == ".AppImage"):
                self.appimages += 1   
                name = str(loc) + '/' + str(file).encode('utf-8').decode()
                self.names.append(name)
                extractAppImage(name)


desktopCount=0

class getContent():

    global appimageLoc

    # def getIcon(path):
    #     os.popen(path + " --appimage-extract *.svg").read
    #     time.sleep(0)
    #     iconFIle = glob.glob('squashfs-root/.DirIcon')
    #     # return(str(iconFIle[0]))
    #     print(str(iconFIle[0]))
    #     if os.path.islink(str(iconFIle)):
    #         image = os.readlink(str(iconFIle))
    #         print(image)
    #         os.popen(path + " --appimage-extract " + str(image)).read
    #     return(str(iconFIle))


    def getName(path, desktopFile):

        global desktopCount

        contents = pathlib.Path(str(desktopFile[desktopCount])).read_text()
        desktopCount = desktopCount + 1
        for line in contents.split("\n"):
            if line.startswith("Name="):
                return(line.split("=")[1])


def getFileNum(list, loc):
    return getImages(list, loc)



def buttonClicked(button, imagePath, imageList):
    os.system("chmod +x " + imageList)
    t1 = threading.Thread(target=execProgram(imageList))
    t1.start()

def execProgram(imageList):
    os.system(imageList)
>>>>>>> Stashed changes
