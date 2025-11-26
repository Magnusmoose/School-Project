from functionsMainMenuMA import displayMainMenu, inputOption
from functionsGeneralMA import fileManagement

data = fileManagement.openJsonFileReadable("programData.json")

displayMainMenu(data["options"])
print(inputOption(data["options"]))