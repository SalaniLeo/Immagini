# Flake

<p> early development </p>

<p> GTK user interface for <a href="https://github.com/AppImage/appimagekit">appimagekit</a></p> 

  <h2> Documentation </h2>
  
  Flake provides a gtk user friendly interface for <a href="https://github.com/AppImage/appimagekit">appimagetool</a>, that has a terminal only interface

  This first version has only the very basic options, such as name, icon, executable etc... In the next versions i'll add all the options that <a             href="https://github.com/SalaniLeo/appimagecreator">this</a> app has but much less buggy and built excusively on gtk.

  See the <a href="https://appimage-builder.readthedocs.io/en/latest/">appimage builder</a> docs

  <h4> Appimages </h4>
  
  <h5>Only supports one file scripts/application. </h5>
    
  <p>The app builds the appimages with a default .AppRun file, that works by using the exec command to run the executable file selected, therefore you cannot run any script that is not executable by your terminal or that has specified the script executor (#!/bin/python3 - #!/bin/sh)
  
<details>
    <summary>default .apprun</summary>
  <div>
  
    #!/bin/sh 
    HERE="$(dirname "$(readlink -f "${0}")")" 
    EXEC="${HERE}/usr/bin/[selected exe]" 
    exec "${EXEC}"
    
  </div> 

</details>
  
  <h2> Usage </h2>

  Only supports one file scripts, and only 

  <h4>For now it only supports one file scripts/apps</h4>

  <h3>Types/Categories</h3>
    You can see <a href="https://specifications.freedesktop.org/menu-spec/latest/apa.html">valid types</a> and categories in the official documentation page

