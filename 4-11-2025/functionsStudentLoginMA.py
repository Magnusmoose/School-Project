from functionsGeneralMA import coolPrint, fileManagement

#  A function that can be called in the main program whenever the student login process needs to be initiated
def wholeStudentLogin(studentData):
    displayStudentLoginMenu()
    return getUserInputIdentification(studentData)

# Prints the cool Ascii art of student login
def displayStudentLoginMenu():
    print(fileManagement.openFileReadable("asciiArt/studentLoginAsciiArt.txt"))
    print("")

# Get's and checks the user's inut to decide weather it is valid and if the page should be shown
def getUserInputIdentification(studentData):
    listOfIdentification = createListOfAllIdentication()

    coolPrint("Please enter your student ID here:")
    menuChoice = str(input()).lower()
    choiceValid = False
    matchedIdentification = None

    for identification in listOfIdentification:
        if identification == menuChoice:
            choiceValid = True
            matchedIdentification = identification

    if choiceValid != True:
        coolPrint("That is not a valid ID")
        return None

    studentObject = fileManagement.searchJsonFile("identification", studentData, matchedIdentification)
    coolPrint(f"Welcome {studentObject["name"]}")

    return studentObject

# Creates a list of all the student ID's in the system so that you can check if the ID entered is correct
def createListOfAllIdentication():
    data = fileManagement.openJsonFileReadable("studentIdentification.json")
    listOfIdentification = []

    for student in data:
        listOfIdentification.append(student["identification"])

    return listOfIdentification