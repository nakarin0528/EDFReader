# -*- coding: utf-8 -*-
import tkinter as tk
from Model import Model
from ViewController import ViewController


class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width) + "x" + str(self.model.height))
        master.title("EDFReader")
        # master.resizable(0, 0)

        self.view = ViewController(master, self.model)
