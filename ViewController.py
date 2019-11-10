# -*- coding: utf-8 -*-
import os
import tkinter as tk
import tkinter.ttk as ttk
from Model import Model
from Presenter import Presenter
import tkinter.filedialog


class ViewController():
    def __init__(self, master, model):
        self.master = master
        self.model = model
        self.presenter = Presenter(model)

        self.firstView(self.master)

    def firstView(self, master):
        button = tk.Button(
            master,
            text="load EDF file",
            command=self.loadEDF)
        button.grid()

    def loadEDF(self):
        fTyp = [("", "*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        filePath = tk.filedialog.askopenfilename(
            filetypes=fTyp, initialdir=iDir)
        self.presenter.loadEDF(filePath)
        self.showAllInfo()

    def showAllInfo(self):
        signalLabels = self.presenter.getSignalLabels()
        signalFs = self.presenter.getSignalFs()
        signalNs = self.presenter.getSignalNSumples()
        N = len(signalLabels)

        canvas = tkinter.Canvas(self.master, width=480, height=420)
        canvas.grid(row=1, rowspan=N, column=0, columnspan=4)

        scrollBar = ttk.Scrollbar(self.master, orient=tk.VERTICAL)
        scrollBar.grid(row=1, rowspan=N, column=4, sticky='ns')
        scrollBar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollBar.set)

        scHeight = (150 / 6 * (N + 1))
        canvas.config(scrollregion=(0, 0, 480, scHeight))

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame,
                             anchor=tk.NW, width=canvas.cget('width'))

        e0 = tk.Label(frame, width=5, text='select')
        e0.grid(row=1, column=0, padx=0, pady=0, ipady=0)

        e1 = tk.Label(frame, width=20, text="signal label")
        e1.grid(row=1, column=1, padx=0, pady=0, ipady=0)

        e2 = tk.Label(frame, width=10, text="sampling rate")
        e2.grid(row=1, column=2, padx=0, pady=0, ipady=0)

        e3 = tk.Label(frame, width=15, text="number of samples")
        e3.grid(row=1, column=3, padx=0, pady=0, ipady=0)

        for i in range(N):
            irow = i + 2
            color = None
            if i % 2 == 0:
                color = '#cdfff7'
            else:
                color = 'white'

            # checkbox
            bln = tk.BooleanVar()
            bln.set(False)
            c = tk.Checkbutton(frame, variable=bln,
                               width=5, background='white')
            c.grid(row=irow, column=0, padx=0, pady=0, ipady=0)

            # signal labels
            b1 = tk.Label(frame, width=20,
                          text=signalLabels[i], background=color)
            b1.grid(row=irow, column=1, padx=0, pady=0, ipady=0)

            # sampling Fs
            b2 = tk.Label(frame, width=10,
                          text=signalFs[i], background=color)
            b2.grid(row=irow, column=2, padx=0, pady=0, ipady=0)

            # sampling N
            b3 = tk.Label(frame, width=15,
                          text=signalNs[i], background=color)
            b3.grid(row=irow, column=3, padx=0, pady=0, ipady=0)
