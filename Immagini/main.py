import sys
from .ui.mainWindow import Immagini
import os

AppId="dev.salaniLeo.immagini"
flatpak = False

if 'FLATPAK_SANDBOX_DIR' in os.environ:
    flatpak = True


class main():
    app = Immagini(AppId,flatpak)
    app.run(sys.argv)