import sys
from .mainWindow import Flake
import os

AppId="io.github.salaniLeo.flake"
flatpak = False

if 'FLATPAK_SANDBOX_DIR' in os.environ:
    flatpak = True


class main():
    app = Flake(AppId,flatpak)
    app.run(sys.argv)