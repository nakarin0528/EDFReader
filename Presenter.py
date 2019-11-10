# -*- coding: utf-8 -*-
from Model import Model
import pyedflib


class Presenter():
    def __init__(self, model):
        self.model = model

    def loadEDF(self, path):
        self.model.loadEDF(path)

    def getSignalLabels(self):
        return self.model.edf.getSignalLabels()

    def getSignalFs(self):
        return self.model.edf.getSampleFrequencies()

    def getSignalNSumples(self):
        return self.model.edf.getNSamples()
