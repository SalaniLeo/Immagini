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

        self.entryNum = 0

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

        self.nameEntry = self.newEntryRow("Name", False, "Name")
        self.exeEntry = self.newEntryRow("Executable",True,"Executable")
        self.iconEntry = self.newEntryRow("Icon", True,"Icon")
        self.categoriesEntry = self.newEntryRow("Category",False,"Category")
        self.typeEntry = self.newEntryRow("Type",False,"Type")

        self.parentFolder = self.newAdvancedRow("Enable folder mode",True, True)
        self.customARLoc = self.newAdvancedRow("Enable custom apprun",True, False)
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
        # self.okButton.connect("clicked", self.confirm)
        # self.okButton.set_margin_bottom(6)
        self.okButton.set_margin_top(6)
        self.okButton.connect('clicked', self.createImage)

        self.container.append(self.okButton)
        self.container.append(self.bottomBox)


    def showAdvanced(widget, active):
        global mainBox
        if active is True:
            mainBox.add(AdvancedInfo)
        else:
            mainBox.remove(AdvancedInfo)

    def newEntryRow(self, name, buttonNeeded ,placeholder):

        label = Gtk.Label(label=name)
        label.set_hexpand(False)
        label.set_halign(Gtk.Align.START)
        entry = Gtk.Entry()
        entry.set_valign(Gtk.Align.CENTER)
        entry.set_halign(Gtk.Align.FILL)
        entry.set_placeholder_text(placeholder)
        entry.set_hexpand(True)

        if name == "Enable folder mode":
            entry.set_placeholder_text("Parent folder location")
        elif name == "Enable custom apprun":
            entry.set_placeholder_text("Custom AppRun location")
        
        global test
        test.append(entry)

        row = Adw.ActionRow.new()
        row.add_suffix(entry)
        row.add_prefix(label)
        if buttonNeeded:
            folderMode = not buttonNeeded
            button = Gtk.Button.new_from_icon_name("document-open-symbolic") 
            button.connect('clicked', self.fileChooser, name, folderMode, entry)
            button.set_valign(Gtk.Align.CENTER)
            row.add_suffix(button)

        return row

    def newAdvancedRow(self, name, buttonNeeded, folderMode):

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
        
        switch.connect('state-set', self.enableOption, entry)

        row = Adw.ActionRow.new()
        row.add_suffix(switch)
        row.add_suffix(entry)
        row.add_prefix(label)

        if buttonNeeded:
            button = Gtk.Button.new_from_icon_name("document-open-symbolic") 
            button.set_valign(Gtk.Align.CENTER)
            button.connect('clicked', self.fileChooser, name, folderMode, entry)
            row.add_suffix(button)

        return row

    def enableOption(self, switch, state, opt):
        if state == True:
            opt.get_style_context().remove_class(class_name='error')
            opt.set_editable(True)
        elif state == False:
            opt.get_style_context().add_class(class_name='error')
            opt.set_editable(False)


    
    def fileCResponse(self, dialog, window, entry):

            self.dialog.destroy()
            entry.set_text(dialog.get_file().get_path())


    def fileChooser(self, button , title, folderMode, entry):
        
            self.dialog = Gtk.FileChooserNative.new(title=title,
                                                    parent=None, 
                                                    action=Gtk.FileChooserAction.OPEN)

            if folderMode:
                self.dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
            
            self.dialog.show()
            self.dialog.set_title(title)
            self.dialog.connect("response", self.fileCResponse, entry)


    def createImage(self, button):

        nameText = test[0].get_text()
        exeText = test[1].get_text()
        iconText = test[2].get_text()
        typeText = test[3].get_text()
        categoryText = test[4].get_text()

        if None or "" not in (nameText,exeText,iconText,typeText,categoryText):

            
            # if(self.folderMSwitch.get_active()):
                
            # if(self.customARSwitch.get_active()):

            start(nameText,exeText,iconText,typeText,categoryText,
            
            
            )
                
            
            throwError(self, "Please fill in all the informations", "All the info are required")



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
test = []