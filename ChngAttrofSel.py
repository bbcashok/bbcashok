#ChngAttrofSel.py
import maya.cmds as cmds
import functools

def createUI(pWindowTitle, pApplyCallback):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI(windowID)
        
    cmds.window(windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True)
    
    cmds.rowColumnLayout(numberOfRows = 2)
    
    
    
    cmds.text(label = 'Type the Arrtibute to change for the selection and its value')
   
    
    cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,125),(2,100),(3,80)], columnOffset=[(1,'right',3)])
    

    

   
    
    cmds.text(label = 'Attribute:')
    
    targetAttributeField = cmds.textField(text = '.aiRenderCurve')
    
    cmds.separator (h=10, style='none')
    
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
   
    
    cmds.text(label = 'Value:')
    
    valueField = cmds.intField(value = 1)
     
    cmds.separator (h=10, style='none')
    
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    
    
    cmds.button(label = 'Apply', command=functools.partial(pApplyCallback,
                                                            targetAttributeField, valueField))
    
   
    
    
    def cancelCallback(*pArgs):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI(windowID)
    
    cmds.button(label = 'Cancel', command = cancelCallback)
    cmds.separator (h=10, style='none')
    
   
    cmds.rowColumnLayout(numberOfRows = 3)
    cmds.text(label = 'Developed by', align='left')
    cmds.text(label = 'B Ashok', align='left')
    cmds.text(label = 'bbcashok@gmail.com', align='left')
    cmds.showWindow()    
    

def applyCallback( pTargetAttributeField, pvalueField, *pArgs):
    
    print 'Apply button pressed.'
    
    val = cmds.intField(pvalueField, query=True, value=True)
    targetAttribute = cmds.textField(pTargetAttributeField, query =True, text = True)
    
   
    print val
    print targetAttribute
    selectobjs = cmds.ls( dag=True, ap=True, sl=True )
    print selectobjs
    noObjs = len(selectobjs)
    print noObjs
    for i in range (0 , noObjs):
        print selectobjs[i] + targetAttribute
        setname = selectobjs[i] + targetAttribute
        print setname 
        cmds.setAttr(setname, val)
        
    
    
    
createUI('My Title', applyCallback)    
    
