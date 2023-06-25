import gi
import os
import stat
import threading
from ..ui.console import console
from ..ui.error import throwError
from ..ui.uiElements import *
from ..ui.strings import *
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')
from gi.repository import Gtk, Adw

class manageImages(list):
    def __init__(self, list, loc): 
        menu = Gtk.Menu()
        menu_item = Gtk.MenuItem()
        menu.append(menu_item)
        menu_item.show()

    def deleteImage(button, imagePath, refresh, name, mainWindow, setRowState, row):
        manageImages.askSure(name, imagePath, refresh, mainWindow)

    def askSure(name, imagePath, refresh, mainWindow):

        dialog = Adw.MessageDialog.new()

        dialog.set_transient_for(mainWindow)
        dialog.set_modal(True)
        dialog.set_heading(heading=f'{globalDelete} {name}?')
        dialog.set_body(body=askConfirmDeleting)
        dialog.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancel')
        dialog.set_response_appearance(
            response=Gtk.ResponseType.CANCEL.value_nick,
            appearance=Adw.ResponseAppearance.DESTRUCTIVE
        )
        dialog.add_response(Gtk.ResponseType.OK.value_nick, 'Ok')
        dialog.set_response_appearance(
            response=Gtk.ResponseType.OK.value_nick,
            appearance=Adw.ResponseAppearance.SUGGESTED
        )
        dialog.connect('response', manageImages.dialog_response, imagePath, refresh)

        dialog.present()

    def dialog_response(dialog, response, imagePath, refresh):
        if response == Gtk.ResponseType.OK.value_nick:
            os.remove(imagePath)
            refresh(None, None, None)
        elif response == Gtk.ResponseType.CANCEL.value_nick:
            None

    def imageOptions(button, appImage, fullName, executable ,mainWindow, setRowState, row):
        options = imageOptions(mainWindow, executable, appImage, fullName, setRowState, row)
        options.show()

    def setExecutable(switch, state, appImage, setRowState, row):
        if switch.get_active():
            st = os.stat(appImage)
            os.chmod(appImage, st.st_mode | stat.S_IEXEC)
            setRowState(row, 'default')
        else:
            current = stat.S_IMODE(os.lstat(appImage).st_mode)
            os.chmod(appImage, current & ~stat.S_IEXEC)
            setRowState(row, 'error')

    def extractImage(button, imagePath, entry, mainWindow, name):
        command = "cd " + entry.get_placeholder_text() + " && " + imagePath + " --appimage-extract"

        dst = entry.get_placeholder_text() + '/' + name.get_text() + '.AppDir'

        if os.path.exists(dst):
            throwError(None, dst + folderAlreadyExistsSubtitle, folderAlreadyExistsTitle, mainWindow)
        else:
            terminal = Gtk.TextView()
            terminal.set_editable(False)

            bff = Gtk.TextBuffer()
            terminal = Gtk.TextView(buffer = bff)
            bff.set_text(extractingImage)

            iter = bff.get_end_iter()

            consolePage = console(mainWindow, terminal)
            consolePage.present()

            extractOutput = os.popen(command).read()
            bff.insert(iter, extractOutput)

            os.rename(entry.get_placeholder_text() + '/squashfs-root', dst)


    def renameImage(button, appImage, name, loc, refresh, imageName=None, imageNum=None):
        dst = loc + "/" + name.get_text() + ".AppImage"

        os.rename(appImage, dst)

        refresh(None, None, None)

    def startImage(button, appImage, startInTerminal, mainWindow, flatpak, setState, row):
        
        command = None
        
        st = os.stat(appImage)
        executable = bool(st.st_mode & stat.S_IEXEC)
        
        if not executable:
            throwError(None, noExePermissionSubtitle, noExePermissionTitle, mainWindow)
        else:
            if flatpak:
                command = 'cd ~ && ' + 'flatpak-spawn --host ' + appImage.split("/home/",1)[1].split("/",1)[1]
            else:
                command = appImage
        
            launchThread = threading.Thread(target=os.popen(command))
            launchThread.start()
        

imageNum = None
imageNames = None

class imageOptions(Adw.PreferencesWindow):

    def __init__(self, parent, refresh, appImage, fullName, setRowState, row, **kwargs):
        super().__init__(**kwargs)  

        self.set_transient_for(parent)
        self.set_modal(True)

        self.set_title(imageOptionsTitle)
        self.set_default_size(450,375)

        prefercePage = Adw.PreferencesPage.new()
        self.add(page=prefercePage)

        imageOptions = Adw.PreferencesGroup.new()

        nameEntry = Gtk.Entry()
        nameEntry.set_hexpand(True)
        nameEntry.set_text(fullName)
        nameEntry.set_valign(Gtk.Align.CENTER)

        renameButton = Gtk.Button()
        renameButton.connect('clicked', manageImages.renameImage, appImage, nameEntry, os.path.dirname(appImage), refresh)
        renameButton.set_icon_name(icon_name='emblem-ok-symbolic')
        renameButton.set_valign(Gtk.Align.CENTER)

        self.renameImage = Adw.ActionRow.new()
        self.renameImage.set_title(title=globalName + ':')
        self.renameImage.add_suffix(nameEntry)
        self.renameImage.add_suffix(renameButton)
        imageOptions.add(child=self.renameImage)

        st = os.stat(appImage)
        executable = bool(st.st_mode & stat.S_IEXEC)

        executableSw = Gtk.Switch.new()
        executableSw.set_valign(align=Gtk.Align.CENTER)
        if executable:
            executableSw.set_active(True)
        executableSw.connect('notify::active', manageImages.setExecutable, appImage, setRowState, row)

        setExecutable = Adw.ActionRow.new()
        setExecutable.set_title(title=imageOptionsExecutable)
        setExecutable.add_suffix(widget=executableSw)
        imageOptions.add(child=setExecutable)


        extractEntry = pathEntry(os.path.dirname(os.path.abspath(appImage)))
        extractEntry.set_hexpand(True)
        extractEntry.set_valign(Gtk.Align.CENTER)

        extractButton = Gtk.Button.new()
        extractButton.set_icon_name(icon_name='emblem-ok-symbolic')
        extractButton.set_valign(Gtk.Align.CENTER)
        extractButton.connect('clicked', manageImages.extractImage, appImage, extractEntry, parent, nameEntry)

        extractImage = Adw.ActionRow.new()
        extractImage.set_title(title=imageOptionsExtract)
        extractImage.add_suffix(extractEntry)
        extractImage.add_suffix(extractButton)

        startInTerminalSw = Gtk.Switch.new()
        startInTerminalSw.set_active(False)
        startInTerminalSw.set_valign(align=Gtk.Align.CENTER)
        # startInTerminalSw.connect('notify::active', manageImages.createShortcut, 'desktop', str(pathlib.Path.home())+'/Desktop', appImage)

        startInTerminal = Adw.ActionRow.new()
        startInTerminal.set_title(title=imageOptionsStartTerminal)
        startInTerminal.add_suffix(widget=startInTerminalSw)


        # integrateSw = Gtk.Switch.new()
        # integrateSw.set_active(False)
        # integrateSw.set_valign(align=Gtk.Align.CENTER)
        # integrateSw.connect('notify::active', manageImages.integrateImage, appImage, flatpak)

        # setLauncherShortcut = Adw.ActionRow.new()
        # setLauncherShortcut.set_title(title='System integrate:')
        # setLauncherShortcut.add_suffix(widget=integrateSw)

        imageOptions.add(child=startInTerminal)
        # imageOptions.add(child=setLauncherShortcut)
        imageOptions.add(child=extractImage)

        prefercePage.add(imageOptions)
