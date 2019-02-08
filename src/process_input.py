import sys

class ProcessInput():

    def __init__(self):
        self.startPage = ''
        self.endPage = ''


    def parse_input(self):
        argList = sys.argv

        if len(argList) == 3:
            self.startPage = self.normalize_input(sys.argv[1])
            self.endPage = self.normalize_input(sys.argv[2])
        else:
            print("Not enough arguments given")
            sys.exit()


    def normalize_input(self, inputString):

        inputNorm = inputString.lower()
        inputNorm = inputNorm.replace(" ", "_")

        return inputNorm

