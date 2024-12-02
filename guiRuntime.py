import tkinter as tk

def createWindow():
    winodow = tk.Tk()
    winodow.title("Remote GPIO Controller")
    winodow.geometry("600x500")
    
    try:
        winodow.wm_iconphoto(False, tk.PhotoImage(file='./assets/icon.png'))
    except Exception as e:
        print("An error occurred while loading the window icon! Using default instead.")
        
    return winodow

def runGUIRuntime(runAs, log):
    log.info("launching GUI as " + runAs)
    window = createWindow()
    window.mainloop()