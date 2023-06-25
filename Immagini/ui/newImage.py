import sys
from ..imageCreator import startCreatingImage
import shutil
from .error import *
import gi
import threading
import pathlib
import json
from ..convertFlatpak import startConvertingFlatpak
from .uiElements import *
from ..ui.strings import *
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Adw, Gio

AdvancedInfo = Adw.PreferencesGroup.new()
outputRow = Adw.PreferencesGroup.new()
isOutputActive = False
settings = Gio.Settings.new("dev.salaniLeo.immagini")
page = None
dependeciesSwitches = []

class newImageBox(Gtk.Box):
    def __init__(self, mainWindow, application, **kwargs):
        super().__init__(**kwargs)
        global page
        page = mainWindow

        mainBox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        stack = Gtk.Stack()
        stack.add_titled(child=self.createNew(mainWindow, application), name=createNewOne, title=createNewOne)
        stack.add_titled(child=convertFlatpak(mainWindow, application), name=convertFromFlatpak, title=convertFromFlatpak)

        stack.set_transition_type(
            transition=Gtk.StackTransitionType.CROSSFADE
        )
        stack_sidebar = Gtk.StackSidebar.new()
        stack_sidebar.set_stack(stack=stack)
        # stack_sidebar.connect('clicked', self.test)
        
        mainBox.append(stack_sidebar)
        mainBox.append(stack)
        self.append(mainBox)
        
    def createNew(self, mainWindow, application):
        global AdvancedInfo
        global outputRow
        
        mainBox = Adw.PreferencesPage.new()

        self.entryNum = 0

        self.bottomBox = Gtk.Box()
        self.bottomBox.set_vexpand(True)

        mainBox.set_vexpand(True)

        AdvancedInfo = Adw.PreferencesGroup.new()
        AdvancedInfo.set_title("Advanced")

        self.addInfo = Adw.PreferencesGroup.new()
        self.addInfo.set_title("New")

        self.nameEntry = self.newEntryRow(globalName, False, globalName,False, False)
        self.exeEntry = self.newEntryRow(globalExecutable,True,globalExecutable,False, True)
        self.iconEntry = self.newEntryRow(globalIcon, True, globalIcon, False, True)
        self.categoriesEntry = self.newEntryRow(globalCategory,False,globalCategory,False, False)
        self.typeEntry = self.newEntryRow(globalType,False,globalType,False, False)

        self.includeLibraries = self.newAdvancedList(includeLibrariesTitle, includeLibrariesSubtitle)
        self.parentFolder = self.newAdvancedRow(useFolderModeTitle, useFolderModeSubtitle, True, True, True)
        self.customARLoc = self.newAdvancedRow(useCustomAppRunTitle, useCustomAppRunSubtitle,True, False, True)
        self.includeInterpreter = self.newInterpreterSelector(includeDependeciesTitle, installedIntepreters, selectManually)
        self.createTemplateImage = self.newTemplateRow(createTemplateImage)

        AdvancedInfo.add(self.parentFolder)
        AdvancedInfo.add(self.customARLoc)
        AdvancedInfo.add(self.includeLibraries)
        AdvancedInfo.add(self.includeInterpreter)
        AdvancedInfo.add(self.createTemplateImage)
        AdvancedInfo.set_visible(False)

        self.addInfo.add(self.nameEntry)
        self.addInfo.add(self.exeEntry)
        self.addInfo.add(self.iconEntry)
        self.addInfo.add(self.categoriesEntry)
        self.addInfo.add(self.typeEntry)
        self.addInfo.set_hexpand(True)

        self.okButton = Gtk.Button(label=globalConfirm)
        self.okButton.set_size_request(80, -1)
        self.okButton.set_hexpand(True)
        self.okButton.set_halign(Gtk.Align.CENTER)
        self.okButton.set_valign(Gtk.Align.CENTER)
        self.okButton.set_margin_bottom(6)
        self.okButton.set_margin_top(6)
        self.okButton.connect('clicked', newImageBox.initCreation, application.refresh, page)
    
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

        self.outputEntry = self.newEntryRow(outputLocationTitle,True,outputLocationSubtitle,True, True)
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
            
        return mainBox

    def showAdvanced(widget, active):
        if active is True:
            AdvancedInfo.set_visible(True)
        else:
            AdvancedInfo.set_visible(False)
            
    def sameOutput(active):
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

            button = browseButton(fileChooser, selectLibrariesTitle, False, nameLabel, page)
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
            adw_expander_row.set_title(title=includeLibrariesTitle)

            box.add(adw_expander_row)

            global advancedRow
            advancedRow.append(nameLabel)
            
            global advancedSwitch
            advancedSwitch.append(switch)

            return adw_expander_row

    def newInterpreterSelector(self, title, sysInterp, browseInterp):
                global advancedRow, dependeciesSwitches

                adw_expander_row = Adw.ExpanderRow.new()

                selItemsLabel = Gtk.Label()

                switch = Gtk.Switch()
                switch.set_valign(Gtk.Align.CENTER)
                switch.set_halign(Gtk.Align.END)

                javaSwitch = Gtk.Switch()
                pySwitch = Gtk.Switch()

                titleLabel = Gtk.Label()
                titleLabel.set_halign(Gtk.Align.START)
                titleLabel.set_valign(Gtk.Align.CENTER)
                titleLabel.set_text(sysInterp)

                sysInterpretersBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
                sysInterpretersBox.set_halign(Gtk.Align.START)
                sysInterpretersBox.set_valign(Gtk.Align.CENTER)

                if 'python' in os.listdir('/usr/bin'):
                    pyBox = Gtk.Box(spacing=6)
                    pyLabel = Gtk.Label()
                    pyVersion = os.popen('/usr/bin/python --version').read()

                    pySwitch.set_valign(Gtk.Align.CENTER)
                    # pyCheck.connect('state-set', self.enableOption, None, pyCheck)

                    pyLabel.set_valign(Gtk.Align.CENTER)
                    pyLabel.set_label(str(pyVersion).split('\n')[0])

                    pyBox.append(pySwitch)
                    pyBox.append(pyLabel)

                    sysInterpretersBox.append(pyBox)

                if 'java' in os.listdir('/usr/bin'):
                    javaBox = Gtk.Box(spacing=6)
                    javaLabel = Gtk.Label()
                    javaVersion = os.popen('/usr/bin/java --version').read()

                    javaSwitch.set_valign(Gtk.Align.CENTER)
                    # javaCheck.connect('state-set', self.enableOption, None, pyCheck)

                    javaLabel.set_valign(Gtk.Align.CENTER)
                    javaLabel.set_label(str(javaVersion).split('\n')[0])

                    javaBox.append(javaSwitch)
                    javaBox.append(javaLabel)
                    
                    sysInterpretersBox.append(javaBox)


                fileBox = Gtk.Box()
                fileLabel = Gtk.Label(label=selectFiles)
                fileLabel.set_size_request(110, -1)
                fileLabel.set_xalign(0)

                fileButton = browseButton(fileChooser, sysInterp, False, selItemsLabel, page)
                fileButton.set_valign(Gtk.Align.CENTER)

                fileBox.append(fileLabel)
                fileBox.append(fileButton)


                folderBox = Gtk.Box()
                folderLabel = Gtk.Label(label=selectFolders)
                folderLabel.set_size_request(110, -1)
                folderLabel.set_xalign(0)

                folderButton = browseButton(fileChooser, sysInterp, True, selItemsLabel, page)
                folderButton.set_valign(Gtk.Align.CENTER)
                
                folderBox.append(folderLabel)
                folderBox.append(folderButton)

                browseLabel = Gtk.Label()
                browseLabel.set_margin_top(6)
                browseLabel.set_markup(browseInterp)
                browseLabel.set_halign(Gtk.Align.START)
                browseLabel.set_valign(Gtk.Align.CENTER)

                selectedFileView = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                selectedFileView.append(Gtk.Label(label=selectedItems))
                selectedFileView.set_margin_top(6)
                selectedFileView.append(selItemsLabel)
                selectedFileView.set_halign(Gtk.Align.START)

                leftBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
                leftBox.set_hexpand(True)
                leftBox.set_margin_start(12)
                leftBox.append(titleLabel)
                leftBox.append(sysInterpretersBox)
                leftBox.append(browseLabel)
                leftBox.append(fileBox)
                leftBox.append(folderBox)
                leftBox.append(selectedFileView)

                expandableLayout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
                expandableLayout.append(leftBox)

                box = Adw.PreferencesGroup.new()

                adw_expander_row.add_row(child=expandableLayout)
                adw_expander_row.set_title(title)

                box.add(adw_expander_row)

                advancedRow.append(titleLabel)
                
                dependeciesSwitches.append(pySwitch)
                dependeciesSwitches.append(javaSwitch)
                
                return adw_expander_row

    def newTemplateRow(self, text):

        button = Gtk.Button(label=text)
        button.set_size_request(120, -1)
        button.set_hexpand(True)
        button.set_halign(Gtk.Align.CENTER)
        button.set_margin_bottom(6)
        button.set_margin_top(6)
        button.connect('clicked', self.fillTemplateInfo)

        row = Adw.ActionRow.new()
        row.set_child(button)

        return row

    def fillTemplateInfo(self, button):
        nameEntry = normalRow[0]
        exeEntry = normalRow[1]
        iconEntry = normalRow[2]
        typeEntry = normalRow[3]
        categoryEntry = normalRow[4]

        if flatpak:
            tPath = "/app/bin/Immagini/ui/"
            iPath = '/app/share/icons/hicolor/scalable/apps/'
        else:
            tPath = "Immagini/ui/"
            iPath = 'share/icons/hicolor/scalable/apps/'

        nameEntry.set_text(globalTemplate)
        exeEntry.set_text(tPath + 'template.py')
        iconEntry.set_text(iPath + 'dev.salaniLeo.immagini.svg')
        typeEntry.set_text(globalApplication)
        categoryEntry.set_text(globalUtility)

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
        
            if "~" in libraryPath:
                libraryPath = libraryPath.replace("~", str(pathlib.Path.home()))
            
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

            pythonSwitch = dependeciesSwitches[0]
            javaSwitch = dependeciesSwitches[1]

            if None or "" in (nameText,exeText,iconText,typeText,categoryText,outputText):

                throwError(self, pleaseFillInAllInfoSubtitle, pleaseFillInAllInfoTitle, mainWindow, currentThread)

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
                    
                if(pythonSwitch.get_active()):
                    includePython = True
                else:
                    includePython = False
                    
                if(javaSwitch.get_active()):
                    includeJava = True
                else:
                    includeJava = False
                    
                includeInterpreters = []
                includeInterpreters.append(includePython)
                includeInterpreters.append(includeJava)

                if os.path.exists(iconText) and os.path.exists(exeText):
                    
                    AppDir = outputText + "/" + folderName
                    
                    if os.path.exists(AppDir):
                        folderExistsError(None, folderName + folderAlreadyExistsSubtitle, folderAlreadyExistsTitle, mainWindow, AppDir)
                    else:
                        startCreatingImage(

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
                            includeInterpreters,
                            flatpak,
                            self,
                            mainWindow

                        )

                elif not os.path.exists(exeText):
                    throwError(None, exeText + ' ' + invalidExeTitle, invalidExeSubtitle, mainWindow)

                elif not os.path.exists(iconText):
                    throwError(None, iconText + ' ' + invalidIconTitle, invalidIconSubtitle, mainWindow)

                if removeappdir:
                    try:
                        shutil.rmtree(outputText + "/" + nameText + ".AppDir")
                    except:
                        None 

                refresh(None, None, None)


    def getFlatpak(isFlatpak):
        global flatpak
        flatpak = isFlatpak

