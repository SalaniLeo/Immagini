<<<<<<< Updated upstream
# from .creator.error import *
# import gi
# gi.require_version('Gtk', '4.0')
# gi.require_version('Adw', '1')
# gi.require_version('Gio', '2.0')
# from gi.repository import Gtk, Adw, Gio, Gdk, GLib
# from .ui import createAppImage

# class MainWindow(Gtk.ApplicationWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.set_size_request(750,450)
        
#         #CSS
#         css_provider = Gtk.CssProvider()
#         css_provider.load_from_resource('/io/github/salaniLeo/flake/assets/app.css')
#         css_provider.load_from_file(Gio.File.new_for_path('assets/app.css'))
#         Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
#         style_context = self.get_style_context()
#         style_context.add_provider_for_display(self.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)


#         #headerbar    
#         self.header = Gtk.HeaderBar()
#         title_label = Gtk.Label()
#         title_label.set_markup("<b>Flake</b>")
#         self.header.set_title_widget(title_label)
#         self.set_titlebar(self.header)
#         self.header.set_name("headerbar")
#         self.set_name("window")


#         #headerbarmenu
#         menu = Gio.Menu.new()

#         self.popover = Gtk.PopoverMenu()
#         self.popover.set_menu_model(menu)

#         self.menuButton = Gtk.MenuButton()
#         self.menuButton.set_popover(self.popover)
#         self.menuButton.set_icon_name("open-menu-symbolic")

#         self.header.pack_end(self.menuButton)


#         preferences = Gio.SimpleAction.new("preferences", None)
#         preferences.connect("activate", self.show_preferences)
#         self.add_action(preferences)
        
#         menu.append("Preferences", "win.preferences") 
#         menu.append("About Flake", "win.about")


#         #plus button
#         self.plusButton = Gtk.Button()
#         self.plusButton.connect("clicked", newAppImage)
#         self.plusButton.set_icon_name("list-add-symbolic")

#         self.header.pack_start(self.plusButton)



# def newAppImage(self):
#     createAppImage.on_activate(self)


# class Flake(Adw.Application):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.connect('activate', self.on_activate)

    # def on_activate(self, app):
    #     self.win = MainWindow(application=app)
    #     self.win.present()  

import gi
import os
# import library.getFiles as count
from .library.getFiles import getFiles
=======
import gi
import os
# import library.getFiles as count
from .library.getContent import *
# from .library.getContent import *
from threading import Thread

>>>>>>> Stashed changes

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class mainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.set_title(title='Library')
        self.set_size_request(600,400)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.set_child(self.stack)

<<<<<<< Updated upstream
        imagesDir = '/home/leo/Apps'

        appslist = os.listdir(imagesDir)

        appsInfo = getFiles(appslist, imagesDir)

        flowbox = Gtk.FlowBox.new()
        flowbox.set_margin_top(margin=12)
        flowbox.set_margin_end(margin=12)
        flowbox.set_margin_bottom(margin=12)
        flowbox.set_margin_start(margin=12)
        flowbox.set_valign(align=Gtk.Align.START)
        flowbox.set_max_children_per_line(n_children=10)
        flowbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        self.stack.add_child(child=flowbox)

        for n in range(appsInfo.appimages):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            flowbox.insert(widget=button, position=n)
=======
        self.flowbox = Gtk.FlowBox.new()
        self.flowbox.set_margin_top(margin=12)
        self.flowbox.set_margin_end(margin=12)
        self.flowbox.set_margin_bottom(margin=12)
        self.flowbox.set_margin_start(margin=12)
        self.flowbox.set_valign(align=Gtk.Align.START)
        self.flowbox.set_max_children_per_line(n_children=10)
        self.flowbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        self.stack.add_child(child=self.flowbox)

        t1 = Thread(target=self.images)
        t1.start()
>>>>>>> Stashed changes

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferences', 'app.preferences')

        about = Gio.SimpleAction.new("about", None)
        about.connect("activate", Flake.show_about)

        menu_button_model.append('About', 'app.about')

        menuButton = Gtk.MenuButton.new()
        menuButton.set_icon_name(icon_name='open-menu-symbolic')
        menuButton.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menuButton)
