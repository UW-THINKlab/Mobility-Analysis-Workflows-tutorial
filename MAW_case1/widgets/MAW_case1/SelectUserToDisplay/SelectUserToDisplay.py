import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWSelectUserToDisplay(OWBwBWidget):
    name = "SelectUserToDisplay"
    description = "None"
    priority = 10
    icon = getIconName(__file__,"counting.svg")
    want_main_area = False
    docker_image_name = "uwthinklab/maw_visualization"
    docker_image_tag = "v1"
    inputs = [("input_data_path",str,"handleInputsinput_data_path"),("output_data_path",str,"handleInputsoutput_data_path"),("user_name",str,"handleInputsuser_name")]
    outputs = [("Output",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    input_data_path=pset("/data/trans_data/case1.csv")
    output_data_path=pset("/data/trans_data/case1_output.csv")
    user_name=pset("284aa3b586cce58e13a3a9cef9b33fa1b1e7fc8e422faa52e126ad7b3ccc767b")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"SelectUserToDisplay")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsinput_data_path(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("input_data_path", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutput_data_path(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("output_data_path", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsuser_name(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("user_name", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"Output"):
            outputValue=getattr(self,"Output")
        self.send("Output", outputValue)
