import maya.cmds as cmds
import os

class AutoFile():
    def __init__(self, mayaName):
        self.mayaName = mayaName
        self.filePath = cmds.file(q=True, sn=True)
        self.fileDir = os.path.dirname(self.filePath)

    def animEXFile(self, deleteLists = [], parentList = []):
        cmds.file(rename = self.fileDir + '/' + self.mayaName)
        for deleteList in deleteLists:
	        cmds.delete(deleteList)
        cmds.parent(parentList["child"], parentList["parent"])
        cmds.file(save=True, type='mayaAscii', force=True)

    def filePass(self):
        filePath = cmds.file(q=True, sn=True)
        sceneName = os.path.splitext(os.path.basename(filePath))[0]
        folderPass = cmds.workspace(q=True,rootDirectory=1)+'data/json/' + sceneName + '/autoFiles_getScene.json';
        return folderPass