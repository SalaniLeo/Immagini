import gi
import sys
import shutil
from ..ui.strings import *
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

def throwError(self, error, title, mainWindow, thread = None):

        dialog = Adw.MessageDialog.new()

        dialog.set_transient_for(mainWindow)
        dialog.set_modal(True)
        
        dialog.set_heading(heading=title)
        dialog.set_body(body=error)
        dialog.add_response(Gtk.ResponseType.OK.value_nick, okButton)
        dialog.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )

        dialog.present()
        
        if thread != None:
            sys.exit()

def folderExistsError(self, error, title, mainWindow, appdir, thread=None):
        dialog = Adw.MessageDialog.new()

        dialog.set_heading(heading=title)
        dialog.set_body(body=error)
        dialog.add_response(Gtk.ResponseType.CANCEL.value_nick, globalDelete)
        dialog.set_response_appearance(
            response=Gtk.ResponseType.CANCEL.value_nick,
            appearance=Adw.ResponseAppearance.DESTRUCTIVE
        )
        dialog.add_response(Gtk.ResponseType.OK.value_nick, okButton)
        dialog.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )
        dialog.connect('response', dialog_response, appdir)

        dialog.present()

def dialog_response(self, response, appdir):
            if response == Gtk.ResponseType.OK.value_nick:
                None
            elif response == Gtk.ResponseType.CANCEL.value_nick:
                shutil.rmtree(appdir)