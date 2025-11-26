from functionsGeneralMA import coolPrint, fileManagement, getInputAndValidate, pageSwap

# A function that can be called in the main program whenever the student menu process needs to be initiated
def wholeStudentMenu(data, studentObject, booksData, studentsData):
	displayStudentMenu(studentObject, data["studentMenuOptions"])
	menuInput = getInputAndValidate(data["studentMenuOptions"], "page")
	pageSwap()
	if menuInput == 0:
		displayAvailableBooks(booksData)
	elif menuInput == 1:
		borrowABook(studentObject, booksData, studentsData)

# Displays the student  menu options for the user to see. I have made it easily editable so that the options that can be selected can be modified at any point
def displayStudentMenu(studentObject, options):
	print(fileManagement.openFileReadable("asciiArt/studentMenuAsciiArt.txt"), "\n")

	for optionIndex in range(len(options)):
	    coolPrint(f"    {optionIndex + 1}) {options[optionIndex]}")

def displayAvailableBooks(booksData):
	print(fileManagement.openFileReadable("asciiArt/browseAvailableBooksAsciiArt.txt"), "\n")
	for bookData in booksData:
		if bookData["availableCopies"] >= 1:
			coolPrint(f"{bookData["name"]} ({bookData["identification"]}):\n    - Author: {bookData["author"]}\n    - Genre: {bookData["genre"]}\n    - Available Copies: {bookData["availableCopies"]}\n")
	coolPrint("Press enter to exit")
	input()

'''def borrowABook(studentObject, booksData, studentsData):
	print(fileManagement.openFileReadable("asciiArt/borrowABookAsciiArt.txt"), "\n")
	if studentObject["numberOfBooksTakenOut"] >= 3:
		coolPrint("You have reached the maximum borrowing limit (3 books)")
	else:
		booksDataIdentifiers = []
		for bookData in booksData:
			booksDataIdentifiers.append(bookData["identification"])

		valid = False

		while valid != True
			bookIndexWanted = getInputAndValidate(booksDataIdentifiers, "book")
			if booksData[bookIndexWanted]["availableCopies"] >= 1:

		oldObject = studentObject

		booksData[bookIndexWanted]["availableCopies"] -= 1
		studentObject["booksTakenOut"].append(booksData[bookIndexWanted]["identification"])
		studentObject["numberOfBooksTakenOut"] += 1

		studentsData[studentsData.index(oldObject)] = studentObject

		fileManagement.writeToJsonFile("booksData.json", booksData)
		fileManagement.writeToJsonFile("studentIdentification.json", studentsData)'''