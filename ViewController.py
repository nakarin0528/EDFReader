# -*- coding: utf-8 -*-
import os
import time
import datetime
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

        self.irow = 0
        self.pathLabel = None
        self.convertButton = None

        self.pwMain = tk.PanedWindow(self.master, orient='horizontal')
        self.pwMain.pack(expand=True, fill=tk.BOTH, side="left")

        self.pwLeft = tk.PanedWindow(
            self.pwMain, width=480, orient='vertical')
        self.pwMain.add(self.pwLeft)

        # self.pwRight = tk.PanedWindow(
        #     self.pwMain, bg='cyan', orient='vertical')
        # self.pwMain.add(self.pwRight)

        self.selectFrame = tk.Frame(self.pwLeft, width=480)
        self.pwLeft.add(self.selectFrame)
        label = tk.Label(self.selectFrame, text="select EDF file: ")
        label.grid(row=self.irow, column=0, padx=0, pady=0)
        button = tk.Button(
            self.selectFrame,
            text="load",
            command=self.loadEDF)
        button.grid(row=self.irow, column=1, padx=0, pady=0)
        self.irow += 1

    def showDialog(self, mode):
        fTyp = [("", "*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        if mode == 'file':
            filePath = tk.filedialog.askopenfilename(
                filetypes=fTyp, initialdir=iDir)
            return filePath
        else:
            dirPath = tk.filedialog.askdirectory(initialdir=iDir)
            return dirPath

    def loadEDF(self):
        filePath = self.showDialog(mode='file')
        self.presenter.loadEDF(filePath)
        self.showAllInfo(self.selectFrame)
        self.showOutputSetting(self.selectFrame)

    def changeCheckButtonState(self, n):
        self.presenter.changeCheckButtonState(n)

        isEnable = self.presenter.isChecked() and self.pathLabel['text'] != ''
        self.convertButton['state'] = tk.NORMAL if isEnable else tk.DISABLED

    def setOutputPath(self):
        dir = self.showDialog(mode='dir')
        self.presenter.setOutputPath(dir)
        self.pathLabel["text"] = dir

        isEnable = self.presenter.isChecked() and self.pathLabel['text'] != ''
        self.convertButton['state'] = tk.NORMAL if isEnable else tk.DISABLED

    def convertToCsv(self):
        if self.presenter.isChecked():
            self.presenter.convertToCsv()
        else:
            print("error")

    def showAllInfo(self, fm):
        signalLabels = self.presenter.getSignalLabels()
        signalFs = self.presenter.getSignalFs()
        signalNs = self.presenter.getSignalNSumples()
        N = len(signalLabels)
        startTime = self.presenter.getStartTime()
        endTime = self.presenter.getEndTime()

        # start and end time labels
        startLabel = tk.Label(
            fm, text="start: " + startTime.strftime("%Y/%m/%d %H:%M:%S"))
        startLabel.grid(row=self.irow, column=0, padx=1, pady=0)
        self.irow += 1
        endLabel = tk.Label(fm, text="end: " +
                            endTime.strftime("%Y/%m/%d %H:%M:%S"))
        endLabel.grid(row=self.irow, column=0, padx=1, pady=0)
        self.irow += 1

        # signal table
        canvas = tkinter.Canvas(fm, width=480,
                                height=400)
        canvas.grid(row=self.irow, rowspan=N, column=0, columnspan=4)

        scrollBar = ttk.Scrollbar(fm, orient=tk.VERTICAL)
        scrollBar.grid(row=self.irow, rowspan=N, column=4, sticky='ns')
        scrollBar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollBar.set)

        scHeight = (150 / 6 * (N + 1))
        canvas.config(scrollregion=(0, 0, 480, scHeight))

        tableFrame = tk.Frame(canvas, bd=2, relief='ridge')
        canvas.create_window((0, 0), window=tableFrame,
                             anchor=tk.NW, width=canvas.cget('width'))

        e0 = tk.Label(tableFrame, width=5, text='select')
        e0.grid(row=self.irow, column=0, padx=0, pady=0, ipady=0)

        e1 = tk.Label(tableFrame, width=20, text="signal label")
        e1.grid(row=self.irow, column=1, padx=0, pady=0, ipady=0)

        e2 = tk.Label(tableFrame, width=10, text="sampling rate")
        e2.grid(row=self.irow, column=2, padx=0, pady=0, ipady=0)

        e3 = tk.Label(tableFrame, width=15, text="number of samples")
        e3.grid(row=self.irow, column=3, padx=0, pady=0, ipady=0)
        self.irow += 1

        for i in range(N):
            color = None
            if i % 2 == 0:
                color = '#cdfff7'
            else:
                color = 'white'

            # checkbox
            bln = tk.BooleanVar()
            bln.set(False)
            c = tk.Checkbutton(
                tableFrame,
                variable=bln,
                width=5,
                background=color,
                command=lambda n=i: self.changeCheckButtonState(n))
            c.grid(row=self.irow, column=0, padx=0, pady=0, ipady=0)
            self.presenter.addCheckButton()

            # signal labels
            b1 = tk.Label(tableFrame, width=20,
                          text=signalLabels[i], background=color)
            b1.grid(row=self.irow, column=1, padx=0, pady=0, ipady=0)

            # sampling Fs
            b2 = tk.Label(tableFrame, width=10,
                          text=signalFs[i], background=color)
            b2.grid(row=self.irow, column=2, padx=0, pady=0, ipady=0)

            # sampling N
            b3 = tk.Label(tableFrame, width=15,
                          text=signalNs[i], background=color)
            b3.grid(row=self.irow, column=3, padx=0, pady=0, ipady=0)

            self.irow += 1

    def showOutputSetting(self, fm):

        frame = fm
        outputLabel = tk.Label(frame, text="output path: ", width=10)
        outputLabel.grid(row=self.irow, column=0, padx=1, pady=0)
        self.pathLabel = tk.Label(frame, text="")
        self.pathLabel.grid(row=self.irow, column=1, padx=1, pady=0)
        foldarButton = tk.Button(
            frame,
            text="foldar",
            command=self.setOutputPath)
        foldarButton.grid(row=self.irow, column=2, padx=0, pady=0)
        self.irow += 1

        self.convertButton = tk.Button(
            frame,
            text="convert",
            command=self.convertToCsv
        )
        self.convertButton.grid(row=self.irow, column=2, padx=0, pady=0)
        self.convertButton['state'] = tk.DISABLED
