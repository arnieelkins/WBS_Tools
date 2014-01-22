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
	pass



## *!* ## Dabo Code ID: dButton-dPanel-152
def onHit(self, evt):
	# Refresh button
	self.Form.requery()



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
	dir = app.tempdir
	dataSet = self.biz.getDataSet()
	count = 0
	for record in dataSet:
		if record['AttachmentSelected'] == 'True':
			data = record['AttachmentData']
			name = record['AttachmentName']
			fullname = os.path.join(dir, name)
			if os.path.isfile(fullname):
				os.remove(fullname)
			outfile = open(fullname, 'wb')
			outfile.write(data)
			outfile.close()
			count = count + 1
	dabo.ui.info(str(count) + " files were written to " + str(dir))


def initProperties(self):
	self.ContactRecNo = -1


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
	dabo.ui.info("All records marked as Selected!")


def selectNone(self):
	for idx in self.biz.bizIterator():
		self.biz.Record['AttachmentSelected'] = 'False'
	self.update()
	dabo.ui.info("Selection cleared!")


## *!* ## Dabo Code ID: dButton-dPanel-944
def onHit(self, evt):
	# Get Files button
	self.Form.getFiles()

