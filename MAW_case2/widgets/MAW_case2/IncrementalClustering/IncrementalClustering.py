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

class OWIncrementalClustering(OWBwBWidget):
    name = "IncrementalClustering"
    description = "Minimum Python3 container with pip"
    priority = 10
    icon = getIconName(__file__,"cluster.svg")
    want_main_area = False
    docker_image_name = "uwthinklab/maw_containers_1"
    docker_image_tag = "v2"
    inputs = [("Input",str,"handleInputsInput")]
    outputs = [("Output",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    Input=pset("/data/trans_data/case2.csv")
    Output=pset("/data/trans_data/case2_output.csv")
    SpatialConstraint=pset("1.0")
    DurationConstraint=pset("0.0")
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"IncrementalClustering")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsInput(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("Input", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"Output"):
            outputValue=getattr(self,"Output")
        self.send("Output", outputValue)
