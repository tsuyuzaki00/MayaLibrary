import pymel.core as pm
import json
from collections import OrderedDict as od

class MayaJson:
    def __init__(self):
        #filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
        self.filePass = 'testScripts/jsonTest.json'

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
