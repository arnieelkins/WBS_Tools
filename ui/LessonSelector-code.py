# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dCheckBox-dPanel-479
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-739
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-947
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-418
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-233
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-875
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-133
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-868
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-336
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-828
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
			newForm.CenterOnParent()
			newForm.show()
			newForm.safeDestroy()
	self.Form.safeDestroy()



## *!* ## Dabo Code ID: dCheckBox-dPanel-837
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
							self.TIGN50QCheckBox,
							self.GHS50QCheckBox,
							self.KJ50QCheckBox,
							self.BWS50QCheckBox,
							self.FOG50QCheckBox,
							self.LLL50QCheckBox,
							]


def initProperties(self):
	self.Icon = "icons/wbs.ico"


def onClose(self, evt):
	self.saveSizeAndPosition()



## *!* ## Dabo Code ID: dCheckBox-dPanel-635
def onHit(self, evt):
	self.Form.ProcessCheckBoxes(evt)


