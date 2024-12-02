import sys

import configuration
import guiRuntime
import cliRuntime
import logger

# setup of the logger
log = logger.setuplogger()

# initialize of application
def initApplication():
    # config file path
    configFilePath = 'config/config.json'
    
    # loading the configuration from config/config.json
    data = configuration.loadFile(configFilePath)
    
    # loading configuratino file keys to variables
    runAs = data['runAs']
    interfaceMode = data['interfaceMode']
    
    # checking if running ether as host or client
    if runAs == '':
        runAs == 'client' # default is client
    
    # checking interface mode to be ether gui or cli
    if interfaceMode == '':
        interfaceMode = 'gui' # default is gui
    elif interfaceMode == 'cli':
        runAs = 'host' # in cli only host
    
    # write pre launch information to configuration file
    configuration.writeFile(configFilePath, data)
    
    # launching in desired interface mode and as client or host
    if interfaceMode == 'gui':
        guiRuntime.runGUIRuntime(runAs, log)
    elif interfaceMode == 'cli':
        cliRuntime.runCLIRuntime(runAs, log)
        
def cleanup():
    logger.cleanup_old_logs()
    
# runs when file name is main 
if __name__ == "__main__":
    # checks if there are more arguments given then just the name
    try:
        if len(sys.argv) == 1:
            initApplication()
            cleanup()
        elif len(sys.argv) >= 2:
            log.warning("This program does not accept arguments!")
            
    
    # prints message when a keyboard interrupt occurred        
    except KeyboardInterrupt:
        log.info("Application terminated by user!")
    
    log.info("Exeting...")