 # Flake

<p>Very basic GTK user interface for <a href="https://github.com/AppImage/appimagekit">appimagekit</a></p> 

  <h1> Install </h1>
  
  <li><h3>AppImage:</h3>
  x86_64: <a href="https://github.com/SalaniLeo/Flake/releases/download/v0.0.3/Flake-0.0.3-x86_64.AppImage">here</a><br>
  aarch64: Coming next release...<br>
  <li><h3>Flatpak:</h3>
  flathub: <a href="https://flathub.org/apps/details/io.github.salaniLeo.flake">here</a><br>
   from flathub repo: <b>flatpak install flathub io.github.salaniLeo.flake</b>

  <h1> Documentation </h1>
   
  If you want to see what features I'll add in the future see <a href="#workingOn">what I'm working on</a>

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
   <p>The app supports AppRun files made by users, to use this option enable advanced options and enable "custom apprun".<p>
   The official docs on how to setup an AppDir folder are <a href="https://docs.appimage.org/reference/appdir.html">here</a>
   
</div>

  <h2> Options </h2>
   <li><h3> FolderMode </h3>
      <h4> using a <a href=#AppRun>custom apprun</a> is recommended if the exe file selected is not written is bash. </h4>
      
  Application folder must meet the <a href="https://docs.appimage.org/packaging-guide/manual.html#creating-an-appdir-manually">foldermode   requirements</a> for the app to work correctly.
      
   Allows users to include in the AppImage applications that require multiple files (like most ones).
   
   <b> I'll improve this option in every release, since it's still in beta </b>
   <br>

<div id='workingOn'>
  <h2>Next release updates</h2>

  <li>Library - just started
  <li>Settings - half done, adding settings to page
  <li>Credits - done
  <li>Library's create image option - waiting to finish library 
