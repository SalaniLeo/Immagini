import os
import stat
import glob
import pathlib
import subprocess
import gi
from .imageOptions import manageImages
from ..creator import error
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk, Pango, Gdk

class getImages(list):
    def __init__(self, list, loc): 

        i = 0
        self.appimages = 0
        self.executable = []
        self.names = []

        for x in list:
            file = pathlib.Path(list[i-1])
            i += 1
            self.file_extension = file.suffix
            if(self.file_extension == ".AppImage"):
                self.appimages += 1
                name = str(loc) + '/' + str(file).encode('utf-8').decode()
                self.names.append(name)
                names.append(self.names)

    def createElements(appImage):

        box = Gtk.Button()
        margin = 1
        box.set_margin_start(margin)
        box.set_margin_end(margin)
        box.set_margin_top(margin)
        box.set_margin_bottom(margin)

        imageName = os.path.splitext(appImage)[0]

        fullName = os.path.basename(imageName)
        baseName = fullName.replace("-x86_64", "")
        name = Gtk.Label(label=baseName)
        name.set_max_width_chars(15)
        name.set_ellipsize(Pango.EllipsizeMode.END)
        name.set_halign(Gtk.Align.CENTER)

        st = os.stat(appImage)
        executable = bool(st.st_mode & stat.S_IEXEC)

        if not executable:
            box.get_style_context().add_class(class_name='error')

        box.set_size_request(10,50)
        box.set_child(name)
        box.connect("clicked", executeImage, executable, appImage)        

        return box

    def restart_count():
        global desktopCount
        global nameNum
        desktopCount = 0
        nameNum = 0

desktopCount=0
names = []
nameNum = 0

def getFileNum(list, loc):
    return getImages(list, loc)

def executeImage(executable, imagePath):
        if not executable:
            error.throwError(None, "The app has no executable permissions", "Permission denied")
        else:
            subprocess.run(imagePath)