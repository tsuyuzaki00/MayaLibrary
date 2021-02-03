import pymel.core as pm
import sys
import os
sys.path.append(os.path.abspath(".."))
from MayaLibrary import getNameSplit as gns

'''
#choiceNode create = 
'camera'
'polyCube'
'polyBall'
'polyCylinder'
'polyPlane'
'imagePlane'
'spotLight'
'pointLight'
'directionalLight'
'ambientLight'
'spaceLocator'
'ikHandle'
'''

def choiceNode(create = '', name = ''):
    if create == 'camera':
        sel = pm.camera(n = name)
        renameNode(sel = sel[0])
    elif create == 'polyCube':
        sel = pm.polyCube(n = name)
        renameNode(sel = sel[0])
    elif create == 'polyBall':
        sel = pm.polyCube(n = name)
        pm.polySmooth(dv = 2)
        renameNode(sel = sel[0])
    elif create == 'polyCylinder':
        sel = pm.polyCylinder(sc = 2 ,sa = 16, n = name)
        renameNode(sel = sel[0])
    elif create == 'polyPlane':
        sel = pm.polyPlane(w = 10, h = 10, n = name)
        renameNode(sel = sel[0])
    elif create == 'imagePlane':
        sel = pm.imagePlane(n = name)
        renameNode(sel = sel[0])
    elif create == 'spotLight':
        shape = pm.spotLight(n = name)
        sel = pm.listRelatives(shape, p = True)
        renameNode(sel = sel[0])
    elif create == 'pointLight':
        shape = pm.pointLight(n = name)
        sel = pm.listRelatives(shape, p = True)
        renameNode(sel = sel[0])
    elif create == 'directionalLight':
        shape = pm.directionalLight(n = name)
        sel = pm.listRelatives(shape, p = True)
        renameNode(sel = sel[0])
    elif create == 'ambientLight':
        shape = pm.ambientLight(n = name)
        sel = pm.listRelatives(shape, p = True)
        renameNode(sel = sel[0])
    elif create == 'spaceLocator':
        sel = pm.spaceLocator(n = name)
        renameNode(sel = sel[0])
    elif create == 'nullNode' or create == 'transform':
        sel = pm.createNode('transform', n = name)
        renameNode(sel = sel)
    elif create == 'joint':
        pass
    elif create == 'ikHandle':
        sel = pm.selected()
        ikHand = pm.ikHandle(sj = sel[0], ee = sel[1], n = name)
        test = pm.rename(ikHand[1], name)
        renameNode(sel = ikHand[0])
        renameNode(sel = test)

def renameNode(sel):
    scene = gns.scene()
    num = '1'.zfill(2)
    node = gns.node(sel)
    obj = gns.obj(sel)
    pos = gns.pos(sel)
        
    pm.rename(sel, '_'.join( [pos, obj, node, scene, num] ))

