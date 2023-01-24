
import gi
import shutil
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def throwError(self, error, title):
        
        # parent = Gtk.ApplicatioWindow()
        
        
        dialog = Gtk.MessageDialog(
                parent         = self,
                message_type   = Gtk.MessageType.ERROR,
                secondary_text = error,
                text           = title,
                buttons        = Gtk.ButtonsType.CLOSE,
        )
        
        dialog.show()
        # outputConsole.set_hexpand(True)
        return None