<<<<<<< Updated upstream
        
=======

>>>>>>> Stashed changes
        newAppImage = Gtk.Button()
        newAppImage.connect('clicked', Flake.createAppImage)
        newAppImage.set_icon_name(icon_name='list-add-symbolic')
        headerbar.pack_start(child=newAppImage)

<<<<<<< Updated upstream

class Flake(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.Example',
=======
        # self.test = FlakePreferences.

    def images(self):

            test = FlakePreferences()

            imagesDir = test.settings.get_string("librarypath")
            appslist = os.listdir(imagesDir)
            appsInfo = getFileNum(appslist, imagesDir)
            time.sleep(0.5)
            for n in range(appsInfo.appimages):
                self.flowbox.insert(widget=createElements(imagesDir, appsInfo.names[n]), position=n)


class Flake(Adw.Application):

    def __init__(self,AppId):
        super().__init__(application_id=AppId,
>>>>>>> Stashed changes
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app)
        self.create_action('preferences', self.show_preferences)
        self.create_action('about', self.show_about)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = mainWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def show_preferences(self, action, param):
        adw_preferences_window = FlakePreferences()
        adw_preferences_window.show()

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)

    def show_about(self, action, param):
<<<<<<< Updated upstream
        dialog = Adw.AboutWindow() 
        dialog.set_application_name=("Flake") 
        dialog.set_version("0.0.4") 
        dialog.set_developer_name("Leonardo Salani") 
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0)) 
        dialog.set_comments("GTK user insterface for appimagekit") 
        dialog.set_website("https://github.com/SalaniLeo/Flake") 
        # dialog.add_credit_section("Contributors", ["salaniLeo"]) 
        # dialog.set_translator_credits("Italian: Leonardo Salani")
        # dialog.set_copyright("© 2022 developer")
        dialog.set_developers(["salaniLeo"]) 
        dialog.set_application_icon("io.github.salaniLeo.flake") # icon must be uploaded in ~/.local/share/icons or /usr/share/icons
=======
        dialog = Adw.AboutWindow()
        dialog.set_application_name=("Flake")
        dialog.set_version("0.0.4")
        dialog.set_developer_name("Leonardo Salani")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("GTK user insterface for appimagekit")
        dialog.set_website("https://github.com/SalaniLeo/Flake")
        dialog.set_developers(["salaniLeo"])
        dialog.set_application_icon("io.github.salaniLeo.flake")
>>>>>>> Stashed changes
        dialog.present()

    def createAppImage(self, button):
        None

<<<<<<< Updated upstream
class FlakePreferences(Adw.PreferencesWindow):

=======

class FlakePreferences(Adw.PreferencesWindow):
    
>>>>>>> Stashed changes
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title(title='Preferences')
        self.settings = Gio.Settings.new("io.github.salanileo.flake")
        autoDeleteOption = self.settings.get_boolean("removeappdir")
        autoFolderMode = self.settings.get_boolean("foldermode")
        autoCustomAppRun = self.settings.get_boolean("customapprun")
<<<<<<< Updated upstream
        libraryPath = self.settings.get_string("librarypath")
=======
        self.libraryPath = self.settings.get_string("librarypath")
>>>>>>> Stashed changes

        prefercePage = Adw.PreferencesPage.new()
        self.add(page=prefercePage)

<<<<<<< Updated upstream
        generalOptionsGroup = Adw.PreferencesGroup.new()
        generalOptionsGroup.set_title(title='General')

        prefercePage.add(group=generalOptionsGroup)
=======
        imageCreatorOptions = Adw.PreferencesGroup.new()
        imageCreatorOptions.set_title(title='General')
>>>>>>> Stashed changes

        self.autoDelete = Gtk.Switch.new()
        self.autoDelete.set_valign(align=Gtk.Align.CENTER)
        self.autoDelete.connect('notify::active', self.saveOpt, "removeappdir")
        self.autoDelete.set_state(autoDeleteOption)

        deleteADRow = Adw.ActionRow.new()
        deleteADRow.set_title(title='Auto delete AppDir')
        deleteADRow.add_suffix(widget=self.autoDelete)
