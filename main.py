import os
import sys
from tkinter import *
from exante.ExanteApi import ExanteApi
from gui.LoginWindow import LoginWindow

if __name__ == "__main__":

    args = sys.argv
    scriptPath = os.path.dirname(os.path.abspath(__file__))


    if len(args) >= 3:
        eapi = ExanteApi(applicationID=args[1], accessKey=args[2])
        eapi.start()
    else:
        print("Too few arguments, applicationID and accessKey are missing: {}".format(args))
        root = Tk()
        root.geometry("550x450")
        root.title("Auto trader")
        LoginWindow(master=root, onLogin=lambda x, y, z: print("appid: {}, key: {}, success: {}".format(x, y, z)))
        root.mainloop()
