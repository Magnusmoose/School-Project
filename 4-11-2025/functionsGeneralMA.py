from time import sleep
from json import load, dump
from os import system

# A class for all my functions to do with managing, accessing and save data to and from files
class fileManagement:
    # Opens a json file and returns the data
    def openJsonFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = load(openFileReadable)
        return data

    def writeToJsonFile(fileName, data):
        with open(fileName, "w") as openFileWritable:
            dump(data, openFileWritable, indent = 4)

    # Opens a file and returns the data
    def openFileReadable(fileName):
        with open(fileName, "r") as openFileReadable:
            data = openFileReadable.read()
        return data

    # Searchs for an object within a json file with the ID
    def searchJsonFile(fieldToFind, jsonData, identificationToFind):
        for studentObject in jsonData:
            if studentObject[fieldToFind].lower() == identificationToFind.lower():
                return studentObject

# Prints the text like it is being actively typed out
def coolPrint(text):
    for character in text:
        print(character, end = "")
        sleep(0.02)
    print(end = "\n")

# Gets and validates an input that can be used in all of the menu pages
def getInputAndValidate(options, errorMessage):
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
            coolPrint(f"That is not a valid input please either type the number or name of the {errorMessage} you would like to go to:")
            menuChoice = str(input()).lower()

    return choiceIndex

# Gives a standard set of instructions for when the page swaps to a new menu
def pageSwap():
    sleep(0.5)
    system("clear")