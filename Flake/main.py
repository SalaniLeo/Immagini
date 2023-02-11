import sys
from .mainWindow import Flake
import os

AppId="io.github.salaniLeo.flake"

# if(os.path.exists(".flatpak-conf")):
#     flatpak = True

# print()

class main():
    app = Flake(AppId)
    app.run(sys.argv)