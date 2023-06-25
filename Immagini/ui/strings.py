from gettext import gettext as _

# ----- most used word ---- #
globalImmagini = _("Immagini")

globalName = _("Name")
globalExecutable = _("Executable")
globalIcon = _("Icon")
globalPath = _("Path")
globalCategory = _("Category")
globalType = _("Type")
globalDelete = _("Delete")
globalClose = _("Close")
globalRefresh = _("Refresh")
globalConfirm = _("Confirm")
globalTemplate = _("Template")
globalShare = _('Share folder')
globalLib = _('Libraries folder')
globalInfo = _('Info')
globalDesktop = _('Desktop file')

globalApplication = _("Application")
globalUtility = _("Utility")

globalLibraryTitle = _("Immagini - Library")
globalNewImageTitle = _("Immagini - New")
globalInstalledFlatpaks = _("Immagini - Installed Flatpaks")

# ----- MAIN WINDOW ----- #
menuRefresh = _("Refresh")
menuShowInFolder = _("Show in folder")
menuPreferences = _("Preferences")
menuShortcuts = _("Shortcuts")
menuAbout = _("About Immagini")

aboutWindowComment = _("Management tool for AppImage applications")

# ----- PREFERENCES WINDOW ----- #
prefrencesTitle = _("Preferences")
newImagePreferencesTitle = _("New image options")
libraryPreferencesTitle = _('Library options')

libraryLocationTitle = _('Library location')
libraryLocationSubtitle = _("To apply changes restart the app")
librarySelectionTitle = _('Select library location')

autoDeleteAppDirTitle = _('Auto delete AppDir')
autoDeleteAppDirSubtitle = _('Deletes the .AppDir folder after creating an AppImage file')

autoFolderModeTitle = _('Enable FolderMode by default')
autoFolderModeSubtitle = _('Automatically enables the "Folder Mode" option when creating a new image file')

autoCustomAppRunTitle = _('Enable custom AppRun by default')
autoCustomAppRunSubtitle = _('Automatically enables the "Custom AppRun" option when creating a new image file')

useLibraryPathTitle = _('Use library folder as default')
useLibraryPathSubtitle = _('Uses library folder as default location when creating new apps')

libraryPathChanged = _("Library path changed")

# ----- NEW IMAGE WINDOW ----- #

includeLibrariesTitle = _("Include libraries")
includeLibrariesSubtitle = _('Select a library to include inside an AppImage')
selectLibrariesTitle = _("Select libraries")

useFolderModeTitle = _("Folder mode")
useFolderModeSubtitle = _("Parent folder location")

useCustomAppRunTitle = _("Custom AppRun")
useCustomAppRunSubtitle = _("Custom AppRun location")

includeDependeciesTitle = _("Include dependencies")
installedIntepreters = _("Installed languages: ")
selectManually = _('Select manually: ')

createTemplateImage = _('Create template image')

outputLocationTitle = _("Location")
outputLocationSubtitle = _("App location")

selectFiles = _("Select files ")
selectFolders = _("Select folders ")
selectedItems = _("Selected items: ")

pleaseFillInAllInfoSubtitle = _("Please fill in all the informations")
pleaseFillInAllInfoTitle = _("All the info are required")

createNewOne = _('Create new')
convertFromFlatpak = _('Convert from Flatpak')

installedFlatpaks = _('Intalled Flatpaks')

executableNotProvidedByManifest = _("Not provided by manifest, may be wrong")
executableNotFoundInsideFlatpak = _("Can't locate binary inside flatpak application")

convertButtonLabel = _('Convert')

couldNotCopyFilesSubtilte = _('Could not copy the application files into the appimage')
couldNotCopyFilesTitle = _('Could not copy files')

# advanced options
advancedTitle = _("Advanced")

# ----- TERMINAL ----- #
terminalTitle = _('Terminal')


# ----- IMAGE OPTIONS ----- #
imageOptionsTitle = _('Image Options')
imageOptionsExecutable = _('Executable:')
imageOptionsExtract = _('Extract image:')
imageOptionsStartTerminal = _('Start in terminal:')

askConfirmDeleting = _('Deleting an appimage file is not reversible')
extractingImage = _("Extracting image")


# ----- ERRORS ----- #

okButton = "Ok"

noExePermissionSubtitle = _("The app has no executable permissions")
noExePermissionTitle = _("Permission denied")

folderAlreadyExistsSubtitle = _(' alredy exists')
folderAlreadyExistsTitle = _('Folder already exists')

invalidAppRunSubTitle = _("Selected file must be named 'AppRun'")
invalidAppRunTitle = _("AppRun file not valid")

invalidAppFolderSubtitle = _("The Application folder does not contain the selected executable file")
invalidAppFolderTitle = _("Application folder does not contain executable")

invalidExeTitle = _('does not exists')
invalidExeSubtitle = _("could not copy the exe file")

invalidIconTitle = _("does't exist")
invalidIconSubtitle = _("could not copy icon")

invalidIconSizeSubtitle = _("The icon size must be 32x32, 48x48 etc.. not")
invalidIconSizeTitle = _("Icon size not valid")

invalidLibraryTitle = _("could not copy library")
invalidLibrarySubtitle = _("Library does not exist")