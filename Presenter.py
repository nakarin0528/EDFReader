# -*- coding: utf-8 -*-
from Model import Model
import datetime
import pyedflib


class Presenter():
    def __init__(self, model):
        self.model = model

    def loadEDF(self, path):
        self.model.loadEDF(path)

    def getStartTime(self):
        return self.model.edf.getStartdatetime().strftime("%Y/%m/%d %H:%M:%S")

    def getEndTime(self):
        return (self.model.edf.getStartdatetime() + datetime.timedelta(seconds=int(
            self.getSignalNSumples()[0] / self.getSignalFs()[0]))).strftime("%Y/%m/%d %H:%M:%S")

    def getSignalLabels(self):
        return self.model.edf.getSignalLabels()

    def getSignalFs(self):
        return self.model.edf.getSampleFrequencies()

    def getSignalNSumples(self):
        return self.model.edf.getNSamples()

    def setOutputPath(self, path):
        self.model.outputPath = path

    def addCheckButton(self):
        self.model.isChecked.append(False)

    def changeCheckButtonState(self, index):
        self.model.isChecked[index] = not self.model.isChecked[index]

    def isChecked(self):
        return True in self.model.isChecked

    def convertToCsv(self):
        print("convert")
        checkedIndexArray = [i for i, x in enumerate(
            self.model.isChecked) if x == True]
        self.model.convert(checkedIndexArray)

    def dateTimeValidation(self, startTime, endTime):
        self.model.startTime = datetime.datetime.strptime(
            startTime, '%Y/%m/%d %H:%M:%S')
        self.model.endTime = datetime.datetime.strptime(
            endTime, '%Y/%m/%d %H:%M:%S')
        try:
            self.model.startTime = datetime.datetime.strptime(
                startTime, '%Y/%m/%d %H:%M:%S')
            self.model.endTime = datetime.datetime.strptime(
                endTime, '%Y/%m/%d %H:%M:%S')
            return True
        except ValueError:
            return False