class convertFlatpak(Gtk.Box):
    def __init__(self, mainWindow, application, **kwargs):
        super().__init__(**kwargs)
        self.mainBox = Gtk.Box()
        self.stack = Gtk.Stack()
        self.applications = []
        self.flatpakLocation = f'{pathlib.Path.home()}/.var/flatpak/app'

        self.scrolled_window = Gtk.ScrolledWindow.new()
        self.scrolled_window.set_vexpand(True)
        self.scrolled_window.set_hexpand(True)
        self.stack.add_child(self.scrolled_window)
        self.stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )
        self.mainBox.append(self.stack)

        self.installedFlatpaks = Gtk.Label()
        self.installedFlatpaks.set_markup(f'<span size="larger"><b>{installedFlatpaks}</b></span>')
        self.installedFlatpaks.set_halign(Gtk.Align.START)

        self.flowbox = Gtk.FlowBox.new()
        self.flowbox.set_margin_top(margin=12)
        self.flowbox.set_margin_end(margin=12)
        self.flowbox.set_margin_bottom(margin=12)
        self.flowbox.set_margin_start(margin=12)
        self.flowbox.set_valign(align=Gtk.Align.START)
        self.flowbox.set_max_children_per_line(n_children=5)
        self.flowbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        self.flowbox.insert(self.installedFlatpaks, 0)
        self.scrolled_window.set_child(child=self.flowbox)

        n = 1
        for app in os.listdir(self.flatpakLocation):
            self.applications.append(app)
            self.button = Gtk.Button.new_with_label(label=f'{app}')
            self.button.connect('clicked', self.createFromFlatpakPage, n-1)
            self.flowbox.insert(widget=self.button, position=n)
            n = n + 1
            
        self.append(self.mainBox)

    
    def createFromFlatpakPage(self, button, appNumber):
        self.imageLoc = settings.get_string('librarypath')
        self.appId = self.applications[appNumber]
        self.appName = self.appId.split('.')[-1]
        self.currentLocation = f'{self.flatpakLocation}/{self.appId}'
        self.filesLoc = f'/current/active/files'
        self.sharedLoc = f'{self.appId}/current/active/export'
        self.jsonLoc = f'{self.currentLocation}{self.filesLoc}/manifest.json'
        self.flatpak = flatpak
        self.page = page
        
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        topBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        centerBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        bottomBox = Gtk.Box()
        flatpakInfoBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        infoLabel = Gtk.Label()
        nameLabel = Gtk.Label()
        binaryLabel = Gtk.Label()
        iconLabel = Gtk.Label()
        desktopLabel = Gtk.Label()
        shareLabel = Gtk.Label()
        libLabel = Gtk.Label()
        convertButton = Gtk.Button()

        self.readFlatpakManifest()
        self.findIconLoc()
        self.getApplicationFolders()

        self.binaryName = f'{self.appId}{self.filesLoc}/bin/{self.command}'
        self.iconName = f'{self.iconDir}{self.icon}'

        page.set_title(self.appId)

        self.backButton = Gtk.Button.new_from_icon_name("pan-start-symbolic") 
        self.backButton.connect("clicked", self.goBack)

        topBox.append(self.backButton)

        self.stack.add_child(mainBox)
        self.stack.set_visible_child(mainBox)

        infoLabel.set_markup(f'<span size="larger"><b>{globalInfo}:</b></span>')
        infoLabel.set_margin_bottom(12)
        infoLabel.set_halign(Gtk.Align.START)

        nameLabel.set_markup(f'<b>{globalName}:</b> {self.appName}')
        nameLabel.set_halign(Gtk.Align.START)

        binaryLabel.set_markup(f'<b>{globalExecutable}:</b> {self.binaryName}')
        binaryLabel.set_halign(Gtk.Align.START)
        binaryLabel.set_wrap(True)

        iconLabel.set_markup(f'<b>{globalIcon}:</b> {self.iconName}')
        iconLabel.set_halign(Gtk.Align.START)
        iconLabel.set_wrap(True)

        desktopLabel.set_markup(f'<b>{globalDesktop}:</b> {self.desktopFileLoc}')
        desktopLabel.set_halign(Gtk.Align.START)
        desktopLabel.set_wrap(True)

        shareLabel.set_markup(f'<b>{globalShare}:</b> {self.shareLoc}')
        shareLabel.set_size_request(100,-1)
        shareLabel.set_halign(Gtk.Align.START)
        shareLabel.set_wrap(True)

        libLabel.set_markup(f'<b>{globalLib}:</b> {self.libLoc}')
        libLabel.set_halign(Gtk.Align.START)
        libLabel.set_wrap(True)

        convertButton.connect('clicked', self.startConverting)
        convertButton.set_label(convertButtonLabel)
        convertButton.set_margin_top(12)
        convertButton.set_size_request(150, -1)
        convertButton.set_hexpand(False)

        flatpakInfoBox.append(infoLabel)
        flatpakInfoBox.append(nameLabel)
        flatpakInfoBox.append(binaryLabel)
        flatpakInfoBox.append(iconLabel)
        flatpakInfoBox.append(desktopLabel)
        flatpakInfoBox.append(shareLabel)
        flatpakInfoBox.append(libLabel)
        flatpakInfoBox.set_halign(Gtk.Align.START)
        flatpakInfoBox.set_hexpand(True)
        flatpakInfoBox.set_margin_top(12)
        flatpakInfoBox.set_margin_bottom(12)
        flatpakInfoBox.set_margin_end(12)

        centerBox.set_margin_top(12)
        centerBox.set_margin_bottom(12)
        centerBox.append(flatpakInfoBox)
        centerBox.set_halign(Gtk.Align.START)

        bottomBox.append(convertButton)

        mainBox.append(topBox)
        mainBox.append(centerBox)
        mainBox.append(bottomBox)
    
    def readFlatpakManifest(self):
        with open(self.jsonLoc, 'r') as f:
            d = json.load(f)
        try:
            self.command = d['command']
        except:
            maybeBinary = f'{self.currentLocation}{self.filesLoc}/bin/{self.appName}'
            if os.path.exists(maybeBinary):
                self.command = f'{maybeBinary} ({executableNotProvidedByManifest})'
            else:
                self.command = f'{executableNotFoundInsideFlatpak}'
        
            
    def findIconLoc(self):
        iconDir = f'{self.currentLocation}{self.filesLoc}/share/icons/hicolor'
        icon128x128Dir = f'{iconDir}/128x128'
        iconSvgDir = f'{iconDir}/scalable'

        self.icon = "Can't find an icon"
        if os.path.exists(icon128x128Dir):
            self.iconDir = f'{self.appId}{self.filesLoc}/share/icons/hicolor/128x128/apps/'
            self.icon = f'{self.appId}.png'
        elif os.path.exists(iconSvgDir):
            self.iconDir = f'{self.appId}{self.filesLoc}/share/icons/hicolor/scalable/apps/'
            self.icon = f'{self.appId}.svg'


    def getApplicationFolders(self):
        self.binLoc = f'{self.appId}{self.filesLoc}/bin'
        self.shareLoc = f'{self.appId}{self.filesLoc}/share'
        self.libLoc = f'{self.appId}{self.filesLoc}/lib'
        self.desktopFileLoc = f'{self.sharedLoc}/share/applications/{self.appId}.desktop'

    def goBack(self, button):
        self.stack.set_visible_child(self.scrolled_window)
        page.set_title(globalNewImageTitle)

    def startConverting(self, button):

        libraryPath = settings.get_string("librarypath")
        if "~" in libraryPath:
            libraryPath = libraryPath.replace("~", str(pathlib.Path.home()))

        startConvertingFlatpak(page, libraryPath, self.appId, f'{self.flatpakLocation}/{self.desktopFileLoc}', self)


flatpak = None
normalRow = []
advancedRow = []
advancedSwitch = []