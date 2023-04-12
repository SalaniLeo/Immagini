import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

def throwError(self, error, title, mainWindow, thread = None):
                 
        dialog = Adw.MessageDialog.new()

        dialog.set_transient_for(mainWindow)
        dialog.set_modal(True)
        
        dialog.set_heading(heading=title)
        dialog.set_body(body=error)
        dialog.add_response(Gtk.ResponseType.OK.value_nick, 'Ok')
        dialog.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )

        dialog.present()