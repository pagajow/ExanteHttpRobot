import os
from tkinter import *
from exante.ExanteApi import ExanteApi
from gui.LoginWindow import LoginWindow
from gui.MainWindow import MainWindow

if __name__ == "__main__":
    """
    args = sys.argv
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    if len(args) >= 3:
        eapi = ExanteApi(applicationID=args[1], accessKey=args[2])
    """

    root = Tk()
    root.title("Exante robot")

    def onLogin(api: ExanteApi):
        if api is not None:
            mainWindow = MainWindow(master=root, api=api)
            mainWindow.pack(anchor=CENTER)


    applicationID = None
    if os.path.isfile('app_id'):
        try:
            with open('app_id') as f:
                applicationID = f.read()
        except IOError:
            print("File app_id not accessible")
    accessKey = None
    if os.path.isfile('access_key'):
        try:
            with open('access_key') as f:
                accessKey = f.read()
        except IOError:
            print("File access_key not accessible")

    loginWindow = LoginWindow(master=root, onLogin=onLogin, applicationID=applicationID, accessKey=accessKey)
    loginWindow.pack(anchor=CENTER)
    root.mainloop()
