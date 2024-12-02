from InquirerPy import inquirer

def mainMenu(log):
    while True:
        choice = inquirer.select(
            message="Main Menu:",
            choices=[
                "Start",
                "Settings",
                "Exit"
            ]
        ).execute()
        
        if choice == "Start":
            log.info("Starting...")
        elif choice == "Settings":
            log.info("entering settings...")
            settings(log)
        elif choice == "Exit":
            break
        
def settings(log):
    while True:
        choice = inquirer.select(
            message="Settings:",
            choices=[
                "Running as Client/Host",
                "Interface Mode",
                "Back"
            ]
        ).execute()
        
        if choice == "Running as Client/Host":
            pass
        elif choice == "Interface Mode":
            pass
        elif choice == "Back":
            break

def runCLIRuntime(runAs, log):
    log.info("running CLI as " + runAs)
    mainMenu(log)