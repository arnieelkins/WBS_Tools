# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo.lib.reportUtils as reportUtils
import os
import traceback


## *!* ## Dabo Code ID: dGrid-dPanel
def onGridMouseLeftDoubleClick(self, evt):
	# double-click on the grid
	app = self.Application
	downloadDir = app.PreferenceManager.getValue("downloaddir")
	if downloadDir == None or downloadDir == '':
		response = dabo.ui.areYouSure(message = "I do not seem to have a download directory set.  Would you like to choose one now?",
								defaultNo = False,
								cancelButton = False,
								requestUserAttention=True)
		if not response == True:
			dabo.ui.exclaim("Well, I can't download anything without having a place to write the file!")
			return()
		else:
			result = dabo.ui.getFolder()
			if result == None or result == '':
				dabo.ui.exclaim("Well, I can't download anything without having a place to write the file!")
				return()
			else:
				downloadDir = result
				app.PreferenceManager.setValue("downloaddir", downloadDir)
	if self.CurrentRow >= 0:
		self.Form.moveToRowNumber(self.CurrentRow)
		# column 4 = RecNo
		RecNo = self.getValue(self.CurrentRow, 4)
		print 'RecNo = ' + str(RecNo)
		fileName = self.getValue(self.CurrentRow, 0)
		fileData = self.getValue(self.CurrentRow, 6)
		f = downloadDir + os.sep + fileName
		print "f = " + str(f)
		try:
			handle = open(f, 'wb')
			handle.write(fileData)
			handle.close()
		except Exception, e:
			dabo.ui.exclaim("Oh No!  An exception while writing the file!  This is a Really, Really Bad Thing!\n" + str(traceback.format_exc()))
		print "f = " + str(f)
		if fileName.lower().endswith('.pdf'):
			reportUtils.previewPDF(f)
		else:
			dabo.ui.info("File " + str(fileName) + " downloaded to " + str(downloadDir))



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	if not self.StudentRecNo == -1:
		self.PrimaryBizobj.addWhere("AttachmentStudentsRecNo = %s" % self.StudentRecNo)
		print self.PrimaryBizobj.CurrentSQL
	self.requery()


def createBizobjs(self):
	app = self.Application

	attachmentsBizobj = app.biz.AttachmentsBizobj(app.dbConnection)
	self.addBizobj(attachmentsBizobj)

	contactsBizobj = app.biz.ContactsBizobj(app.dbConnection)
	self.addBizobj(contactsBizobj)
	attachmentsBizobj.addChild(contactsBizobj)

	studentsBizobj = app.biz.StudentsBizobj(app.dbConnection)
	self.addBizobj(studentsBizobj)
	attachmentsBizobj.addChild(studentsBizobj)


def getFileFromDB(self, RecNo):
	print "RecNo = " + str(RecNo)
	app = self.Application
	return f


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.StudentRecNo = -1
	self.Icon = "icons/wbs.ico"


def onDeleteAttachmentButton(self):
	app = self.Application
	if not self.AttachmentsGrid.Selection == None:
		bizObj = self.getBizobj('Attachments')
		currentRow = self.AttachmentsGrid.CurrentRow
		dataSet = self.AttachmentsGrid.DataSet
		currentRecNo = dataSet[currentRow]['AttachmentRecNo']
		bizObj.moveToRowNumber(currentRow)
		recordData = ''
		fieldNames = ['AttachmentRecNo', 'AttachmentName', 'AttachmentCreated', 'AttachmentType']
		for name in fieldNames:
			recordData = recordData + ' ' + str(dataSet[currentRow][name]) + '\n'
		response = dabo.ui.areYouSure(message = 'You are about to delete this record!\n' + recordData,
										defaultNo = True,
										cancelButton = False,
										requestUserAttention=True)
		if response == True:
			try:
				returnCode = bizObj.delete()
				if returnCode == None:
					returnCode = bizObj.save()
					if returnCode == None:
						dlg = dabo.ui.info('Delete successful!')
					else:
						dabo.ui.exclaim('returnCode from delete was not what I expected!\nreturnCode = ' + str(returnCode) + '\nPlease make a note of what you were attempting to do and the returnCode and contact the author!' + str(traceback.format_exc()))
						return()
				else:
					dabo.ui.exclaim('returnCode from save was not what I expected!\nreturnCode = ' + str(returnCode) + '\nPlease make a note of what you were attempting to do and the returnCode and contact the author!' + str(traceback.format_exc()))
					return()
				self.requery()
			except:
				dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# Delete Attachment button
	self.Form.onDeleteAttachmentButton()