<<<<<<< Updated upstream
        generalOptionsGroup.add(child=deleteADRow)
=======
        imageCreatorOptions.add(child=deleteADRow)
>>>>>>> Stashed changes



        self.autoFolderMSw = Gtk.Switch.new()
        self.autoFolderMSw.set_valign(align=Gtk.Align.CENTER)
        self.autoFolderMSw.connect('notify::active', self.saveOpt, "foldermode")
        self.autoFolderMSw.set_state(autoFolderMode)

        autoFolderMRow = Adw.ActionRow.new()
        autoFolderMRow.set_title(title='Enable FolderMode by default')
        autoFolderMRow.add_suffix(widget=self.autoFolderMSw)
<<<<<<< Updated upstream
        generalOptionsGroup.add(child=autoFolderMRow)
=======
        imageCreatorOptions.add(child=autoFolderMRow)
>>>>>>> Stashed changes



        self.autoCustomARSw = Gtk.Switch.new()
        self.autoCustomARSw.set_valign(align=Gtk.Align.CENTER)
<<<<<<< Updated upstream
        self.autoCustomARSw.connect('notify::active', self.saveOpt, "foldermode")
=======
        self.autoCustomARSw.connect('notify::active', self.saveOpt, "customapprun")
>>>>>>> Stashed changes
        self.autoCustomARSw.set_state(autoCustomAppRun)

        autoCustomARRow = Adw.ActionRow.new()
        autoCustomARRow.set_title(title='Enable custom AppRun by default')
        autoCustomARRow.add_suffix(widget=self.autoCustomARSw)
<<<<<<< Updated upstream
        generalOptionsGroup.add(child=autoCustomARRow)
=======
        imageCreatorOptions.add(child=autoCustomARRow)
>>>>>>> Stashed changes


        libraryOptions = Adw.PreferencesGroup.new()
        libraryOptions.set_title(title='Library')

        prefercePage.add(group=libraryOptions)
<<<<<<< Updated upstream

        self.libraryPathEntry = Gtk.Entry.new()
        self.libraryPathEntry.set_valign(align=Gtk.Align.CENTER)
        self.libraryPathEntry.set_text(libraryPath)
=======
        prefercePage.add(group=imageCreatorOptions)

        self.libraryPathEntry = Gtk.Entry.new()
        self.libraryPathEntry.set_valign(align=Gtk.Align.CENTER)

        if os.path.exists(self.libraryPath):
            self.libraryPathEntry.set_text(self.libraryPath)
        else:
            self.libraryPathEntry.set_text("~/Applications")

        self.libraryPathEntry.connect('changed', self.saveString, "librarypath")
>>>>>>> Stashed changes

        libraryPathRow = Adw.ActionRow.new()
        libraryPathRow.set_title(title='Library location')
        libraryPathRow.add_suffix(widget=self.libraryPathEntry)
        libraryOptions.add(child=libraryPathRow)

<<<<<<< Updated upstream
    # def checkAutoEnable(self, var):

    #     self.settings = Gio.Settings.new("io.github.salanileo.flake")
    #     if var is self.folderMSwitch:
    #         self.autoDeleteOption = self.settings.get_boolean("foldermode")
    #     elif var is self.customARSwitch:
    #         self.autoDeleteOption = self.settings.get_boolean("customapprun")
    #     elif var is self.removeAppDir:
    #         self.autoDeleteOption = self.settings.get_boolean("removeappdir")

    #     var.set_state(self.autoDeleteOption)

    def saveOpt(self, switch, GParamBoolean, key):
        self.settings.set_boolean(key, switch.get_state())

=======
    def saveOpt(self, switch, GParamBoolean, key):
        self.settings.set_boolean(key, switch.get_state())

    def saveString(self, entry, key):
        if os.path.exists(entry.get_text()):
                self.settings.set_string(key, entry.get_text())

    def releadLibrary(path):
        None

>>>>>>> Stashed changes

if __name__ == '__main__':
    import sys

    app = Flake()
    app.run(sys.argv)

