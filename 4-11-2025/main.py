from functionsMainMenuMA import wholeMainMenu
from functionsStudentLoginMA import wholeStudentLogin
from functionsGeneralMA import fileManagement
from time import sleep

data = fileManagement.openJsonFileReadable("programData.json")
quit = False

while quit == False:
	menuChoiceMade = wholeMainMenu(data)
	sleep(0.5)
	if menuChoiceMade == 0:
		print("")
		correctInputOrNot = wholeStudentLogin()
		sleep(0.5)
		if correctInputOrNot == True:
			pass