import gi
import imageCreator
import shutil
import ui.errorWindow

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
        
# opens popup window for exe selection
    def chooseExe(self, button):
        dialog = Gtk.FileChooserDialog(title="choose the executable",parent=None)
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(500, 500)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            imageCreator.exe = dialog.get_filename()
            exeEntry.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            None

        dialog.destroy()

# opens popup window for icon selection
    def chooseIcon(self, button):
        dialog = Gtk.FileChooserDialog(title="choose the icon",parent=None)
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(500, 500)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            imageCreator.icon = dialog.get_filename()
            iconEntry.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            None

        dialog.destroy()


# saves and switches page for the main window
    def confirm(self, button):

        # if none or "" start building the app
        if None or "" not in (nameEntry.get_text(),exeEntry.get_text(),iconEntry.get_text(),typeEntry.get_text(),categoriesEntry.get_text()):

            sp.add_from_file("secondPage.ui")
            sp.connect_signals(spHandler())
            secondPage = sp.get_object("secondPage")
            secondPage.set_title("AppImageCreator")
        
            
            if(builder.get_object("folderMSwitch").get_active()):
                
                spHandler.AdvOption("folderMLabel",True)
                spHandler.AdvOption("folderMEntry",True)
                spHandler.AdvOption("folderMButton",True)
                
            if(builder.get_object("CustomARSwitch").get_active()):
                
                spHandler.AdvOption("AppRLabel",True)
                spHandler.AdvOption("AppREntry",True)
                spHandler.AdvOption("AppRButton",True)

        else:
            # gives error back
            ui.errorWindow.error_message("please fill all the informations")

        
    # sets text to output entry
    def updateLoc(outputLoc):
        outputEntry = sp.get_object("outputEntry")
        outputEntry.set_text(outputLoc)
    
    #shows the advanced options grid when activated 
    def showAdvanced(self, widget, active):
        if active is True:
            AdvancedOGrid.set_visible(True)
        else:
            AdvancedOGrid.set_visible(False)
            

# hanlder of the other window
class spHandler():

    # opens folder chooser dialog
    def selectOutput(self, button):
        dialog = Gtk.FileChooserDialog(title="choose the icon",parent=None, action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(500, 500)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            Handler.updateLoc(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            None

        dialog.destroy()

    # starts creating the app
    def startCreating(self, button):

        expander = sp.get_object("expander")
        expander.set_expanded(True)
        outputConsole = sp.get_object("outputConsole")
        tb = outputConsole.get_buffer()
        end_iter = tb.get_end_iter()
        tb.insert(end_iter, imageCreator.start(nameEntry.get_text(),exeEntry.get_text(),iconEntry.get_text(),typeEntry.get_text(),categoriesEntry.get_text(),sp.get_object("outputEntry").get_text())) 
        # outputConsole.set_hexpand(True)
        remAppDir = sp.get_object("remAppDir")

        if(remAppDir.get_active()):
            shutil.rmtree(sp.get_object("outputEntry").get_text() + "/" + nameEntry.get_text() + ".AppDir/")

    def AdvOption(element, show):
        final = sp.get_object(element)
        final.set_visible(show)

def fileChooser():
    
        dialog = Gtk.FileChooserDialog(title="choose the icon",parent=None)
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(500, 500)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            return dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            None

# ui.errorWindow.error_message("could not copy the exe file")
# ui.errorWindow.error_message("could not copy icon")

sp = Gtk.Builder()

builder = Gtk.Builder()
builder.add_from_file("firstPage.ui")
builder.connect_signals(Handler())

nameEntry = builder.get_object('nameEntry')
exeEntry = builder.get_object('exeEntry')
iconEntry = builder.get_object('iconEntry')
typeEntry = builder.get_object('typeEntry')
categoriesEntry = builder.get_object('categoriesEntry')
AdvancedOSwitch = builder.get_object('AdvancedOSwitch')
AdvancedOGrid = builder.get_object('AdvancedOGrid')

Gtk.main()