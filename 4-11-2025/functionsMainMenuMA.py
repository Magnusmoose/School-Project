from functionsGeneralMA import coolPrint, fileManagement

# Displays the main menu options for the user to see. I have made it easily editable so that the options that can be selected can be modified at any point
def displayMainMenu(options):
    print(fileManagement.openFileReadable("librarySystemAsciiArt.txt"))

    print("")
    for optionIndex in range(len(options)):
        coolPrint(f"    {optionIndex + 1}) {options[optionIndex]}")

# Gets an input from the user about the selection in the menu that they want to make
def inputOption(options):
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