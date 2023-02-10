import sys
from .mainWindow import Flake

AppId="io.github.salaniLeo.flake"

class main():
    app = Flake(AppId)
    app.run(sys.argv)