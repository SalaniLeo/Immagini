import sys
from .imageCreator import start
import shutil
from .creator.error import *
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, Gdk, GLib

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.set_size_request(600,400)
        
        css_provider = Gtk.CssProvider()
        css_provider.load_from_resource('/io/github/salaniLeo/flake/assets/app.css')
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        style_context = self.get_style_context()
        style_context.add_provider_for_display(self.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

                          
        self.header = Gtk.HeaderBar()
        title_label = Gtk.Label()
        title_label.set_markup("<b>Flake</b>")
        self.header.set_title_widget(title_label)
        self.set_titlebar(self.header)
        self.header.set_name("headerbar")
        self.set_name("window")
        
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.switch = Gtk.Switch()
        self.label = Gtk.Label(label="Advanced:")
        self.switch_box.append(self.label)
        self.switch_box.append(self.switch)
        self.header.pack_start(self.switch_box)
        self.switch_box.set_spacing(5) # Add some spacing
        
        self.switch.connect("state-set", self.showAdvanced)
        
        #stack for confirm animation
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.set_child(self.stack)

        #main box in the middle
        self.mainBox = Gtk.Grid()
        self.stack.add_child(self.mainBox)
        self.mainBox.set_name("mainBox")
        self.set_default_size(750,400)
        
        self.topBox = Gtk.Box()
        self.mainBox.attach(self.topBox, 0, 0, 2, 1)
        self.topBox.set_vexpand(True)
        
        self.bottomBox = Gtk.Box()
        self.mainBox.attach(self.bottomBox, 0, 4, 1, 1)
        self.bottomBox.set_vexpand(True)

        self.leftBox = Gtk.Box()
        self.mainBox.attach(self.leftBox, 0, 0, 1, 1)
        self.leftBox.set_hexpand(True)
        
        self.rightBox = Gtk.Box()
        self.mainBox.attach(self.rightBox, 2, 0, 1, 2)
        self.rightBox.set_hexpand(True)
        
        
        
        self.centerGrid = Gtk.Grid()
        self.mainBox.attach(self.centerGrid, 1, 1, 1, 1)
        self.centerGrid.set_name("centerGrid")
        self.centerGrid.set_hexpand(True)
        # self.centerGrid.set_row_spacing(12)
        # self.centerGrid.set_column_spacing(12)
        
        
        self.nameLabel = Gtk.Label(label="Name:")
        self.centerGrid.attach(self.nameLabel,0,0,1,1)
        self.nameLabel.set_name("nameLabel")
        self.nameLabel.set_xalign(0.0)
        
        self.nameEntry = Gtk.Entry()
        self.centerGrid.attach(self.nameEntry,1,0,3,1)
        self.nameEntry.set_name("nameEntry")                
        
        self.exeLabel = Gtk.Label(label="Executable:")
        self.centerGrid.attach(self.exeLabel,0,1,1,1) 
        self.exeLabel.set_name("exeLabel")
        self.exeLabel.set_xalign(0.0)

        self.exeEntry = Gtk.Entry()
        self.centerGrid.attach(self.exeEntry,1,1,2,1) 
        self.exeEntry.set_name("exeEntry")
        self.exeEntry.set_hexpand(True)


        self.exeBrowse = Gtk.Button(label="browse")
        self.centerGrid.attach(self.exeBrowse,3,1,1,1)
        self.exeBrowse.set_name("exeBrowse")
        self.exeBrowse.connect("clicked", self.chooseExe)    


        self.iconLabel = Gtk.Label(label="Icon:")
        self.centerGrid.attach(self.iconLabel,0,2,1,1) 
        self.iconLabel.set_name("iconLabel")
        self.iconLabel.set_xalign(0.0)

        self.iconEntry = Gtk.Entry()
        self.centerGrid.attach(self.iconEntry,1,2,1,1) 
        self.iconEntry.set_name("iconEntry")
        self.iconEntry.set_hexpand(True)
        
        self.iconBrowse = Gtk.Button(label="browse")
        self.centerGrid.attach(self.iconBrowse,3,2,1,1)
        self.iconBrowse.set_name("iconBrowse")
        self.iconBrowse.connect("clicked", self.chooseIcon)    
        
        
        
        self.typeLabel = Gtk.Label(label="Type:")
        self.centerGrid.attach(self.typeLabel,0,3,1,1)
        self.typeLabel.set_name("typeLabel")
        self.typeLabel.set_xalign(0.0)

        self.typeEntry = Gtk.Entry()
        self.centerGrid.attach(self.typeEntry,1,3,3,1)
        self.typeEntry.set_name("typeEntry")
        self.typeEntry.set_hexpand(True)
        
    
    
        self.categoryLabel = Gtk.Label(label="Category:")
        self.centerGrid.attach(self.categoryLabel,0,4,1,1)
        self.categoryLabel.set_name("categoryLabel")
        self.categoryLabel.set_xalign(0.0)

        self.categoriesEntry = Gtk.Entry()
        self.centerGrid.attach(self.categoriesEntry,1,4,3,1)
        self.categoriesEntry.set_name("categoriesEntry")
        
    
        self.okBLabel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)    
        self.mainBox.attach(self.okBLabel, 0, 3, 3, 1)
        self.okBLabel.set_homogeneous(True)
        self.okBLabel.set_hexpand(False)
        self.okBLabel.set_name("okBLabel")
        self.okBLabel.set_baseline_position(Gtk.BaselinePosition.CENTER)

        self.okButton = Gtk.Button(label="confirm")

        self.okButton.set_size_request(80, -1)  # imposta la larghezza a 80 pixel
        self.okButton.set_halign(Gtk.Align.CENTER)  # imposta l'allineamento al centro
        self.okButton.set_valign(Gtk.Align.CENTER)  # imposta l'allineamento al centro
        self.okButton.connect("clicked", self.confirm)
        self.okBLabel.append(self.okButton)  #inserisci il bottone nella bottomBox

        self.AdvancedOGrid = Gtk.Grid()
        self.mainBox.attach(self.AdvancedOGrid,1,2,1,1)
        self.AdvancedOGrid.set_visible(False)
        # self.AdvancedOGrid.set_size_request(100,100)
        self.AdvancedOGrid.set_name("advGrid")
        
        self.folderMLabel = Gtk.Label(label="Folder mode:")
        self.AdvancedOGrid.attach(self.folderMLabel,0,0,1,1)
        
        self.folderMSwitch = Gtk.Switch()
        self.AdvancedOGrid.attach(self.folderMSwitch,1,0,1,1)


        self.customARLabel = Gtk.Label(label="Custom apprun:")
        self.AdvancedOGrid.attach(self.customARLabel,0,1,1,1)

        self.customARSwitch = Gtk.Switch()
        self.AdvancedOGrid.attach(self.customARSwitch,1,1,1,1)
        
        
        
        
        ###Second Page###
        self.secondPage = Gtk.Grid()
        self.stack.add_child(self.secondPage)
        self.secondPage.set_row_spacing(35)
        self.secondPage.set_column_spacing(35)

        
        self.backButton = Gtk.Button.new_from_icon_name("pan-start-symbolic") 
        self.backButton.connect("clicked", self.goBack)
    
        
        self.topBox2 = Gtk.Box()
        self.secondPage.attach(self.topBox2, 0, 0, 2, 1)
        self.topBox2.set_vexpand(True)
        
        self.bottomBox2 = Gtk.Box()
        self.secondPage.attach(self.bottomBox2, 0, 4, 1, 1)
        self.bottomBox2.set_vexpand(True)
        
        self.bottomBox2 = Gtk.Box()
        self.secondPage.attach(self.bottomBox2, 0, 5, 1, 1)
        self.bottomBox2.set_vexpand(True)

        self.leftBox2 = Gtk.Box()
        self.secondPage.attach(self.leftBox2, 0, 0, 1, 1)
        self.leftBox2.set_hexpand(True)
        
        self.rightBox2 = Gtk.Box()
        self.secondPage.attach(self.rightBox2, 2, 0, 1, 2)
        self.rightBox2.set_hexpand(True)
        
        self.centerGrid2 = Gtk.Grid()
        self.secondPage.attach(self.centerGrid2, 1, 1, 1, 1)
        self.centerGrid2.set_hexpand(True)
        # self.centerGrid2.set_vexpand(True)
        self.centerGrid2.set_column_spacing(12)
        self.centerGrid2.set_row_spacing(12)


        
        self.outputFLabel = Gtk.Label(label="Output folder:")
        self.centerGrid2.attach(self.outputFLabel,0,0,1,1) 
        self.outputFLabel.set_name("exeLabel")
        self.outputFLabel.set_xalign(0.0)

        self.outputFEntry = Gtk.Entry()
        self.centerGrid2.attach(self.outputFEntry,1,0,2,1) 
        self.outputFEntry.set_hexpand(True)

        self.outputFBrowse = Gtk.Button(label="browse")
        self.centerGrid2.attach(self.outputFBrowse,3,0,1,1)
        self.outputFBrowse.connect("clicked", self.chooseOutputLoc)    
        
        
        
        self.secondPARFileLabel = Gtk.Label(label="Custom AppRun file:")
        self.centerGrid2.attach(self.secondPARFileLabel,0,1,1,1) 
        self.secondPARFileLabel.set_name("exeLabel")
        self.secondPARFileLabel.set_xalign(0.0)
        self.secondPARFileLabel.set_visible(False)


        self.secondPARFileEntry = Gtk.Entry()
        self.centerGrid2.attach(self.secondPARFileEntry,1,1,2,1) 
        self.secondPARFileEntry.set_hexpand(True)
        self.secondPARFileEntry.set_visible(False)


        self.secondPARFileBrowse = Gtk.Button(label="browse")
        self.centerGrid2.attach(self.secondPARFileBrowse,3,1,1,1)
        self.secondPARFileBrowse.connect("clicked", self.chooseAppRunLoc) 
        self.secondPARFileBrowse.set_visible(False)
        
        
        
        self.secondPPFolderLabel = Gtk.Label(label="App parent folder:")
        self.centerGrid2.attach(self.secondPPFolderLabel,0,2,1,1) 
        self.secondPPFolderLabel.set_name("exeLabel")
        self.secondPPFolderLabel.set_xalign(0.0)
        self.secondPPFolderLabel.set_visible(False)


        self.secondPPFolderEntry = Gtk.Entry()
        self.centerGrid2.attach(self.secondPPFolderEntry,1,2,2,1) 
        self.secondPPFolderEntry.set_hexpand(True)
        self.secondPPFolderEntry.set_visible(False)


        self.secondPPFolderBrowse = Gtk.Button(label="browse")
        self.centerGrid2.attach(self.secondPPFolderBrowse,3,2,1,1)
        self.secondPPFolderBrowse.connect("clicked", self.chooseAppParentFolder)
        self.secondPPFolderBrowse.set_visible(False)
        
        
        self.confirmGrid = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.secondPage.attach(self.confirmGrid, 1, 3, 1, 1)
        self.confirmGrid.set_hexpand(True)
        self.confirmGrid.set_spacing(12)
        self.confirmGrid.set_baseline_position(Gtk.BaselinePosition.CENTER)
        
        
        self.remAppDirBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.removeAppDir = Gtk.Switch()
        self.label = Gtk.Label(label="Remove AppDir:")
        self.remAppDirBox.append(self.label)
        self.remAppDirBox.append(self.removeAppDir)
        self.confirmGrid.append(self.remAppDirBox)
        self.remAppDirBox.set_spacing(12)

        self.expander = Gtk.Expander()
        self.confirmGrid.append(self.expander)
        self.outputConsole = Gtk.TextView(editable=False)
        self.outputConsole.set_editable(False)
        self.expander.set_child(self.outputConsole)
        self.expander.set_label("Console output")
        self.expander.set_size_request(100,100)
        
        self.createBLabel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)    
        self.confirmGrid.append(self.createBLabel)
        self.createBLabel.set_homogeneous(True)
        self.createBLabel.set_hexpand(False)
        self.createBLabel.set_name("aaa")
        self.createBLabel.set_baseline_position(Gtk.BaselinePosition.CENTER)

        self.createButton = Gtk.Button(label="confirm")

        self.createButton.set_size_request(80, -1)
        self.createButton.set_halign(Gtk.Align.CENTER)
        self.createButton.set_valign(Gtk.Align.CENTER)
        self.createButton.connect("clicked", self.startCreating)
        self.createBLabel.append(self.createButton)
        
        
        
    def goBack(self, button):
        if(self.expander.get_expanded()):
            self.expander.set_expanded(False)
            self.set_default_size(750,400)
        self.stack.set_visible_child(self.mainBox)
        self.header.remove(self.backButton)
        self.header.pack_start(self.switch_box)
        
    def goFarw(self):
        self.stack.set_visible_child(self.secondPage)
        self.header.remove(self.switch_box)
        self.header.pack_start(self.backButton)

    def showAdvanced(self, widget, active):
        if active is True:
            self.AdvancedOGrid.set_visible(True)
        else:
            self.AdvancedOGrid.set_visible(False)


# saves and switches page for the main window
    def confirm(self, button):

        # if none or "" start building the app
        if None or "" not in (self.nameEntry.get_text(),
                              self.exeEntry.get_text(),
                              self.iconEntry.get_text(),
                              self.typeEntry.get_text(),
                              self.categoriesEntry.get_text()):
            
            self.goFarw()
            
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


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()  
        
    # def throwError(self, error, title):
    #     dialog = Gtk.MessageDialog(
    #             parent         = self,
    #             message_type   = Gtk.MessageType.ERROR,
    #             secondary_text = error,
    #             text           = title,
    #             buttons        = Gtk.ButtonsType.CLOSE,
    #     )
        # result = dialog.show()
        # print(dialog.response)
        # if result == Gtk.ResponseType.CLOSE:
        #     dialog.destroy()

def main(version):
    app = MyApp(application_id="io.github.salaniLeo.flake")
    app.run(sys.argv)
        
