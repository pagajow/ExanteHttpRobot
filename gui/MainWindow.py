from tkinter import *
from exante.ApiWorker import ApiWorker
from exante.ExanteApi import ExanteApi


class MainWindow(Frame):
    def __init__(self, master: Frame, api: ExanteApi):
        Frame.__init__(self, master, padx=20, pady=20)
        self.api = api

        self.label = Label(master=self, text="API label")
        self.label.grid(row=0, column=0)
