 # Flake

<p> early development </p>

<p> GTK user interface for <a href="https://github.com/AppImage/appimagekit">appimagekit</a></p> 

  <h1> Documentation </h1>

  See the <a href="https://appimage-builder.readthedocs.io/en/latest/">appimage builder</a> docs for all the info about AppImages

  <h2> Appimages </h2>
  
   <h3>App generated .AppDir</h3>
   <b>This is without any option activated so result may vary</b><br>
   The .AppDir folder contains:<br><br>
<ul>
  <li>the bin folder where the executable file/script/app is</li>
  <li> <a href=#.Desktop>Desktop file</a></li>
  <li> <a href=#Icon>Icon</a></li>
  <li> <a href=#AppRun>AppRun</a></li>
</ul> 

<div id=".Desktop">
 <h2>Desktop file</h2>
The app creates a Desktop entry for you automatically when building the .AppDir folder. To see the content click...
<details>
  <summary>...here</summary><div>
  
    [Desktop Entry]
    Name=Flake
    Exec=Flake-v0.0.1-x86_64.AppImage (which is picked from the /usr/bin folder inside the .AppImage)
    Icon=Icon.svg
    Type=Application
    Categories=Utility
    
</div></details></li>
 </div>


<div id="Icon">
 <h2>Icon</h2>
 <p>The icon is used in thumbnails, and should be in a standard size like 128x128 or 256x256 pixels.</p>
</div>

<div id="AppRun">
 <h2>AppRun</h2>
 <li><h3>Default AppRun</h3>
 <h4>Only supports one file scripts/application. </h4>

  <p>The app creates a default AppRun file in case a custom one is not provided, if you want to see what's inside...
  <details><summary>...click me</summary>
  <div>
  
    #!/bin/sh 
    HERE="$(dirname "$(readlink -f "${0}")")" 
    EXEC="${HERE}/usr/bin/[selected exe]" 
    exec "${EXEC}"
    
  </div></details>
  
   <li><h3>Custom AppRun</h3>
   <p>The app supports AppRun files made by you, to use this option enable advanced options and enable "custom apprun".<p>
   The official docs on how to setup an AppDir folder are <a href="https://docs.appimage.org/reference/appdir.html">here</a>
   
</div>
