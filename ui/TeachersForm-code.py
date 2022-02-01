# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import os


## *!* ## Dabo Code ID: dButton-dPanel-601
def onHit(self, evt):
    # New button
    self.Form.addTeacher()



## *!* ## Dabo Code ID: dForm-top
def addTeacher(self):
    try:
    	self.new()
    	dlg = dabo.ui.info('Output from save operation = ' + str(self.save()) + '.\n')
    	self.requery()
    except:
    	dabo.ui.exclaim('Uh oh, something went wrong!  Better check the log file!')


def afterInitAll(self):
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
    self.requery()


def initProperties(self):
    app = self.Application
    self.BasePrefKey = app.BasePrefKey
    self.SaveRestorePosition = True
    self.FontSize = app.PreferenceManager.getValue("fontsize")


def onChooseTeacherPicture(self, teacherRecNo):
    app = self.Application
    import wx
    import MySQLdb
    dlg = dabo.ui.uiwx.dFileDialog(parent=None, message=u'Choose the picture of this teacher', defaultPath=app.HomeDirectory, wildcard='*.*')
    if dlg.ShowModal() == wx.ID_OK:
    	picturePath = dlg.GetPath()
    	idx = picturePath.rfind(os.sep)
    	pictureName = picturePath[idx + len(os.sep):]
    	print 'picturePath = ' , picturePath
    	print 'pictureName = ' , pictureName
    	pictureFile = open(picturePath, 'rb')
    	pictureData = pictureFile.read()
    	pictureFile.close()
    	if not pictureData == '' and not pictureData == None:
    		tempCursor = self.getBizobj('Teachers').getTempCursor()
    		tempCursor.execute("update Teachers set TeacherPictureName=%s, TeacherPictureData=%s where TeacherRecNo = %s", (pictureName, pictureData, teacherRecNo))
    		self.requery()



## *!* ## Dabo Code ID: dButton-dPanel-271
def onHit(self, evt):
    # Last button
    self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-165
def onHit(self, evt):
    # Next button
    self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel-714
def onHit(self, evt):
    # First button
    self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel-429
def onHit(self, evt):
    # Delete button
    self.Form.deleteTeacher()



## *!* ## Dabo Code ID: dButton-dPanel-879
def onHit(self, evt):
    # Save button
    self.Form.save()



## *!* ## Dabo Code ID: dButton-dPanel-132
def onHit(self, evt):
    # Prior button
    self.Form.prior()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
    # Refresh button
    self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-946
def onHit(self, evt):
    # Choose Picture button
    app = self.Application
    self.Form.onChooseTeacherPicture(self.Form.PrimaryBizobj.Record.TeacherRecNo)


