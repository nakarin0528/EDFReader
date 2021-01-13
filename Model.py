# -*- coding: utf-8 -*-

import os
import sys
import time
import pyedflib
import pandas as pd
import datetime


class Model():
    def __init__(self):
        # window
        self.width = 700
        self.height = 600

        # path
        self.filePath = ""
        self.outputPath = ""

        self.edf = None

        self.isChecked = []  # for checkButton
        self.startTime = None  # for save
        self.endTime = None  # for save

    def loadEDF(self, path):
        self.edf = pyedflib.EdfReader(path)
        self.startTime = self.edf.getStartdatetime()
        self.endTime = self.startTime + datetime.timedelta(seconds=int(
            self.edf.getNSamples()[0] / self.edf.getSampleFrequencies()[0]))

    def setOutputPath(self, path):
        self.outputPath = path

    def convert(self, checkedIndexArray):
        for index in checkedIndexArray:
            label = self.edf.getSignalLabels()[index]
            fs = self.edf.getSampleFrequencies()[index]
            N = self.edf.getNSamples()[index]
            # result = [[label, "startTime", "Fs", "samples"]]
            signals = []

            diff_startTime = self.startTime - self.edf.getStartdatetime()
            diff_startTime_sec = diff_startTime.total_seconds()

            during_time = self.endTime - self.startTime
            during_time_sec = during_time.total_seconds()

            time_label = []
            during_sec = int(during_time_sec)
            
            for i in range(during_sec * fs):
                time_label.append(self.startTime +
                            datetime.timedelta(microseconds=((i / fs) * 1000000)))

            trimedSignals = self.edf.readSignal(index)[
                int(diff_startTime_sec) * N: int(during_time_sec) * N]
            signals.extend(trimedSignals)

            df_signals = pd.DataFrame({'Time': time_label, 'signal': signals}, index=None)
            df_signals.to_csv(self.outputPath + '/' + label + ".csv",
                          index=False)
            # df_Fs = pd.DataFrame(
            #     ["Fs", fs])
            # df_samples = pd.DataFrame(
            #     ["samples", N])

            # result = pd.concat(
            #     [df_signals, df_Fs, df_samples], axis=1)
            # result.to_csv(self.outputPath + '/' + label + ".csv",
            #               index=False, header=False)
