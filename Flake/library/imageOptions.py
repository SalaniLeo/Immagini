import gi
import subprocess
import os
import stat
import threading
import pathlib
from ..creator import error
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gtk, Gdk, Adw

imagePath = ""

class manageImages(list):
    def __init__(self, list, loc): 
        menu = Gtk.Menu()
        menu_item = Gtk.MenuItem("A menu item")
        menu.append(menu_item)
        menu_item.show()

    def executeImage(imagePath, executable):
        
        if not executable:
                error.throwError(None, "The app has no executable permissions", "Permission denied")
        else:
                subprocess.run(imagePath)

    def deleteImage(button, imagePath, refresh, name, mainWindow, setRowState, row):
        manageImages.askSure(name, imagePath, refresh, mainWindow)

    def askSure(name, imagePath, refresh, mainWindow):

        dialog = Adw.MessageDialog.new()

        dialog.set_transient_for(mainWindow)
        dialog.set_modal(True)
        dialog.set_heading(heading='Delete ' + name + "?")
        dialog.set_body(body='Deleting an appimage file is not reversible')
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

    def extractImage(button, imagePath, entry):
        command = "cd " + entry.get_text() + " && " + imagePath + " /app/bin/Flake/creator/builder/tool/AppRun --appimage-extract"

        os.popen(command)


    def renameImage(button, appImage, name, loc, refresh, imageName=None, imageNum=None):
        dst = loc + "/" + name.get_text() + ".AppImage"

        os.rename(appImage, dst)

        refresh(None, None, None)

imageNum = None
imageNames = None

def runImage():
    subprocess.run(imagePath)

class imageOptions(Adw.PreferencesWindow):

    def __init__(self, parent, refresh, appImage, fullName, setRowState, row, **kwargs):
        super().__init__(**kwargs)  

        self.set_transient_for(parent)
        self.set_modal(True)

        self.set_title(title='Image options')
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

        renameImage = Adw.ActionRow.new()
        renameImage.set_title(title='Name:')
        renameImage.add_suffix(nameEntry)
        renameImage.add_suffix(renameButton)
        imageOptions.add(child=renameImage)

        st = os.stat(appImage)
        executable = bool(st.st_mode & stat.S_IEXEC)

        executableSw = Gtk.Switch.new()
        executableSw.set_valign(align=Gtk.Align.CENTER)
        if executable:
            executableSw.set_active(True)
        executableSw.connect('notify::active', manageImages.setExecutable, appImage, setRowState, row)

        setExecutable = Adw.ActionRow.new()
        setExecutable.set_title(title='Executable:')
        setExecutable.add_suffix(widget=executableSw)
        imageOptions.add(child=setExecutable)


        extractEntry = Gtk.Entry()
        extractEntry.set_hexpand(True)
        extractEntry.set_text(os.path.dirname(os.path.abspath(appImage)))
        extractEntry.set_valign(Gtk.Align.CENTER)

        extractButton = Gtk.Button.new()
        extractButton.set_icon_name(icon_name='emblem-ok-symbolic')
        extractButton.set_valign(Gtk.Align.CENTER)
        extractButton.connect('clicked', manageImages.extractImage, appImage, extractEntry)

        extractImage = Adw.ActionRow.new()
        extractImage.set_title(title='Extract image:')
        extractImage.add_suffix(extractEntry)
        extractImage.add_suffix(extractButton)

        # desktopShortcutSw = Gtk.Switch.new()
        # desktopShortcutSw.set_active(False)
        # desktopShortcutSw.set_valign(align=Gtk.Align.CENTER)
        # desktopShortcutSw.connect('notify::active', manageImages.createShortcut, 'desktop', str(pathlib.Path.home())+'/Desktop', appImage)

        # setDesktopShortcut = Adw.ActionRow.new()
        # setDesktopShortcut.set_title(title='Desktop shortcut:')
        # setDesktopShortcut.add_suffix(widget=desktopShortcutSw)


        # launcherShortcutSw = Gtk.Switch.new()
        # launcherShortcutSw.set_active(False)
        # launcherShortcutSw.set_valign(align=Gtk.Align.CENTER)
        # launcherShortcutSw.connect('notify::active', manageImages.createShortcut, 'launcher', str(pathlib.Path.home())+'/.local/bin', appImage)

        # setLauncherShortcut = Adw.ActionRow.new()
        # setLauncherShortcut.set_title(title='Launcher shortcut:')
        # setLauncherShortcut.add_suffix(widget=launcherShortcutSw)

        # imageOptions.add(child=setDesktopShortcut)
        # imageOptions.add(child=setLauncherShortcut)
        imageOptions.add(child=extractImage)


        prefercePage.add(imageOptions)