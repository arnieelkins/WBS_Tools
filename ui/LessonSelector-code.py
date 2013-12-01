# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dCheckBox-dPanel-668
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-222
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-645
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-662
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-89
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	import os
	app = self.Application
	for box in self.Form.CheckBoxList:
		if box.Value == True:
			formClass = dabo.ui.createClass('ui//GradingForm.cdxml')
			# now create an instance of the form
			newForm = formClass(self.Form, Modal=True)
			newForm.StudentRecNo = self.Form.StudentRecNo
			newForm.Centered = True
			newForm.lessonShortName = box.Caption
			# and finally, show the new form
			newForm.show()
			newForm.safeDestroy()
	self.Form.safeDestroy()



## *!* ## Dabo Code ID: dCheckBox-dPanel-447
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
							self.KJCheckBox,
							self.BWSCheckBox,
							self.FOGCheckBox,
							self.LLLCheckBox,
							]


def initProperties(self):
	app = self.Application
	self.SaveRestorePosition = True
	self.FontSize = app.PreferenceManager.getValue("fontsize")
	self.BorderResizable = False
	self.recordNumber = 1
	self.MinimumSize = (233, 381)
	self.MaximumSize = (233, 381)


