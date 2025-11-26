from time import sleep
from json import load
from os import system

class fileManagement:
    def openJsonFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = load(openFileReadable)
        return data

    def openFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = openFileReadable.read()
        return data

    def searchJsonFile(fieldToFind, jsonData, identificationToFind):
        for studentObject in jsonData:
            if studentObject[fieldToFind].lower() == identificationToFind.lower():
                return studentObject

def coolPrint(text):
    for character in text:
        print(character, end = "")
        sleep(0.02)
    print(end = "\n")

def getInputAndValidate(options):
    coolPrint("Please make your choice here:")
    menuChoice = str(input()).lower()
    choiceValid = False
    
    while choiceValid != True:
        choiceValid = False
        for optionIndex in range(len(options)):
            if menuChoice == str(options[optionIndex].lower()) or menuChoice == str(optionIndex + 1):
                choiceValid = True
                choiceIndex = optionIndex

        if choiceValid != True:
            coolPrint("That is not a valid input please either type the number or name of the page you would like to go to:")
            menuChoice = str(input()).lower()

    return choiceIndex

def pageSwap():
    sleep(0.5)
    system("clear")