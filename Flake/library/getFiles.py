import pathlib
from .getContent import getInfo

def getFiles(list, loc):
    return getImages(list, loc)

class getImages(list):
    def __init__(self, list, loc):

        size = 0
        i = 0
        self.appimages = 0
        self.file_name = ""

        for x in list:
            file = pathlib.Path(list[i-1])
            i += 1
            size += 1
            self.file_extension = file.suffix
            if(self.file_extension == ".AppImage"):
                self.file_name = file.name
                self.appimages += 1
                getInfo(str(loc) + '/' + str(file))


