import gi
import os
# import library.getFiles as count
from .library.getContent import *
# from .library.getContent import *
from threading import Thread


gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class mainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.set_title(title='Library')
        self.set_size_request(600,400)

        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.set_child(self.stack)

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

        newAppImage = Gtk.Button()
        newAppImage.connect('clicked', Flake.createAppImage)
        newAppImage.set_icon_name(icon_name='list-add-symbolic')
        headerbar.pack_start(child=newAppImage)

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
        dialog = Adw.AboutWindow()
        dialog.set_application_name=("Flake")
        dialog.set_version("0.0.4")
        dialog.set_developer_name("Leonardo Salani")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("GTK user insterface for appimagekit")
        dialog.set_website("https://github.com/SalaniLeo/Flake")
        dialog.set_developers(["salaniLeo"])
        dialog.set_application_icon("io.github.salaniLeo.flake")
        dialog.present()

    def createAppImage(self, button):
        None


class FlakePreferences(Adw.PreferencesWindow):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title(title='Preferences')
        self.settings = Gio.Settings.new("io.github.salanileo.flake")
        autoDeleteOption = self.settings.get_boolean("removeappdir")
        autoFolderMode = self.settings.get_boolean("foldermode")
        autoCustomAppRun = self.settings.get_boolean("customapprun")
        self.libraryPath = self.settings.get_string("librarypath")

        prefercePage = Adw.PreferencesPage.new()
        self.add(page=prefercePage)

        imageCreatorOptions = Adw.PreferencesGroup.new()
        imageCreatorOptions.set_title(title='General')

        self.autoDelete = Gtk.Switch.new()
        self.autoDelete.set_valign(align=Gtk.Align.CENTER)
        self.autoDelete.connect('notify::active', self.saveOpt, "removeappdir")
        self.autoDelete.set_state(autoDeleteOption)

        deleteADRow = Adw.ActionRow.new()
        deleteADRow.set_title(title='Auto delete AppDir')
        deleteADRow.add_suffix(widget=self.autoDelete)
        imageCreatorOptions.add(child=deleteADRow)



        self.autoFolderMSw = Gtk.Switch.new()
        self.autoFolderMSw.set_valign(align=Gtk.Align.CENTER)
        self.autoFolderMSw.connect('notify::active', self.saveOpt, "foldermode")
        self.autoFolderMSw.set_state(autoFolderMode)

        autoFolderMRow = Adw.ActionRow.new()
        autoFolderMRow.set_title(title='Enable FolderMode by default')
        autoFolderMRow.add_suffix(widget=self.autoFolderMSw)
        imageCreatorOptions.add(child=autoFolderMRow)



        self.autoCustomARSw = Gtk.Switch.new()
        self.autoCustomARSw.set_valign(align=Gtk.Align.CENTER)
        self.autoCustomARSw.connect('notify::active', self.saveOpt, "customapprun")
        self.autoCustomARSw.set_state(autoCustomAppRun)

        autoCustomARRow = Adw.ActionRow.new()
        autoCustomARRow.set_title(title='Enable custom AppRun by default')
        autoCustomARRow.add_suffix(widget=self.autoCustomARSw)
        imageCreatorOptions.add(child=autoCustomARRow)


        libraryOptions = Adw.PreferencesGroup.new()
        libraryOptions.set_title(title='Library')

        prefercePage.add(group=libraryOptions)
        prefercePage.add(group=imageCreatorOptions)

        self.libraryPathEntry = Gtk.Entry.new()
        self.libraryPathEntry.set_valign(align=Gtk.Align.CENTER)

        if os.path.exists(self.libraryPath):
            self.libraryPathEntry.set_text(self.libraryPath)
        else:
            self.libraryPathEntry.set_text("~/Applications")

        self.libraryPathEntry.connect('changed', self.saveString, "librarypath")

        libraryPathRow = Adw.ActionRow.new()
        libraryPathRow.set_title(title='Library location')
        libraryPathRow.add_suffix(widget=self.libraryPathEntry)
        libraryOptions.add(child=libraryPathRow)

    def saveOpt(self, switch, GParamBoolean, key):
        self.settings.set_boolean(key, switch.get_state())

    def saveString(self, entry, key):
        if os.path.exists(entry.get_text()):
                self.settings.set_string(key, entry.get_text())

    def releadLibrary(path):
        None


if __name__ == '__main__':
    import sys

    app = Flake()
    app.run(sys.argv)

