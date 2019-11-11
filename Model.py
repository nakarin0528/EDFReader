# -*- coding: utf-8 -*-

import os
import sys
import time
import pyedflib
import pandas as pd
import datetime
import numpy as np


class Model():
    def __init__(self):
        # window
        self.width = 1000
        self.height = 600

        # path
        self.filePath = ""
        self.outputPath = ""

        # edf
        self.edf = None

        self.isChecked = []  # for checkButton

    def loadEDF(self, path):
        self.edf = pyedflib.EdfReader(path)

    def setOutputPath(self, path):
        self.outputPath = path

    def convert(self, checkedIndexArray):
        for index in checkedIndexArray:
            label = self.edf.getSignalLabels()[index]
            result = [[label, "startTime", "Fs", "samples"]]
            signals = [label]
            signals.extend(self.edf.readSignal(index))
            df_signals = pd.DataFrame(signals)
            df_startTime = pd.DataFrame(
                ["startTime", self.edf.getStartdatetime()])
            df_Fs = pd.DataFrame(
                ["Fs", self.edf.getSampleFrequencies()[index]])
            df_samples = pd.DataFrame(
                ["samples", self.edf.getNSamples()[index]])

            result = pd.concat(
                [df_signals, df_startTime, df_Fs, df_samples], axis=1)
            result.to_csv(self.outputPath + '/' + label + ".csv",
                          index=False, header=False)
