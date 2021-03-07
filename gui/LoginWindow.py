from tkinter import *
from typing import Callable


class LoginWindow(Frame):

    def __init__(self, master: Frame, onLogin: Callable[[str, str, bool], None]):
        Frame.__init__(self, master)
        self.onLogin = onLogin
