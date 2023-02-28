import gi
import os

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk


class pathEntry(Gtk.Entry):

    def __init__(self, placeholder,  **kwargs):
        super().__init__(**kwargs)   

        self.set_valign(align=Gtk.Align.CENTER)
        self.set_placeholder_text(placeholder)
        self.connect('changed', checkExists, pathEntry)



class fileChooser():
    def __init__(self, button , title, folderMode, entry, mainWindow,  **kwargs):
        super().__init__(**kwargs)   
        
        self.dialog = Gtk.FileChooserNative.new(title=title,parent=None,action=Gtk.FileChooserAction.OPEN)
        self.dialog.set_transient_for(mainWindow)
        self.dialog.set_modal(True)
        if title == 'Select libraries':
            self.dialog.set_select_multiple(True)

        if folderMode:
                self.dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)

        self.dialog.show()
        self.dialog.set_title(title)
        self.dialog.connect("response", self.fileCResponse, entry, self.dialog.get_select_multiple())


    def fileCResponse(self, dialog, window, entry, multiple):
        if multiple:
            files_model = dialog.get_files()
            filenames = [file.get_path() for file in files_model]
            rawName = str(filenames)
            finName = rawName.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n")
            entry.set_text(finName)
        else:
            self.dialog.destroy()
            entry.set_text(dialog.get_file().get_path())



def checkExists(entry, key):
    global changedPath
    if os.path.exists(entry.get_text()):
        setRowState(entry, 'default')
    else:
        setRowState(entry, 'error')

    if entry.get_text() == "":
        setRowState(entry, 'default')

def setRowState(widget, mode):

        if mode == 'default':
            widget.get_style_context().remove_class(class_name='error')

        widget.get_style_context().add_class(class_name=mode)

def browseButton(fileChooser, name, folderMode, entry, page):

    button = Gtk.Button.new_from_icon_name("document-open-symbolic") 
    button.set_valign(Gtk.Align.CENTER)
    button.connect('clicked', fileChooser, name, folderMode, entry, page)

    return button