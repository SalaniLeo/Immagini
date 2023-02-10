import sys

def startApplication():
    from gi.repository import Gio

<<<<<<< Updated upstream
    from .Flake import ui
    try:
        sys.exit(ui.main("0.0.4"))  
=======
    from Flake import main
    try:
        sys.exit(main("0.0.4"))  
>>>>>>> Stashed changes
    except:
        print("Could not start the application.")
        

if __name__ == '__main__':
    startApplication()