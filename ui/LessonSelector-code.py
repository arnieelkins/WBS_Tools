# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dCheckBox-dPanel-5
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-744
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-693
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-180
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-537
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-994
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
    import os
    app = self.Application
    for box in self.Form.CheckBoxList:
    	if box.Value == True:
    		formClass = dabo.ui.createClass("ui" + os.sep + "GradingForm.cdxml")
    		# now create an instance of the form
    		newForm = formClass(self.Form, Modal=True)
    		newForm.StudentRecNo = self.Form.StudentRecNo
    		#newForm.Centered = True
    		newForm.lessonShortName = box.Caption
    		# and finally, show the new form
    		newForm.show()
    		newForm.safeDestroy()
    self.Form.safeDestroy()



## *!* ## Dabo Code ID: dCheckBox-dPanel-160
def onHit(self, evt):
    self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dForm-top
def ProcessCheckBoxes(self, event):
    for box in self.CheckBoxList:
    	if box == event.EventObject:
    		box.Value = True
    	else:
    		box.Value = False


def afterInitAll(self):
    self.CheckBoxList = [self.IntroCheckBox,
    						self.GHSCheckBox,
    						self.TIGNCheckBox,
    						self.TIGNaCheckBox,
    						self.KJCheckBox,
    						self.BWSCheckBox,
    						self.FOGCheckBox,
    						self.LLLCheckBox,
    						]


def initProperties(self):
    app = self.Application
    self.BasePrefKey = app.BasePrefKey
    self.SaveRestorePosition = True
    self.FontSize = app.PreferenceManager.getValue("fontsize")
    self.BorderResizable = False
    self.recordNumber = 1
    self.MinimumSize = (233, 381)
    self.MaximumSize = (233, 381)


def onClose(self, evt):
    self.saveSizeAndPosition()


