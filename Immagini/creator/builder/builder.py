import os
from ...ui.console import console
import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gtk

# import shutil

def initBuild(appDirPath, output, name, flatpak, mainWindow, thread=None):
    # os.system("ARCH=x86_64 ./creator/builder/appimagetool-x86_64.AppImage " + "'" + appDirPath + "'" + " " + output + "/" + name + "-x86_64.AppImage")
    # shutil.move(name + "-x86_64.AppImage", output + "/" + name + "-x86_64.AppImage")

    if flatpak:
        toolDir = "/app/bin/Immagini/creator/builder/tool/AppRun"
    else:
        toolDir = "Immagini/creator/builder/tool/AppRun"

    # os.chmod(toolDir, 777)
    buildoutput = os.popen("ARCH=x86_64 " + toolDir + " '" + appDirPath + "'" + " '" + output + "/" + name + "-x86_64.AppImage' ").read()

    terminal = Gtk.TextView()
    terminal.set_editable(False)

    bff = Gtk.TextBuffer()
    terminal = Gtk.TextView(buffer = bff)

    iter = bff.get_end_iter()
    bff.insert(iter, buildoutput)

    consolePage = console(mainWindow, terminal)
    consolePage.present()



    return buildoutput