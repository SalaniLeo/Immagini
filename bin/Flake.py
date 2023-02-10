import sys

def startApplication():
    from gi.repository import Gio

    from Flake import main
    try:
        sys.exit(main("0.0.4"))  
    except:
        print("Could not start the application.")
        

if __name__ == '__main__':
    startApplication()