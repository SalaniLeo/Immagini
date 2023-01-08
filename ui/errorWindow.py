import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

def error_message(msg, parent=None, title=None):

    dialog = Gtk.MessageDialog(parent= None, message_format = msg)
    dialog.add_buttons("Close", Gtk.ResponseType.CLOSE)
    if parent is not None:        
        dialog.set_transient_for(parent)
    if title is not None:
        dialog.set_title(title)
    else:
        dialog.set_title('')
    dialog.show()
    dialog.run()
    dialog.destroy()
    return None 

#     builder = Gtk.Builder()
#     builder.add_from_file("ui/errorWindow.glade")
#     builder.connect_signals(Handler())

#     errorWindow = builder.get_object("errorWindow")
#     errorWindow.set_property("secondary_text", msg)


# class Handler():
#         def closeWindow(self, button):
#             # Gtk.main_quit()
#             None