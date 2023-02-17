import gi
import subprocess
import os
from ..creator import error
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gtk, Gdk, Adw

class manageImages(list):
    def __init__(self, list, loc): 
        menu = Gtk.Menu()
        menu_item = Gtk.MenuItem("A menu item")
        menu.append(menu_item)
        menu_item.show()

    def executeImage(imagePath, executable):
        
        if not executable:
                error.throwError(None, "The app has no executable permissions", "Permission denied")
        else:
                subprocess.run(imagePath)

    def deleteImage(button, imagePath, refresh, name, mainWindow):
        manageImages.askSure(name, imagePath, refresh, mainWindow)

    def askSure(name, imagePath, refresh, mainWindow):

        dialog = Adw.MessageDialog.new()

        dialog.set_transient_for(mainWindow)
        dialog.set_modal(True)
        dialog.set_heading(heading='Delete ' + name + "?")
        dialog.set_body(body='Deleting an appimage file is not reversible')
        dialog.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancel')
        dialog.set_response_appearance(
            response=Gtk.ResponseType.CANCEL.value_nick,
            appearance=Adw.ResponseAppearance.DESTRUCTIVE
        )
        dialog.add_response(Gtk.ResponseType.OK.value_nick, 'Ok')
        dialog.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )
        dialog.connect('response', manageImages.dialog_response, imagePath, refresh)

        dialog.present()

    def dialog_response(dialog, response, imagePath, refresh):
        if response == Gtk.ResponseType.OK.value_nick:
            os.remove(imagePath)
            refresh(None, None, None)
        elif response == Gtk.ResponseType.CANCEL.value_nick:
            None

    def imageOptions(button, appImage, refresh, baseName,mainWindow):
        options = imageOptions(mainWindow)
        options.show()
        
    def startImage(button, appImage, refresh, baseName,mainWindow):
        None


class imageOptions(Adw.PreferencesWindow):

    def __init__(self, parent,  **kwargs):
        super().__init__(**kwargs)   
        self.set_title(title='Image options')
        self.set_transient_for(parent)
        self.set_modal(True)


