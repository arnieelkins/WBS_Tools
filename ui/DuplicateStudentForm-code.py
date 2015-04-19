# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dGrid-dPanel
def onShow(self):
	pass



## *!* ## Dabo Code ID: dButton-dPanel-81
def onHit(self, evt):
	#No button
	self.Form.Accepted = False
	self.Form.Hide()



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	print 'self.DuplicateRecordsGrid.DataSet = ', self.DuplicateRecordsGrid.DataSet



def initProperties(self):
	app = self.Application
	self.Icon = "resources/wbs.ico"
	self.Accepted = False
	self.BasePrefKey = app.BasePrefKey
	self.SaveRestorePosition = True
	self.FontSize = app.PreferenceManager.getValue('fontsize')



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	#Yes button
	self.Form.Accepted = True
	self.Form.Hide()


