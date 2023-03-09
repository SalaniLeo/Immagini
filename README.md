<h1>Flake</h1>
<b>Library and creation tool for .AppImage files</b><br>

<h2>Install</h2>
<a href="https://beta.flathub.org/apps/io.github.salaniLeo.flake" rel="nofollow"><img src="https://flathub.org/assets/badges/flathub-badge-en.png" style="max-width: 100%;" width="200"></a>

<h1>Library</h1>

<h3>Ways to manage AppImages inside library:</h3>

<li>Rename a file
<li>Set a file executable or not
<li>Extract an appimage in a selected location
<li>Delete an AppImage from disk

<h1>Create new AppImage</h1>
 
 <h2>Create options</h2>
 <li><a href="#DeleteAppDir">Delete .AppDir after build has finished</a>
 <li><a href="#cAppRun">Include custom AppRun</a>
 <li><a href="#folderMode">Folder mode</a>
 
 <h2>Documentation</h2>
 
 <h3>Name</h3>
 The name can be whatever you like, with every character. Even spaces
 
 <div id="exe">
 <h3>Executable</h3>
 The executable file is the file you want to execute as .AppImage. <br>
 With the app default .AppRun you can only execute shell scripts. If you want to include a python script as executable you need to specify the script         runner at the top of the file. 

 Example:
 
<details>
  <summary>Python</summary>
  <div>
 
    #!/bin/python3
    
    import getpass
    user = getpass.getuser()
    print('My name is: ' + user)
 
  </div>
 </details>
 
<details>
  <summary>Bash</summary>
  <div>
 
    #!/bin/sh
    
    echo My name is:
    whoami
 
  </div>
 </details>
 
 Also, if you want to package whole folders see <a href="#folderMode">FolderMode</a>
 </div>
 
 <h3>Icon</h3>
 The Icon must respect the <a href="https://docs.appimage.org/reference/appdir.html#">AppImage icon specifications</a>.<br>
 Selected icons get put in different locations, based on the size and extension of the image.<br>
 The location of the icon is:<br><br>
 <li>For png images:
 usr/share/icons/hicolor/{image dimensions}/icon.png
 <li>For svg images:
 usr/share/icons/hicolor/scalable/icon.svg
 
 <h3>Category and Type</h3>
 To see what category and tpye you can add to your AppImage see <a href="https://specifications.freedesktop.org/menu-spec/latest/apa.html">freedesktop specifications</a> website
 
 <h2>Advanced options</h2>
 <div id="folderMode">
 <h3>Folder mode</h3>
 <b>This option is still in beta quality, so don't expect much.</b><br>
 Folder mode allow you to package folders inside an AppImage.<br>
 To package folders into an AppImage you have to select the main app executable as the app <a href="#exe">executable</a>, and then in the foldermode entry     select the app folder.<br>
 Also, it's recommended to use a <a href="#cAppRun">custom AppRun</a> if you enable this option.
 
 </div>
 
 <div id="cAppRun">
 <h3>Custom AppRun</h3>
 By enabling 'Custom AppRun' you can package in the application your own custom-made AppRun file.<br>
 it's recommended to use this option if you use folder mode.
 
 </div>
 
 
 
