import os
import stat
import shutil
import glob
import time
import pathlib
import gi
import threading
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

def createElements(path, imageList,dir):
    desktopFile = glob.glob(dir + '/squashfs-root/*.desktop')
    name = getContent.getName(desktopFile)

    if name[0] is None or "":
        name[0] = "(app name not found)"

    button = Gtk.Button()
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    # image = Gtk.Image.new_from_file(getContent.getIcon(dir,imageLoc))
    # image.set_size_request(50,50)
    # box.append(image)
    label = Gtk.Label()
    label.set_text(name[0])
    box.append(label)
    # box.append(image)
    button.set_child(box)
    # button.connect('clicked', buttonClicked, path, imageList)

    return button

# imagessss = None

def extractAppImage(imageLoc,dir):

    if not isExecutable(imageLoc):
        os.system("chmod 777 " + imageLoc) 

    os.popen("cd " + dir + " && " + imageLoc + " --appimage-extract *.desktop").read


def isExecutable(path):
    st = os.stat(path)
    return bool(st.st_mode & stat.S_IEXEC)


class getImages(list):
    def __init__(self, list, loc, dir): 

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
                extractAppImage(name, dir)


desktopCount=0

class getContent():

    global appimageLoc

    # def getIcon(path,imageLoc):
    #     os.popen("cd " + dir + " && " + imageLoc + " --appimage-extract *.svg").read

    #     iconFIle = glob.glob(dir + '/squashfs-root/.DirIcon')

    #     return(str(iconFIle))


    def getName(desktopFile):

        global desktopCount
        base = os.path.basename(desktopFile[desktopCount])
        name = os.path.splitext(base)
        desktopCount = desktopCount + 1
        return(name)


def getFileNum(list, loc, dir):
    return getImages(list, loc, dir)

