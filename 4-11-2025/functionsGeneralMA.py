from time import sleep
from json import load

class fileManagement:
    def openJsonFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = load(openFileReadable)
        return data

    def openFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = openFileReadable.read()
        return data

def coolPrint(text):
    for character in text:
        print(character, end = "")
        sleep(0.02)
    print(end = "\n")