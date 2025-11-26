from functionsGeneralMA import coolPrint

# Displays the main menu options for the user to see. I have made it easily editable so that the options that can be selected can be modified at any point
def displayMainMenu():
    with open("librarySystemAsciiArt.txt", "r") as openFileReadable:
        art = openFileReadable.read()
    print(art)

    options = ["Student Login", "Librarian Login", "Quit"]

    print("")
    for optionIndex in range(len(options)):
        coolPrint(f"    {optionIndex + 1}) {options[optionIndex]}")

def inputOption():
    pass