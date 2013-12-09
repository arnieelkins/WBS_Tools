# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPanel-477
def onHit(self, evt):
	# First button
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel-207
def onHit(self, evt):
	# Save button
	self.Form.save()



## *!* ## Dabo Code ID: dButton-dPanel-738
def onHit(self, evt):
	# Last button
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-234
def onHit(self, evt):
	# New button
	self.Form.addTeacher()



## *!* ## Dabo Code ID: dButton-dPanel-311
def onHit(self, evt):
	# Delete button
	self.Form.deleteTeacher()



## *!* ## Dabo Code ID: dButton-dPanel-124
def onHit(self, evt):
	# Next button
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# Refresh button
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-130
def onHit(self, evt):
	# Prior button
	self.Form.prior()



## *!* ## Dabo Code ID: dForm-top
def addTeacher(self):
	try:
		self.new()
		dlg = dabo.ui.info('Output from save operation = ' + str(self.save()) + '.\n')
		self.requery()
	except:
		dabo.ui.exclaim('Uh oh, something went wrong!  Better check the log file!')

def afterInitAll(self):
	SaveRestorePosition="True"
	self.requery()


def createBizobjs(self):
	app = self.Application

	teachersBizobj = app.biz.TeachersBizobj(app.dbConnection)
	self.addBizobj(teachersBizobj)


def deleteTeacher(self):
	app = self.Application
	bizObj = self.PrimaryBizobj
	currentRecord = bizObj.Record
	fields = ['TeacherRecNo', 'TeacherFirstName', 'TeacherLastName']
	tempString = ''
	for field in fields:
		tempString = tempString + str(field) + ' = ' + str(currentRecord[field]) + '\n'
	response = dabo.ui.areYouSure(message = 'You are about to delete this record!\n' + tempString,
									defaultNo = True,
									cancelButton = False,
									requestUserAttention=True)
	if response == True:
		try:
			dlg = dabo.ui.info('Output from delete operation = ' + str(bizObj.delete()) + '.\n')
			dlg = dabo.ui.info('Output from save operation = ' + str(bizObj.save()) + '.\n')
			self.requery()
		except:
			dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")


def initProperties(self):

	SaveRestorePosition="True"
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue("fontsize")




