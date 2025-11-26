from functionsMainMenuMA import wholeMainMenu
from functionsStudentLoginMA import wholeStudentLogin
from functionsGeneralMA import fileManagement, pageSwap
from functionsStudentMenuMA import wholeStudentMenu
from time import sleep

data = fileManagement.openJsonFileReadable("programData.json")
studentData = fileManagement.openJsonFileReadable("studentIdentification.json")
quit = False

while quit == False:
	menuChoiceMade = wholeMainMenu(data)
	pageSwap()
	if menuChoiceMade == 0:
		studentObject = wholeStudentLogin(studentData)
		pageSwap()
		if studentObject != None:
			wholeStudentMenu(data, studentObject)
			pageSwap()
	elif menuChoiceMade == 1:
		pass
	else:
		quit = True