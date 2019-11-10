# -*- coding: utf-8 -*-

import os
import sys
import time
import pyedflib


class Model():
    def __init__(self):
        # window
        self.width = 500
        self.height = 480

        # path
        self.filePath = ""
        self.outputPath = ""

        # edf
        self.edf = None

    def loadEDF(self, path):
        self.edf = pyedflib.EdfReader(path)
        print(self.edf.file_info())

    def setOutputPath(self, path):
        self.outputPath = path
