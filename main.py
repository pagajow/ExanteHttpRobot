import os
from tkinter import *
from exante.ExanteApi import ExanteApi
from gui.LoginWindow import LoginWindow

if __name__ == "__main__":
    args = sys.argv
    scriptPath = os.path.dirname(os.path.abspath(__file__))

    def onLogin(api: ExanteApi):
        if api is not None:
            pass # todo: start robot and show main app window..

    if len(args) >= 3:
        eapi = ExanteApi(applicationID=args[1], accessKey=args[2])
        onLogin(eapi)
    else:
        print("Too few arguments, applicationID and accessKey are missing: {}".format(args))
        root = Tk()
        root.title("Exante login")
        loginWindow = LoginWindow(master=root, onLogin=onLogin)
        loginWindow.pack(anchor=CENTER)
        root.mainloop()
