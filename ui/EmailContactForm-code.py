# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPanel-490
def onHit(self, evt):
	# Last button
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-700
def onHit(self, evt):
	# Next button
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel-11
def onHit(self, evt):
	# Prior button
	self.Form.prior()



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	import os
	Biz = self.PrimaryBizobj
	Biz.addField("AttachmentRecNo")
	Biz.addField("AttachmentContactsRecNo")
	Biz.addField("AttachmentStudentsRecNo")
	Biz.addField("AttachmentName")
	Biz.addField("AttachmentData")
	Biz.addField("AttachmentType")
	Biz.addField("AttachmentCreated")
	Biz.addField("AttachmentSentToContact")
	Biz.addJoin("Contacts", "AttachmentContactsRecNo = ContactRecNo")
	Biz.addField("ContactFirstName")
	Biz.addField("ContactLastName")
	Biz.addWhere("AttachmentContactsRecNo = %s" % self.ContactRecNo)
	Biz.addWhere("AttachmentSentToContact is %s" % "NULL")
	Biz.requery()
	self.update()
	app = self.Application
	dir = app.tempdir
	fileList = []
	for rec in Biz.bizIterator(restorePointer = True):
		filename = Biz.Record.AttachmentName
		data = Biz.Record.AttachmentData
		fullpath = dir + os.sep + filename
		try:
			handle = open(fullpath, 'wb')
			handle.write(data)
			handle.close()
			fileList.append(fullpath)
		except Exception, e:
			dabo.ui.exclaim("Uh oh, something went BOOM!\n" + str(traceback.format_exc()))
			return()
	response = dabo.ui.areYouSure("The files have been written to " + str(app.tempdir) + ".  When you are done with them, click Yes to delete them, or you can click \
				No to leave them alone.")
	if response == True:
		for file in fileList:
			try:
				os.remove(file)
			except Exception, e:
				dabo.ui.exclaim("Uh oh, something went BOOM!\n" + str(traceback.format_exc()))
	response = dabo.ui.areYouSure("Shall I mark the records to indicate that the files have been sent?")
	if response == True:
		for rec in Biz.bizIterator():
			try:
				now = datetime.timestamp.now()
				Biz.Record.AttachmentSentToContact = now
				Biz.Record.save()
			except Exception, e:
				dabo.ui.exclaim("Uh oh, something went BOOM!\n" + str(traceback.format_exc()))
		dabo.ui.info("Ok, unless you saw an error prior to this, all the records were updated!")



def createBizobjs(self):
	app = self.Application

	attachmentsBizobj = app.biz.AttachmentsBizobj(app.dbConnection)
	self.addBizobj(attachmentsBizobj)

	contactsBizobj = app.biz.ContactsBizobj(app.dbConnection)
	self.addBizobj(contactsBizobj)
	attachmentsBizobj.addChild(contactsBizobj)


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.ContactRecNo = -1



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# First button
	self.Form.first()


