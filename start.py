import sys
import importlib.util
import sys


if __name__ == '__main__':

    from gi.repository import Gio

    from flake import main
    sys.exit(main.main("0.0.3"))