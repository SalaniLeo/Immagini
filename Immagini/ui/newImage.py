import sys
from ..imageCreator import start
import shutil
from .error import *
import gi
import threading
from .uiElements import *
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Adw, Gio

mainBox = Adw.PreferencesPage.new()
AdvancedInfo = Adw.PreferencesGroup.new()
outputRow = Adw.PreferencesGroup.new()
isOutputActive = False
settings = Gio.Settings.new("dev.salaniLeo.immagini")
page = None


class newImageBox(Gtk.Box):
    def __init__(self, mainWindow, **kwargs):
        super().__init__(**kwargs)
        global mainBox
        global AdvancedInfo
        global outputRow
        global page

        page = mainWindow

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

        self.nameEntry = self.newEntryRow("Name", False, "Name",False, False)
        self.exeEntry = self.newEntryRow("Executable",True,"Executable",False, True)
        self.iconEntry = self.newEntryRow("Icon", True, "Icon", False, True)
        self.categoriesEntry = self.newEntryRow("Category",False,"Category",False, False)
        self.typeEntry = self.newEntryRow("Type",False,"Type",False, False)

        self.includeLibraries = self.newAdvancedList("Include libraries", 'Select a library to include inside an AppImage')
        self.parentFolder = self.newAdvancedRow("Folder mode", "Parent folder location", True, True, True)
        self.customARLoc = self.newAdvancedRow("Custom apprun", "Custom AppRun location",True, False, True)

        AdvancedInfo.add(self.parentFolder)
        AdvancedInfo.add(self.customARLoc)
        AdvancedInfo.add(self.includeLibraries)
        AdvancedInfo.set_visible(False)

        self.addInfo.add(self.nameEntry)
        self.addInfo.add(self.exeEntry)
        self.addInfo.add(self.iconEntry)
        self.addInfo.add(self.categoriesEntry)
        self.addInfo.add(self.typeEntry)
        self.addInfo.set_hexpand(True)

        self.okButton = Gtk.Button(label="Confirm")
        self.okButton.set_size_request(80, -1)
        self.okButton.set_hexpand(True)
        self.okButton.set_halign(Gtk.Align.CENTER)
        self.okButton.set_valign(Gtk.Align.CENTER)
        self.okButton.set_margin_bottom(6)
        self.okButton.set_margin_top(6)

        mainBox.add(group=self.addInfo)

        self.uselibraryPath = settings.get_boolean("uselibrarypath")

        okPage = Adw.PreferencesGroup.new()

        okRow = Adw.ActionRow.new()
        # okRow.set_visible(False)
        okRow.set_child(self.okButton)
        
        okPage.add(okRow)

        mainBox.add(outputRow)
        mainBox.add(okPage)
        mainBox.add(AdvancedInfo)

        self.outputEntry = self.newEntryRow("Location",True,"App location",True, True)
        outputRow.add(self.outputEntry)

        global isOutputActive

        if not self.uselibraryPath:
            isOutputActive = True
            outputRow.set_visible(True)
        else:
            isOutputActive = False
            outputRow.set_visible(False)

        autoFolderMode = settings.get_boolean("foldermode")
        autoCustomAppRun = settings.get_boolean("customapprun")

        if autoFolderMode:

            advancedSwitch[1].set_active(True)

        if autoCustomAppRun:

            advancedSwitch[0].set_active(True)

    def showAdvanced(widget, active):
        global mainBox
        if active is True:
            AdvancedInfo.set_visible(True)
        else:
            AdvancedInfo.set_visible(False)
            
    def sameOutput(active):
        global mainBox
        global outputRow
        global isOutputActive

        if not active:
            if not isOutputActive:
                isOutputActive = True
                outputRow.set_visible(True)
        else:
            if isOutputActive:
                isOutputActive = False
                outputRow.set_visible(False)

    def newEntryRow(self, name, buttonNeeded, placeholder, folderMode, path):

        if path:
            entry = pathEntry(placeholder)
        else:
            entry = Gtk.Entry()

        label = Gtk.Label(label=name)
        label.set_hexpand(False)
        label.set_xalign(0.0)
        label.set_size_request(65,-1)
        label.set_halign(Gtk.Align.START)

        entry.set_valign(Gtk.Align.CENTER)
        entry.set_halign(Gtk.Align.FILL)
        entry.set_placeholder_text(placeholder)
        entry.set_hexpand(True)
        
        global normalRow
        normalRow.append(entry)

        row = Adw.ActionRow.new()
        row.add_suffix(entry)
        row.add_prefix(label)
        if buttonNeeded:
                row.add_suffix(browseButton(fileChooser, name, folderMode, entry, page))

        return row

    def newAdvancedRow(self, name, placeholder, buttonNeeded, folderMode, path):

        switch = Gtk.Switch()
        switch.set_valign(Gtk.Align.CENTER)

        label = Gtk.Label(label=name)

        if path:
                entry = pathEntry(placeholder)
        else:
                entry = Gtk.Entry()

        entry.set_valign(Gtk.Align.CENTER)
        entry.get_style_context().add_class(class_name='error')
        entry.set_editable(False)
        entry.set_size_request(180,-1)

        button = browseButton(fileChooser, name, folderMode, entry, page)
        button.set_sensitive(False)

        switch.connect('state-set', self.enableOption, entry, button)

        row = Adw.ActionRow.new()
        row.add_suffix(switch)
        row.add_suffix(entry)
        row.add_prefix(label)
        row.add_suffix(button)

        global advancedRow
        advancedRow.append(entry)
        
        global advancedSwitch
        advancedSwitch.append(switch)

        return row

    def newAdvancedList(self, name, placeholder):

            adw_expander_row = Adw.ExpanderRow.new()

            switch = Gtk.Switch()
            switch.set_valign(Gtk.Align.CENTER)
            switch.set_halign(Gtk.Align.END)

            nameLabel = Gtk.Label()
            nameLabel.set_halign(Gtk.Align.START)
            nameLabel.set_valign(Gtk.Align.CENTER)
            nameLabel.set_margin_start(12)
            nameLabel.set_margin_top(12)
            nameLabel.set_margin_bottom(12)
            nameLabel.set_text(placeholder)

            button = browseButton(fileChooser, 'Select libraries', False, nameLabel, page)
            button.set_valign(Gtk.Align.CENTER)
            button.set_margin_bottom(12)
            button.set_margin_top(12)
            button.set_margin_end(12)
            button.set_margin_start(12)
            button.set_sensitive(False)

            switch.connect('state-set', self.enableOption, None, button)


            rightBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            rightBox.append(switch)
            rightBox.append(button)

            leftBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            leftBox.set_hexpand(True)

            leftBox.append(nameLabel)

            expandableLayout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            expandableLayout.append(leftBox)
            expandableLayout.append(rightBox)
            expandableLayout.set_size_request(-1, -1)

            box = Adw.PreferencesGroup.new()

            adw_expander_row.add_row(child=expandableLayout)
            adw_expander_row.set_title(title='Include libraries')

            box.add(adw_expander_row)

            global advancedRow
            advancedRow.append(nameLabel)
            
            global advancedSwitch
            advancedSwitch.append(switch)

            return adw_expander_row

    def enableOption(self, switch, state, row, button):
        if state == True:
            if row != None:
                row.get_style_context().remove_class(class_name='error')
                row.set_editable(True)
            button.set_sensitive(True)
        elif state == False:
            if row != None:
                row.get_style_context().add_class(class_name='error')
                row.set_editable(False)
            button.set_sensitive(False)


    def initCreation(self, refresh, mainWindow):
        createThread = threading.Thread(target=newImageBox.createImage, args=(self, refresh, mainWindow), daemon=True, name='createThread')
        createThread.start()
        createThread.join()

    def createImage(self, refresh, mainWindow):
            currentThread = threading.current_thread()
            nameText = normalRow[0].get_text()
            exeText = normalRow[1].get_text()
            iconText = normalRow[2].get_text()
            typeText = normalRow[3].get_text()
            categoryText = normalRow[4].get_text()

            libraryPath = settings.get_string("librarypath")
            uselibraryPath = settings.get_boolean("uselibrarypath")
            removeappdir = settings.get_boolean("removeappdir")

            if not uselibraryPath:
                outputText = normalRow[5].get_text()
            else:
                outputText = libraryPath

            librariesText = advancedRow[0].get_text()
            parentFolderText = advancedRow[1].get_text()
            appRunText = advancedRow[2].get_text()

            librariesSwitch = advancedSwitch[0]
            parentFolderSwitch = advancedSwitch[1]
            appRunSwitch = advancedSwitch[2]

            if None or "" in (nameText,exeText,iconText,typeText,categoryText,outputText):

                throwError(self, "Please fill in all the informations", "All the info are required", mainWindow, currentThread)

            else:

                folderName = nameText + ".AppDir"

                if(parentFolderSwitch.get_active()):
                    folderMode = True
                else:
                    folderMode = False

                if(appRunSwitch.get_active()):
                    customAppRun = True
                else:
                    customAppRun = False

                if(librariesSwitch.get_active()):
                    includeLibraries = True
                else:
                    includeLibraries = False

                if os.path.exists(iconText) and os.path.exists(exeText):

                    if os.path.exists(outputText + "/" + folderName):
                        throwError(None, 'The' + folderName + 'folder already exists', 'Folder already exists', mainWindow)
                    else:
                        start(
                            
                            nameText,
                            exeText,
                            iconText,
                            typeText,
                            categoryText,
                            outputText,
                            customAppRun,
                            appRunText,
                            folderMode,
                            parentFolderText,
                            includeLibraries,
                            librariesText,
                            flatpak,
                            self,
                            mainWindow
                            
                        )

                elif not os.path.exists(exeText):
                    throwError(None, 'Exe ' + exeText + 'does not appear to exist', 'Could not find exe', mainWindow)

                elif not os.path.exists(iconText):
                    throwError(None, 'Icon ' + iconText + 'does not appear to exist', 'Could not find icon', mainWindow)

                if removeappdir:
                        shutil.rmtree(outputText + "/" + nameText + ".AppDir")

                refresh(None, None, None)
            


    def getFlatpak(isFlatpak):
        global flatpak
        flatpak = isFlatpak


flatpak = None
normalRow = []
advancedRow = []
advancedSwitch = []