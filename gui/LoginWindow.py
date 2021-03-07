from tkinter import *
from typing import Callable

from exante.ExanteApi import ExanteApi


class LoginWindow(Frame):

    def __init__(self, master: Frame, onLogin: Callable[[ExanteApi], None]):
        Frame.__init__(self, master, padx=20, pady=20)
        self.onLogin = onLogin

        # application ID entry:
        self.appIdRow = Frame(master=self, padx=4, pady=4)
        self.appIdRow.grid(row=0, column=0)

        self.appIdLabel = Label(master=self.appIdRow, anchor="w", text="Application ID:", width=20)
        self.appIdLabel.grid(row=0, column=0)

        self.appIdValue = StringVar()
        self.appIdValue.set("")
        self.appIdEntry = Entry(master=self.appIdRow, width=40, textvariable=self.appIdValue)
        self.appIdEntry.grid(row=0, column=1)

        # access key entry
        self.accessKeyRow = Frame(master=self, padx=4, pady=4)
        self.accessKeyRow.grid(row=1, column=0)

        self.accessKeyLabel = Label(master=self.accessKeyRow, anchor="w", text="Access Key:", width=20)
        self.accessKeyLabel.grid(row=0, column=0)

        self.accessKeyValue = StringVar()
        self.accessKeyValue.set("")
        self.accessKeyEntry = Entry(master=self.accessKeyRow, width=40, textvariable=self.accessKeyValue)
        self. accessKeyEntry.grid(row=0, column=1)

        # buttons:
        self.buttonRow = Frame(master=self, padx=4, pady=10)
        self.buttonRow.grid(row=2, column=0,)

        self.cancelBtn = Button(master=self.buttonRow, text="Cancel", height=1, width=10, command=self.onCancelPress, padx=10)
        self.cancelBtn.grid(row=0, column=0)

        self.loginBtn = Button(master=self.buttonRow, text="Login", height=1, width=10, command=self.onLoginPress, padx=10)
        self.loginBtn.grid(row=0, column=1)


    def onLoginPress(self):
        print("onLogin")
        aepi = ExanteApi(applicationID=self.appIdValue.get(), accessKey= self.accessKeyValue.get())
        response = aepi.checkAccount()
        if response.status_code == 200:
            self.onLogin(aepi)
            self.master.destroy()
        else:
            self.onLogin(None)

    def onCancelPress(self):
        print("onCancel")
        self.master.destroy()