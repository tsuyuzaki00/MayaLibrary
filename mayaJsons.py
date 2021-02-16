import pymel.core as pm
import maya.cmds as cmds
import json
import os
from collections import OrderedDict as od

class MayaJson:
    def __init__(self):
        #filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
        self.filePass = 'testScripts/jsonTest.json'

    def createFileJson(self):
        dataPath = cmds.workspace(q=True,rootDirectory=1)+'data/'
        files = os.listdir(dataPath)
        if 'json' in files:
            jsonPath = dataPath + 'json/'
        else:
            os.mkdir(dataPath + 'json')
            jsonPath = dataPath + 'json/'

        files = os.listdir(jsonPath)
        filepath = cmds.file(q=True, sn=True)
        filename = os.path.basename(filepath)
        raw_name, extension = os.path.splitext(filename)
        if raw_name in files:
            getJsons = jsonPath + raw_name + '/'
        else:
            os.mkdir(jsonPath + raw_name)
            getJsons = jsonPath + raw_name + '/'
        
        return getJsons

    def writeJson(self):
        s =  ["help_grp_mb", "guide"],{
            "parent":"gmr_chr_mb1_pxr_grp", "child":"mb1Rig"}
        
        with open(self.filePass, 'w') as f:
            json.dump(s, f, indent = 4, ensure_ascii = False)
    
    def readJson(self):
        with open(self.filePass, 'r') as f:
            roots = json.load(f)
            for root in roots:
                print(root)

    def parentJson(self, parent, child):
        s = {"parent":parent, "child":child}
        with open(self.filePass, 'w') as f:
            json.dump(s, f, indent = 4, ensure_ascii = False)

    def jointHierarchyExportJson(self):
        jsonPath = self.createFileJson()
        sels = pm.selected()
        s = []
        setNode = {}
        margeNode = {}
        timeNode = {"key":1}

        for sel in sels:
            selLists = pm.listAttr(k=True)
            for selList in selLists:
                selAttr = pm.getAttr(sel + '.' + selList)
                keyNode = {selList:round(selAttr,3)}
                setNode.update(keyNode)
                objDict = {str(sel):setNode}
            margeNode.update(objDict)
            timeNode.update(margeNode)
        s.append(timeNode)

        with open(jsonPath + 'jointHierarchy.json', 'w') as f:
        	json.dump(s, f, indent = 4, ensure_ascii = False)

    def jointHierarchyImportJson(self):
        jsonPath = self.createFileJson()
        with open(jsonPath + 'jointHierarchy.json', 'r') as f:
            roots = json.load(f)
            for root in roots:
                keys = root.keys()
                for key in keys:
                    pm.setAttr(key + ".rotateX", root[key]["rotateY"])
                    pm.setAttr(key + ".rotateY", root[key]["rotateY"])
                    pm.setAttr(key + ".rotateZ", root[key]["rotateZ"])
                #pm.setAttr('leg_L0_fk0_ctl.rotateZ', root["Character1_LeftLeg"]["rotateZ"])

