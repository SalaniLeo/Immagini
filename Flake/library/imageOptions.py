import gi
import subprocess
from ..creator import error
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk, Pango, Gdk

class manageImages(list):
    def __init__(self, list, loc): 
        menu = Gtk.Menu()
        menu_item = Gtk.MenuItem("A menu item")
        menu.append(menu_item)
        menu_item.show()

    def executeImage(button, imagePath, executable):
            if not executable:
                error.throwError(None, "The app has no executable permissions", "Permission denied")
            else:
                subprocess.run(imagePath)
