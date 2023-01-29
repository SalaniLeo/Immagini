
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def throwError(self, error, title):
                 
        dialog = Gtk.MessageDialog(
                parent         = self,
                message_type   = Gtk.MessageType.ERROR,
                secondary_text = error,
                text           = title,
                buttons        = Gtk.ButtonsType.CLOSE,
        )
                
        dialog.show()