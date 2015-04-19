# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo.ui.uiwx.gridRenderers
import wx


## *!* ## Dabo Code ID: dButton-dPanel-158
def onHit(self, evt):
	# Save button
	self.Form.save()
	self.Form.requery()


## *!* ## Dabo Code ID: dGrid-dPanel
def afterInitAll(self):
	# Attachments grid
	self.update()


## *!* ## Dabo Code ID: dButton-dPanel-152
def onHit(self, evt):
	# Refresh button
	self.Form.requery()
	self.Form.update()


## *!* ## Dabo Code ID: dButton-dPanel-660
def onHit(self, evt):
	# Select None button
	self.Form.selectNone()


## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# Select All button
	self.Form.selectAll()


## *!* ## Dabo Code ID: dButton-dPanel-246
def onHit(self, evt):
	# Mark Sent button
	self.Form.markSent()


## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	self.AttachmentGrid.getColByDataField('AttachmentSelected').CustomRendererClass = wx.grid.GridCellBoolRenderer
	self.AttachmentGrid.getColByDataField('AttachmentSelected').CustomEditorClass = wx.grid.GridCellBoolEditor
	self.AttachmentGrid.getColByDataField('AttachmentSelected').CustomEditorClass.UseStringValues('True', 'False')
	self.biz = self.getBizobj('Attachments')
	if self.ContactRecNo == -1:
		dabo.ui.exclaim("Hmm...somehow this form was opened without a valid Contact selected!")
		self.safeDestroy()
	else:
		self.biz.addWhere("AttachmentContactsRecNo = %s" % self.ContactRecNo)
	self.biz.addWhere("AttachmentType = 'Graded Lesson'")
	self.biz.addWhere("AttachmentSentToContact is NULL")
	print self.biz.CurrentSQL
	self.biz.requery()
	self.requery()
	self.update()


def createBizobjs(self):
	app = self.Application

	attachmentsBizobj = app.biz.AttachmentsBizobj(app.dbConnection)
	self.addBizobj(attachmentsBizobj)

	contactsBizobj = app.biz.ContactsBizobj(app.dbConnection)
	self.addBizobj(contactsBizobj)
	attachmentsBizobj.addChild(contactsBizobj)


def getFiles(self):
	import os
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
	dataSet = self.biz.getDataSet()
	count = 0
	fileList = []
	numberRenamed = 0
	for record in dataSet:
		print "record['AttachmentSelected'] == " + str(record['AttachmentSelected'])
		if record['AttachmentSelected'] == 'True':
			data = record['AttachmentData']
			name = record['AttachmentName']
			fullname = os.path.join(downloadDir, name)
			if os.path.isfile(fullname):
				# we have a duplicate filename
				idx = fullname.rfind('.')
				if not idx == None and not idx == 0:
					filename = fullname[0:idx]
					ext = fullname[idx + 1:]
					itsAllGood = False
					for diff in range(2, 9):
						tempname = filename + '_' + str(diff) + '.' + ext
						if not os.path.isfile(tempname):
							fullname = tempname
							outfile = open(fullname, 'wb')
							fileList.append(fullname)
							itsAllGood = True
							numberRenamed = numberRenamed + 1
							break
					if not itsAllGood:
						dabo.ui.exclaim("I tried 9 different filenames, and they were all duplicates!  I give up!")
						return()
			else:
				fileList.append(fullname)
				outfile = open(fullname, 'wb')
			outfile.write(data)
			outfile.close()
			count = count + 1
	dabo.ui.info(str(count) + " files were written to " + str(downloadDir) + '.  To do that I had to rename ' + str(numberRenamed) + ' files!')
	print fileList


def initProperties(self):
	self.ContactRecNo = -1
	self.Icon = "icons/wbs.ico"


def markSent(self):
	import datetime
	timeStamp = datetime.datetime.now()
	count = 0
	for idx in self.biz.bizIterator():
		if self.biz.Record['AttachmentSelected'] == 'True':
			self.biz.Record['AttachmentSentToContact'] = timeStamp
			self.biz.Record['AttachmentSelected'] = 'False'
			count = count + 1
	self.save()
	self.requery()
	dabo.ui.info(str(count) + " records marked as Sent")


def selectAll(self):
	for idx in self.biz.bizIterator():
		self.biz.Record['AttachmentSelected'] = 'True'
	self.update()
	totalRecords = self.biz.RowCount
	dabo.ui.info("All " + str(totalRecords) + " records marked as Selected!")


def selectNone(self):
	for idx in self.biz.bizIterator():
		self.biz.Record['AttachmentSelected'] = 'False'
	self.update()
	dabo.ui.info("Selection cleared!")


## *!* ## Dabo Code ID: dButton-dPanel-944
def onHit(self, evt):
	# Get Files button
	self.Form.getFiles()

