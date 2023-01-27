import os
import sys
import signal
import locale
import gettext

if __name__ == '__main__':
    import gi

    from gi.repository import Gio

    from flake import main
    sys.exit(main.main("0.0.3"))