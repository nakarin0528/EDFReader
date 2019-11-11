# -*- coding: utf-8 -*-

import os
import sys
import time
import pyedflib


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
