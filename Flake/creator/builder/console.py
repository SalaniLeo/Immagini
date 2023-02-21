import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gtk

class console(Adw.MessageDialog):
    def __init__(self, mainWindow, console, **kwargs):
        super().__init__(**kwargs)

        self.set_default_size(500,225)
        self.set_title(title='Console')
        self.set_transient_for(mainWindow)
        self.set_modal(True)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_margin_bottom(25)
        self.scrolled.set_margin_top(25)
        self.scrolled.set_margin_end(25)
        self.scrolled.set_margin_start(25)
        self.scrolled.set_vexpand(True)


        self.closeButton = Gtk.Button(label=("Close"))
        self.closeButton.set_hexpand(True)
        self.closeButton.set_size_request(-1, 50)
        self.closeButton.connect('clicked', self.exit)

        self.box.append(self.scrolled)
        self.box.append(self.closeButton)


        self.set_child(self.box)


        self.scrolled.set_child(console)


    def exit(self, button):
        self.close()
