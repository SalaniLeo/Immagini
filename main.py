import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib, Gdk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.set_size_request(600,400)


        css_provider = Gtk.CssProvider()
        css_provider.load_from_file(Gio.File.new_for_path('/home/leo/Apps/Visual Studio Code/flake/app.css'))
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        style_context = self.get_style_context()
        style_context.add_provider_for_display(self.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

                          
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.header.set_name("headerbar")
        self.set_name("window")
        
        
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.switch = Gtk.Switch()
        # self.switch.set_active(True)  # Let's default it to on
        # self.switch.connect("state-set", self.switch_switched) # Lets trigger a function
        self.label = Gtk.Label(label="Advanced:")
        self.switch_box.append(self.label)
        self.switch_box.append(self.switch)
        self.header.pack_start(self.switch_box)
        self.switch_box.set_spacing(5) # Add some spacing
        
        self.switch.connect("state-set", self.showAdvanced) # Lets trigger a function

        #main box in the middle
        self.mainBox = Gtk.Grid()
        self.set_child(self.mainBox)
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
        self.exeBrowse.connect('clicked', self.chooseExe)

        
        
        
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
        self.iconBrowse.connect('clicked', self.chooseIcon)
        
        
        
        
        self.typeLabel = Gtk.Label(label="Name:")
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
        self.okBLabel.set_name("aaa")
        self.okBLabel.set_baseline_position(Gtk.BaselinePosition.CENTER)

        self.okButton = Gtk.Button(label="confirm")

        self.okButton.set_size_request(80, -1)  # imposta la larghezza a 80 pixel
        self.okButton.set_halign(Gtk.Align.CENTER)  # imposta l'allineamento al centro
        self.okButton.set_valign(Gtk.Align.CENTER)  # imposta l'allineamento al centro
        self.okBLabel.append(self.okButton)  #inserisci il bottone nella bottomBox

        self.AdvancedOGrid = Gtk.Grid()
        self.mainBox.attach(self.AdvancedOGrid,1,2,1,1)
        self.AdvancedOGrid.set_visible(False)
        self.AdvancedOGrid.set_size_request(100,100)
        self.AdvancedOGrid.set_name("advGrid")
        
        self.folderMLabel = Gtk.Label(label="Folder mode:")
        self.AdvancedOGrid.attach(self.folderMLabel,0,0,1,1)
        
        self.folderMSwitch = Gtk.Switch()
        self.AdvancedOGrid.attach(self.folderMSwitch,1,0,1,1)


        self.customARLabel = Gtk.Label(label="Custom apprun:")
        self.AdvancedOGrid.attach(self.customARLabel,0,1,1,1)

        self.customARSwitch = Gtk.Switch()
        self.AdvancedOGrid.attach(self.customARSwitch,1,1,1,1)
    
    # opens popup window for exe selection
#     def chooseExe(self, button):
#         self.exeEntry.set_text(fileChooser("Choose executable file", False))

# # opens popup window for icon selection
#     def chooseIcon(self, button):
#         self.iconEntry.set_text(fileChooser("Choose executable file", False, True))

    #shows the advanced options grid when activated 
    def showAdvanced(self, active):
        if active is True:
            self.AdvancedOGrid.set_visible(True)
        else:
            self.AdvancedOGrid.set_visible(False)


        self.open_dialog = Gtk.FileChooserNative.new(title="Choose a file",
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)

        self.open_dialog.connect("response", self.open_response)
        self.exeBrowse.connect("clicked", self.show_open_dialog)

    def show_open_dialog(self, button):
        self.open_dialog.show()

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            filename = file.get_path()
            print(filename)  # Here you could handle opening or saving the file





# def fileChooser(title, folderOnly=Gtk.FileChooserAction.OPEN,iconFilter=False):
    
#         if(folderOnly):
#             folderOnly = Gtk.FileChooserAction.SELECT_FOLDER
    
#         dialog = Gtk.FileChooserDialog(title=title,action=folderOnly,parent=None)
#         # dialog.add_buttons(Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK)
#         dialog.set_default_size(500, 500)
#         # dialog.set_current_folder("/home/leo/Desktop")

#         if(iconFilter):
#             filter_text = Gtk.FileFilter()
#             filter_text.set_name("icon")
#             filter_text.add_pattern("*.svg")
#             filter_text.add_pattern("*.png")
#             filter_text.add_pattern("*.jpg")
#             dialog.add_filter(filter_text)

#         response = dialog.run()
#         if response == Gtk.ResponseType.OK:
#             file = dialog.get_filename()
#             dialog.destroy()
#             if(file is None):
#                 file = " "
#             return file
#         elif response == Gtk.ResponseType.CANCEL:
#             dialog.destroy()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="dev.sudatoleo.flake")
app.run(sys.argv)

