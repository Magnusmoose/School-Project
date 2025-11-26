from functionsGeneralMA import coolPrint, fileManagement, getInputAndValidate

# A function that can be called in the main program whenever the main menu process needs to be initiated
def wholeMainMenu(data):
    displayMainMenu(data["mainMenuOptions"])
    return getInputAndValidate(data["mainMenuOptions"])

# Displays the main menu options for the user to see. I have made it easily editable so that the options that can be selected can be modified at any point
def displayMainMenu(options):
    print(fileManagement.openFileReadable("asciiArt/librarySystemAsciiArt.txt"))

    print("")
    for optionIndex in range(len(options)):
        coolPrint(f"    {optionIndex + 1}) {options[optionIndex]}")