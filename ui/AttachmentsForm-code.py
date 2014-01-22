# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo.lib.reportUtils as reportUtils
import os


## *!* ## Dabo Code ID: dGrid-dPanel
def onGridMouseLeftDoubleClick(self, evt):
	# double-click on the grid
	app = self.Application
	if self.CurrentRow >= 0:
		self.Form.moveToRowNumber(self.CurrentRow)
		# column 4 = RecNo
		RecNo = self.getValue(self.CurrentRow, 4)
		print 'RecNo = ' + str(RecNo)
		fileName = self.getValue(self.CurrentRow, 0)
		fileData = self.getValue(self.CurrentRow, 6)
		f = app.tempdir + os.sep + fileName
		print "f = " + str(f)
		try:
			handle = open(f, 'wb')
			handle.write(fileData)
			handle.close()
		except Exception, e:
			dabo.ui.exclaim("Oh No!  An exception while writing the file!  This is a Really, Really Bad Thing!\n" + str(traceback.format_exc()))
		print "f = " + str(f)
		reportUtils.previewPDF(f)



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
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


