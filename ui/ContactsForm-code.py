# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.
import traceback

## *!* ## Dabo Code ID: dButton-dPanel-204
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel-718
def onHit(self, evt):
	# Delete button
	self.Form.deleteContact()



## *!* ## Dabo Code ID: dButton-dPanel-266
def onHit(self, evt):
	# Last button
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-492
def onHit(self, evt):
	# New button
	self.Form.addContact()



## *!* ## Dabo Code ID: dButton-dPanel-89
def onHit(self, evt):
	# Next button
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# Refresh button
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-2
def onHit(self, evt):
	# Prior button
	self.Form.prior()



## *!* ## Dabo Code ID: dButton-dPanel-773
def onHit(self, evt):
	# Save button
	self.Form.save()



## *!* ## Dabo Code ID: dForm-top
def addContact(self):
	try:
		self.new()
		dlg = dabo.ui.info('Output from save operation = ' + str(self.save()) + '.\n')
		self.requery()
	except:
		dabo.ui.exclaim('Uh oh, something went wrong!  Better check the log file!  ' + str(traceback.format_exc()))

def afterInitAll(self):
	self.requery()


def createBizobjs(self):
	app = self.Application

	contactsBizobj = app.biz.ContactsBizobj(app.dbConnection)
	self.addBizobj(contactsBizobj)


def deleteContact(self):
	app = self.Application
	bizObj = self.PrimaryBizobj
	currentRecord = bizObj.Record
	fields = ['ContactRecNo', 'ContactFirstName', 'ContactLastName']
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
	self.SaveRestorePosition = True
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue("fontsize")
	self.Icon = "icons/wbs.ico"

