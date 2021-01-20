import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import getNameSplit as gns

def createNodes(create = '', name = ''):
    scene = gns.scene()
    num = '1'.zfill(2)
    if create == 'camera':
        sel = pm.camera( n = '_'.join( ['C', name,'cam', scene, num]))

        node = gns.node(sel[0])
        obj = gns.obj(sel[0])
        pos = gns.pos(sel[0])
        
        pm.rename(sel[0], '_'.join( [pos, obj, node, scene, num] ))

createNodes(create = 'camera', name = 'cut')
   