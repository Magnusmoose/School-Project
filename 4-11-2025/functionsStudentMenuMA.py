from functionsGeneralMA import coolPrint, fileManagement, getInputAndValidate

# A function that can be called in the main program whenever the student menu process needs to be initiated
def wholeStudentMenu(data, studentObject):
    displayStudentMenu(studentObject, data["studentMenuOptions"])
    return getInputAndValidate(data["studentMenuOptions"])

# Displays the student  menu options for the user to see. I have made it easily editable so that the options that can be selected can be modified at any point
def displayStudentMenu(studentObject, options):
	print(fileManagement.openFileReadable("asciiArt/studentMenuAsciiArt.txt"))
	print("")

	for optionIndex in range(len(options)):
	    coolPrint(f"    {optionIndex + 1}) {options[optionIndex]}")