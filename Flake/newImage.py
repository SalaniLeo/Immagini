import sys
from .imageCreator import start
import shutil
from .creator.error import *
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Adw, Gio, Gdk, GLib

mainBox = Adw.PreferencesPage.new()
AdvancedInfo = Adw.PreferencesGroup.new()

class newImageBox(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global mainBox
        global AdvancedInfo
        #main box in the middle

        self.container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.bottomBox = Gtk.Box()
        self.bottomBox.set_vexpand(True)

        mainBox.set_vexpand(True)
        self.container.append(mainBox)
        self.append(self.container)

        AdvancedInfo = Adw.PreferencesGroup.new()
        AdvancedInfo.set_title("Advanced")

        self.addInfo = Adw.PreferencesGroup.new()
        self.addInfo.set_title("New")
        mainBox.add(group=self.addInfo)

        self.nameEntry = self.newEntryRow("Name", False,"Name of the AppImage")
        self.exeEntry = self.newEntryRow("Executable",True,"Executable file to package")
        self.iconEntry = self.newEntryRow("Icon", True,"Icon of the app")
        self.categoriesEntry = self.newEntryRow("Category",False,"Category to specify in desktop file")
        self.typeEntry = self.newEntryRow("Type",False,"Type to specify in desktop file")

        self.parentFolder = self.newAdvancedRow("Enable folder mode")
        self.customARLoc = self.newAdvancedRow("Enable custom apprun")
        AdvancedInfo.add(self.parentFolder)
        AdvancedInfo.add(self.customARLoc)


        self.addInfo.add(self.nameEntry)
        self.addInfo.add(self.exeEntry)
        self.addInfo.add(self.iconEntry)
        self.addInfo.add(self.categoriesEntry)
        self.addInfo.add(self.typeEntry)
        self.addInfo.set_hexpand(True)

        self.okButton = Gtk.Button(label="confirm")
        self.okButton.set_size_request(80, -1)
        self.okButton.set_halign(Gtk.Align.CENTER)
        self.okButton.set_valign(Gtk.Align.CENTER)
        self.okButton.connect("clicked", self.confirm)
        self.okButton.set_margin_bottom(6)
        self.okButton.set_margin_top(6)

        self.container.append(self.okButton)
        self.container.append(self.bottomBox)


    def showAdvanced(widget, active):
        global mainBox
        if active is True:
            mainBox.add(AdvancedInfo)
        else:
            mainBox.remove(AdvancedInfo)

    def newEntryRow(self, name, buttonNeeded,placeholder):

        button = Gtk.Button.new_from_icon_name("document-open-symbolic") 
        button.set_valign(Gtk.Align.CENTER)

        width = 500

        label = Gtk.Label(label=name)
        entry = Gtk.Entry()
        # entry.set_hexpand(True)
        entry.set_valign(Gtk.Align.CENTER)
        entry.set_placeholder_text(placeholder)
        if name == "Enable folder mode":
            entry.set_placeholder_text("Parent folder location")
        elif name == "Enable custom apprun":
            entry.set_placeholder_text("Custom AppRun location")
        
        row = Adw.ActionRow.new()
        entry.set_size_request(width,-1)
        row.add_suffix(entry)
        row.add_prefix(label)
        if buttonNeeded:
            entry.set_size_request(width-40,-1)
            row.add_suffix(button)

        # button.connect('state-set', self.enableOption, entry)

        return row

    def newAdvancedRow(self, name):

        switch = Gtk.Switch()
        switch.set_valign(Gtk.Align.CENTER)

        label = Gtk.Label(label=name)
        entry = Gtk.Entry()
        entry.set_valign(Gtk.Align.CENTER)
        entry.get_style_context().add_class(class_name='error')
        entry.set_editable(False)
        entry.set_size_request(180,-1)
        if name == "Enable folder mode":
            entry.set_placeholder_text("Parent folder location")
        elif name == "Enable custom apprun":
            entry.set_placeholder_text("Custom AppRun location")

        # box.set_hexpand(True)
        # box.set_vexpand(True)
        
        row = Adw.ActionRow.new()
        row.add_suffix(switch)
        row.add_suffix(entry)
        row.add_prefix(label)

        switch.connect('state-set', self.enableOption, entry)

        return row

    def enableOption(self, switch, state, opt):
        if state == True:
            opt.get_style_context().remove_class(class_name='error')
            opt.set_editable(True)
        elif state == False:
            opt.get_style_context().add_class(class_name='error')
            opt.set_editable(False)

# saves and switches page for the main window
    def confirm(self, button):

        # if none or "" start building the app
        if None or "" not in (self.nameEntry.get_text(),
                              self.exeEntry.get_text(),
                              self.iconEntry.get_text(),
                              self.typeEntry.get_text(),
                              self.categoriesEntry.get_text()):
            

            
            if(self.folderMSwitch.get_active()):
                
                self.secondPPFolderLabel.set_visible(True)    
                self.secondPPFolderEntry.set_visible(True)  
                self.secondPPFolderBrowse.set_visible(True)  

            else:
                
                self.secondPPFolderLabel.set_visible(False)    
                self.secondPPFolderEntry.set_visible(False)  
                self.secondPPFolderBrowse.set_visible(False)  
                
            if(self.customARSwitch.get_active()):
                
                self.secondPARFileLabel.set_visible(True)    
                self.secondPARFileEntry.set_visible(True)  
                self.secondPARFileBrowse.set_visible(True)  
            else:
                self.secondPARFileLabel.set_visible(False)    
                self.secondPARFileEntry.set_visible(False)  
                self.secondPARFileBrowse.set_visible(False)  
        else:
            
            throwError(self, "Please fill in all the informations", "All the info are required")


# opens popup window for exe selection
    def chooseExe(self, button):
        fileChooser(self, "Choose executable file", self.exeEntry, folderMode=False)

# opens popup window for icon selection
    def chooseIcon(self, button):
        fileChooser(self, "Choose icon", self.iconEntry, folderMode=False)

    def chooseOutputLoc(self, button):
        fileChooser(self, "Choose output location", self.outputFEntry, folderMode=True)
        
    def chooseAppParentFolder(self, button):
        fileChooser(self, "Choose application parent folder", self.secondPPFolderEntry, folderMode=True)
        
    def chooseAppRunLoc(self, button):
        fileChooser(self, "Choose custom apprun file", self.secondPARFileEntry, folderMode=False)

    
    def fileCResponse(self, dialog, response, type, folderMode):

            self.dialog.destroy()
            self.file = dialog.get_file()
            type.set_text(self.file.get_path())


    def startCreating(self, button):
        
        if(self.outputFEntry.get_text() == "" or None):
            
            throwError(self, "An output location is required", "Output location not set")
            
        else:
            
            tb = self.outputConsole.get_buffer()
            self.expander.set_expanded(True)
            end_iter = tb.get_end_iter()
            tb.insert(end_iter, start(
                
                self.nameEntry.get_text(),
                self.exeEntry.get_text(),
                self.iconEntry.get_text(),
                self.typeEntry.get_text(),
                self.categoriesEntry.get_text(),
                self.outputFEntry.get_text(),
                self.customARSwitch.get_active(),
                self.secondPARFileEntry.get_text(),
                self.folderMSwitch.get_active(),
                self.secondPPFolderEntry.get_text(),
                self
                
                )) 
            
        # outputConsole.set_hexpand(True)
            if(self.removeAppDir.get_active()):
                shutil.rmtree(self.outputFEntry.get_text() + "/" + self.nameEntry.get_text() + ".AppDir/")


def fileChooser(self,title,type, folderMode):
    
        self.dialog = Gtk.FileChooserNative.new(title=title,
                                                parent=self, 
                                                action=Gtk.FileChooserAction.OPEN)

        if folderMode:
            self.dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
        
        self.dialog.show()
        self.dialog.set_title(title)
        self.dialog.connect("response", self.fileCResponse, type, folderMode)