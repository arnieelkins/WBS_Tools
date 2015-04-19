# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import os
import datetime
import traceback


## *!* ## Dabo Code ID: dDropdownList-dPanel-655
def onValueChanged(self, evt):
	#HasABible
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPanel-502
def onValueChanged(self, evt):
	#TypeOfBaptism
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-63
def onHit(self, evt):
	# Attachments button
	self.Form.openAttachmentsForm()



## *!* ## Dabo Code ID: dTextBox-dPanel-806
def onValueChanged(self, evt):
	#ChurchName
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel-672
def onValueChanged(self, evt):
	#Religion
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-919
def onHit(self, evt):
	# Upload button
	self.Form.onUploadButton()



## *!* ## Dabo Code ID: dButton-dPage-19
def onHit(self, evt):
	self.Form.prior()



## *!* ## Dabo Code ID: dButton-dPage-292
def onHit(self, evt):
	self.Form.last()



## *!* ## Dabo Code ID: dTextBox-dPanel-963
def onValueChanged(self, evt):
	#Phone1
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDateTextBox-dPanel
def onValueChanged(self, evt):
	#Birthdate
	self.Form.autoSave()



## *!* ## Dabo Code ID: dPage-dPageFrame
def afterInitAll(self):
	# Get Files For Contact page
	print 'clearing WHERE clause on Contacts'
	self.Form.getBizobj('Contacts').setWhereClause('')
	print 'requerying Contacts'
	self.Form.getBizobj('Contacts').requery()



## *!* ## Dabo Code ID: dDropdownList-dPanel-729
def onValueChanged(self, evt):
	#HasBeenBaptized
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPanel-467
def onValueChanged(self, evt):
	#Gender
	self.Form.autoSave()



## *!* ## Dabo Code ID: dEditBox-dPanel-112
def onValueChanged(self, evt):
	#Notes
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPanel-84
def onValueChanged(self, evt):
	#WBSBefore
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPage-625
def onHit(self, evt):
	self.Form.next()



## *!* ## Dabo Code ID: dDropdownList-dPanel
def afterInit(self):
	# StudentContactRecNo
	mybiz = self.Form.getBizobj('Contacts')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.update()


def onMouseRightDown(self, evt):
	# right-click on Contact field should open Contacts form
	self.Form.openContactsForm()
	self.afterInit()


def onValueChanged(self, evt):
	#StudentContactsRecNo
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-221
def onHit(self, evt):
	# Refresh button
	self.Form.requery()



## *!* ## Dabo Code ID: dSpinner-dPanel
def onValueChanged(self, evt):
	#Age
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel
def onValueChanged(self, evt):
	#StudentID
	self.Form.autoSave()



## *!* ## Dabo Code ID: dGrid-dPage-208
def onGridMouseLeftDoubleClick(self, evt):
	if self.CurrentRow >= 0:
		print 'self.CurrentRow = ' + str(self.CurrentRow)
		print 'self.DataSet = ' + str(self.DataSet)
		contactRecNo = self.DataSet[self.CurrentRow]['ContactRecNo']
		self.Form.openGetFilesForContactForm(contactRecNo)



## *!* ## Dabo Code ID: dButton-dPage-868
def onHit(self, evt):
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-360
def onHit(self, evt):
	# Print Forms button
	teacher = self.Form.PrimaryBizobj.Record.TeacherFullName
	if teacher == ' ' or teacher == None:
		dlg = dabo.ui.areYouSure("There is no TEACHER assigned.  Do you still want to print?", defaultNo=True, cancelButton=False, parent=self.Form)
		if dlg == False:
			return()
	contact = self.Form.PrimaryBizobj.Record.ContactFullName
	if contact == ' ' or contact == None:
		dabo.ui.exclaim("You need to assign a CONTACT before you can print a grading sheet!")
		return()
	self.Form.openPrintForm()



## *!* ## Dabo Code ID: dComboBox-dPanel
def onValueChanged(self, evt):
	#Occupation
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel-102
def onValueChanged(self, evt):
	#WBSID
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPanel-487
def onValueChanged(self, evt):
	#RequestedBaptism
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-131
def onHit(self, evt):
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-771
def onHit(self, evt):
	# Grade button
	print "\nGrade button pressed, attempting to open LessonSelector\n"
	app = self.Application
	teacher = self.Form.PrimaryBizobj.Record.TeacherFullName
	if teacher == ' ' or teacher == None:
		dabo.ui.exclaim("Hey, you have to assign a TEACHER before you can grade a lesson!")
		return()
	contact = self.Form.PrimaryBizobj.Record.ContactFullName
	if contact == ' ' or contact == None:
		dabo.ui.exclaim("Hey, you have to assign a CONTACT before you can grade a lesson!")
		return()
	newForm = app.ui.LessonSelector(app.MainForm, Modal=True)
	newForm.StudentRecNo = self.Form.PrimaryBizobj.Record['StudentRecNo']
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()
	self.Form.requery()



## *!* ## Dabo Code ID: dDropdownList-dPanel-19
def onValueChanged(self, evt):
	#MaritalStatus
	self.Form.autoSave()



## *!* ## Dabo Code ID: dEditBox-dPanel-364
def onValueChanged(self, evt):
	#PostalAddress
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel-169
def onValueChanged(self, evt):
	#City
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPage-602
def onHit(self, evt):
	try:
		returnCode = self.Form.save()
		if returnCode == None:
			dlg = dabo.ui.info('Save successful!')
		else:
			dabo.ui.exclaim('returnCode from save was not what I expected!\nreturnCode = ' + str(returnCode) + '\nPlease make a note of what you were attempting to do and the returnCode and contact the author!')
			return()
		self.Form.update()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))



## *!* ## Dabo Code ID: dButton-dPanel-904
def onHit(self, evt):
	# Add grade button
	app = self.Application
	choices = ('Intro', 'GHS', 'TIGN', 'KJ', 'BWS', 'FOG', 'LLL')
	choiceDict = {'Intro':1, 'GHS':2, 'TIGN':3, 'KJ':4, 'BWS':5, 'FOG':6, 'LLL':7}
	lesson = dabo.ui.getChoice(choices, message='Choose a lesson', caption='Choose a lesson', defaultPos=None)
	if not lesson == None:
		bizObj = self.Form.getBizobj('Grades')
		recordNumber = self.Form.PrimaryBizobj.Record['StudentRecNo']
		import datetime
		currentDate = datetime.date.today()
		bizObj.new()
		bizObj.setFieldVal("GradeStudentsRecNo", recordNumber)
		bizObj.setFieldVal("GradeDateGraded", currentDate)
		bizObj.setFieldVal("GradeLessonsRecNo", choiceDict[lesson])
		try:
			dlg = dabo.ui.info('Output from bizObj save operation = ' + str(bizObj.save()) + '.\n')
		except:
			dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))
		self.Form.requery()



## *!* ## Dabo Code ID: dTextBox-dPanel-660
def onValueChanged(self, evt):
	#StudentFirstName
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPanel-141
def afterInit(self):
	# StudentTeachersRecNo
	mybiz = self.Form.getBizobj('Teachers')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	print self.Choices, self.Keys
	self.update()


def onMouseRightDown(self, evt):
	# right-click on Teacher field should open the Teachers form
	self.Form.openTeachersForm()
	self.afterInit()


def onValueChanged(self, evt):
	#StudentTeachersRecNo
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPage
def afterInitAll(self):
	#Lookup button on lookup tab
	self.SetDefault()

def onHit(self, evt):
	# Lookup button on Lookup tab
	bizObj = self.Form.PrimaryBizobj
	#bizObj.LogEvents = ['All']
	studentID = self.Form.StudentIDText.Value
	fName = self.Form.FirstNameText.Value
	lName = self.Form.LastNameText.Value
	contact = self.Form.LookupFormContactDropdownList.Value
	teacher = self.Form.LookupFormTeacherDropdownList.Value
	recNo = self.Form.StudentRecordText.Value
	phone = self.Form.PhoneText.Value
	StudentIDDict = {"field":"StudentID", "value":studentID}
	FirstNameDict = {"field":"StudentFirstName", "value":fName}
	LastNameDict = {"field":"StudentLastName", "value":lName}
	if contact == 1:
		ContactDict = {"field":"StudentContactsRecNo", "value":None}
	else:
		ContactDict = {"field":"StudentContactsRecNo", "value":contact}
	if teacher == 1:
		TeacherDict = {"field":"StudentTeachersRecNo", "value":None}
	else:
		TeacherDict = {"field":"StudentTeachersRecNo", "value":teacher}
	RecNoDict = {"field":"StudentRecNo", "value":recNo}
	Phone1Dict = {"field":"StudentPhone1", "value":phone}
	Phone2Dict = {"field":"StudentPhone2", "value":phone}
	dictList = [StudentIDDict,
				FirstNameDict,
				LastNameDict,
				ContactDict,
				TeacherDict,
				RecNoDict,
				Phone1Dict,
				Phone2Dict,
				]
	bizObj.setWhereClause("")
	for tempDict in dictList:
		whereString = ""
		if tempDict["value"] == "" or tempDict["value"] == None:
			pass
		else:
			print type(tempDict["value"])
			if 'string' in str(type(tempDict["value"]))   or 'unicode' in str(type(tempDict["value"])):
				# If the user enters a search value, it will be a string, which is converted to lowercase
				# for the compare with 'null'.  If the user does not enter a search value, skip the compare.
				print "tempDict['value'].lower() = " + tempDict["value"].lower()
				if tempDict["value"].lower() == "null":
					whereString = "(" + tempDict["field"] + " is NULL or " + tempDict["field"] + " = '')"
				elif tempDict["field"] == "StudentContactsRecNo":
					whereString = tempDict["field"] + " = " + str(tempDict["value"])
				elif tempDict["field"] == "StudentTeachersRecNo":
					whereString = tempDict["field"] + " = " + str(tempDict["value"])
				else:
					whereString = tempDict["field"] + " LIKE '" + str(tempDict["value"]) + "%'"
			else:
				whereString = tempDict["field"] + " LIKE '" + str(tempDict["value"]) + "%'"
			print 'whereString = ' + whereString
			bizObj.addWhere(whereString)
	print bizObj.CurrentSQL
	self.Form.requery()
	rowCount = bizObj.RowCount
	if rowCount >= 0:
		if rowCount == 0:
			dabo.ui.exclaim('No records found with those search parameters!')
		elif rowCount == 1:
			self.Form.StudentDataPage.showContainingPage()
		elif rowCount >= 2:
			self.Form.StudentTablePage.showContainingPage()



## *!* ## Dabo Code ID: dButton-dPanel-376
def onHit(self, evt):
	# Delete grade button
	self.Form.deleteGrade()



## *!* ## Dabo Code ID: dTextBox-dPanel-69
def onValueChanged(self, evt):
	#State
	self.Form.autoSave()



## *!* ## Dabo Code ID: dDropdownList-dPage
def afterInit(self):
	# lookup tab
	mybiz = self.Form.getBizobj('Contacts')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.Choices.insert(0, u'null')
	self.Keys.insert(0, 0L)
	print self.Choices, self.Keys
	self.update()



## *!* ## Dabo Code ID: dGrid-dPage
def onGridMouseLeftDoubleClick(self, evt):
	if self.CurrentRow >= 0:
		self.Form.moveToRowNumber(self.CurrentRow)
		self.Form.StudentDataPage.showContainingPage()



## *!* ## Dabo Code ID: dTextBox-dPanel-959
def onValueChanged(self, evt):
	#Email
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-985
def onHit(self, evt):
	# Save Button
	try:
		dlg = dabo.ui.info('Output from Form.save operation = ' + str(self.Form.save()) + '.\n')
		self.Form.requery()
		self.Form.update()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))



## *!* ## Dabo Code ID: dButton-dPage-839
def onHit(self, evt):
	#Clear button
	bizObj = self.Form.PrimaryBizobj
	self.Form.StudentIDText.Value = ""
	self.Form.FirstNameText.Value = ""
	self.Form.LastNameText.Value = ""
	self.Form.ContactDropdownList.Value = ""
	self.Form.TeacherDropdownList.Value = ""
	self.Form.StudentRecordText.Value = ""
	self.Form.PhoneText.Value = ""
	bizObj.setWhereClause("")
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPage-191
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dEditBox-dPanel
def onValueChanged(self, evt):
	#StreetAddress
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel-561
def onValueChanged(self, evt):
	#StudentsLastName
	self.Form.autoSave()



## *!* ## Dabo Code ID: dTextBox-dPanel-185
def onValueChanged(self, evt):
	#Country
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel-367
def onHit(self, evt):
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel-466
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel-160
def onHit(self, evt):
	self.Form.prior()



## *!* ## Dabo Code ID: dGrid-dPanel
def afterInitAll(self):
	self.RowColorOdd = "azure"
	self.RowColorEven = "whitesmoke"
	self.AlternateRowColoring = True
	#self.Columns[3].Visible = True
	#self.Columns[4].Visible = True
	self.update()


def initProperties(self):
	self.SaveRestorePosition = True
	self.SelectionMode = 'Row'


def onGridCellEdited(self, evt):
	# save the grade data if the user edits anything
	try:
		dlg = dabo.ui.info('Output from Form.save operation = ' + str(self.Form.save(dataSource='Grades')) + '.\n')
		self.Form.requery()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))



## *!* ## Dabo Code ID: dButton-dPanel-165
def onHit(self, evt):
	# Delete button
	print 'bizobj deleteChildLogic == ' + str(self.Form.PrimaryBizobj.deleteChildLogic) + '\n'
	self.Form.delete(dataSource='Students')
	self.Form.requery()



## *!* ## Dabo Code ID: dDropdownList-dPage-242
def afterInit(self):
	# Lookup tab
	mybiz = self.Form.getBizobj('Teachers')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.Choices.insert(0, u'null')
	self.Keys.insert(0, 0L)
	print self.Choices, self.Keys
	self.update()



## *!* ## Dabo Code ID: dTextBox-dPanel-357
def onValueChanged(self, evt):
	#Phone2
	self.Form.autoSave()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# New Student button
	self.Form.addStudent()



## *!* ## Dabo Code ID: dForm-top
def addStudent(self):
	try:
		self.PrimaryBizobj.setWhereClause("")
		self.requery()
		self.new()
		self.autoSave()
		self.PrimaryBizobj.addWhere('StudentContactsRecNo = ' + str(self.PrimaryBizobj.Record['StudentContactsRecNo']))
		self.requery()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))


def afterInitAll(self):
	app = self.Application
	self.setTabOrder()
	self.setupMenu()
	userName = str(app.dbConnectionName).upper()
	self.Caption = self.Caption + '-- WBSTools version ' + str(app.getAppInfo('appVersion') + ' user = ' + userName)
	print 'attempting to set focus to Lookup tab\n'
	self.StudentLookupPage.showContainingPage()
	#self.requery()


def autoSave(self):
	self.save()


def createBizobjs(self):
	app = self.Application

	studentsBizobj = app.biz.StudentsBizobj(app.dbConnection)
	self.addBizobj(studentsBizobj)

	gradesBizobj = app.biz.GradesBizobj(app.dbConnection)
	self.addBizobj(gradesBizobj)
	studentsBizobj.addChild(gradesBizobj)

	contactsBizobj = app.biz.ContactsBizobj(app.dbConnection)
	self.addBizobj(contactsBizobj)
	studentsBizobj.addChild(contactsBizobj)

	teachersBizobj = app.biz.TeachersBizobj(app.dbConnection)
	self.addBizobj(teachersBizobj)
	studentsBizobj.addChild(teachersBizobj)
	
	attachmentsBizobj = app.biz.AttachmentsBizobj(app.dbConnection)
	self.addBizobj(attachmentsBizobj)
	studentsBizobj.addChild(attachmentsBizobj)

	lessonsBizobj = app.biz.LessonsBizobj(app.dbConnection)
	self.addBizobj(lessonsBizobj)

	answersBizobj = app.biz.AnswersBizobj(app.dbConnection)
	self.addBizobj(answersBizobj)


def deleteGrade(self):
	# called when the user clicks the Delete button
	app = self.Application
	if not self.GradeHistoryGrid.Selection == None:
		bizObj = self.getBizobj('Grades')
		currentRow = self.GradeHistoryGrid.CurrentRow
		dataSet = self.GradeHistoryGrid.DataSet
		currentRecNo = dataSet[currentRow]['GradeRecNo']
		bizObj.moveToRowNumber(currentRow)
		recordData = ''
		fieldNames = ['LessonShortName', 'GradeDateGraded', 'GradeScore', 'GradeComments']
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
						dabo.ui.exclaim('returnCode from delete was not what I expected!\nreturnCode = ' + str(returnCode) + '\nPlease make a note of what you were attempting to do and the returnCode and contact the author!')
						return()
				else:
					dabo.ui.exclaim('returnCode from save was not what I expected!\nreturnCode = ' + str(returnCode) + '\nPlease make a note of what you were attempting to do and the returnCode and contact the author!')
					return()
				self.requery()
			except:
				dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!" + str(traceback.format_exc()))


def fillEditPrefsMenu(self):
	from ui.MenEditPrefs import MenEditPrefs
	app = self.Application
	print "finding base_edit menu"
	editMenu = self.MenuBar.getMenu("base_edit")
	print "editMenu = " + str(editMenu)
	editMenu.prependMenu(MenEditPrefs(editMenu))


def fillFileOpenMenu(self):
	from ui.MenFileOpen import MenFileOpen
	"""Add the File|Open menu, with menu items for opening each form."""
	app = self.Application
	fileMenu = self.MenuBar.getMenu("base_file")
	fileMenu.prependMenu(MenFileOpen(fileMenu))


def fillReportsMenu(self):
	"""Add the Reports menu."""
	from dabo.dLocalize import _
	app = self.Application
	from ui.MenReports import MenReports
	menReports = MenReports()

	# We want the reports menu right after the View menu:
	idx = self.MenuBar.getMenuIndex(_("View"))
	if idx is None:
		# punt:
		idx = 2
	idx += 1
	self.MenuBar.insertMenu(idx, menReports)


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.FontSize = app.PreferenceManager.getValue("fontsize")
	self.Icon = "icons/wbs.ico"


def onUploadButton(self):
	app = self.Application
	studentBizobj = self.PrimaryBizobj
	studentRecNo = studentBizobj.Record.StudentRecNo
	contactRecNo = studentBizobj.Record.StudentContactsRecNo
	result = dabo.ui.getFile(multiple=True)
	if not result == None or result == '':
		for filePath in result:
			(pathOnly, attachmentName) = os.path.split(filePath)
			timeStamp = datetime.datetime.now()
			try:
				bizobj = self.getBizobj('Attachments')
				for rec in bizobj.bizIterator():
					print "AttachmentType = " + str(bizobj.Record.AttachmentType)
				bizobj.new()
				bizobj.Record.AttachmentStudentsRecNo = studentRecNo
				bizobj.Record.AttachmentContactsRecNo = contactRecNo
				bizobj.Record.AttachmentName = attachmentName
				handle = open(filePath, 'rb')
				bizobj.Record.AttachmentData = handle.read()
				handle.close()
				dlg = app.ui.FileTypeSelector()
				bizobj.Record.AttachmentType = 4
				bizobj.Record.AttachmentCreated = timeStamp
				result = bizobj.save()
				if result == True or result == None:
					dabo.ui.info("Attachment saved successfully!")
				else:
					dabo.ui.exclaim("Uh oh, something went wrong!")
					print bizobj.Record
			except Exception, e:
				dabo.ui.exclaim("Hey, something went wrong!\n" + str(traceback.format_exc()))


def openAttachmentsForm(self):
	app = self.Application
	biz = self.PrimaryBizobj
	formClass = app.ui.AttachmentsForm
	# now create an instance of the form
	newForm = formClass(self, Modal=True)
	newForm.StudentRecNo = biz.Record.StudentRecNo
	# and finally, show the new form
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()


def openContactsForm(self):
	app = self.Application
	print "\nUser asked to edit Contacts, attempting to open ContactsForm\n"
	#app.LogEvents = ['All']
	newForm = app.ui.ContactsForm(self, Modal=True)
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()


def openGetFilesForContactForm(self, contactRecNo):
	app = self.Application
	newForm = app.ui.GetFilesForContactForm(self, Modal=True)
	newForm.ContactRecNo = contactRecNo
	print 'opening GetFilesForContactForm with ContactRecNo of ' + str(newForm.ContactRecNo)
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()


def openPrintForm(self):
	app = self.Application
	print "\nPrint Forms button pressed, attempting to open PrintOrPreview form\n"
	#app.LogEvents = ['All']
	newForm = app.ui.PrintOrPreviewForm(app.MainForm, Modal=True)
	newForm.bizObj = self.PrimaryBizobj
	newForm.recordNumber = self.PrimaryBizobj.Record['StudentRecNo']
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()


def openTeachersForm(self):
	app = self.Application
	print "\nUser asked to edit Teachers, attempting to open TeachersForm\n"
	#app.LogEvents = ['All']
	newForm = app.ui.TeachersForm(self, Modal=True)
	newForm.CenterOnParent()
	newForm.show()
	newForm.safeDestroy()


def setTabOrder(self):
	self.FirstNameTextBox.MoveAfterInTabOrder(self.StudentIDTextBox)
	self.LastNameTextBox.MoveAfterInTabOrder(self.FirstNameTextBox)
	self.ContactDropdownList.MoveAfterInTabOrder(self.LastNameTextBox)
	self.TeacherDropdownList.MoveAfterInTabOrder(self.ContactDropdownList)
	self.GenderDropdownList.MoveAfterInTabOrder(self.TeacherDropdownList)
	self.OccupationComboBox.MoveAfterInTabOrder(self.GenderDropdownList)
	self.ReligionTextBox.MoveAfterInTabOrder(self.OccupationComboBox)
	self.ChurchNameTextBox.MoveAfterInTabOrder(self.ReligionTextBox)
	self.AgeSpinner.MoveAfterInTabOrder(self.ChurchNameTextBox)
	self.BirthdateTextBox.MoveAfterInTabOrder(self.AgeSpinner)
	self.MaritalStatusDropdownList.MoveAfterInTabOrder(self.BirthdateTextBox)
	self.HasBeenBaptizedDropdownList.MoveAfterInTabOrder(self.MaritalStatusDropdownList)
	self.TypeOfBaptismDropdownList.MoveAfterInTabOrder(self.HasBeenBaptizedDropdownList)
	self.RequestedBaptismDropdownList.MoveAfterInTabOrder(self.TypeOfBaptismDropdownList)
	self.HasBibleDropdownList.MoveAfterInTabOrder(self.RequestedBaptismDropdownList)
	self.WBSBeforeDropdownList.MoveAfterInTabOrder(self.HasBibleDropdownList)
	self.StreetAddressEditBox.MoveAfterInTabOrder(self.WBSBeforeDropdownList)
	self.PostalAddressEditBox.MoveAfterInTabOrder(self.StreetAddressEditBox)
	self.CityTextBox.MoveAfterInTabOrder(self.PostalAddressEditBox)
	self.StateTextBox.MoveAfterInTabOrder(self.CityTextBox)
	self.CountryTextBox.MoveAfterInTabOrder(self.StateTextBox)
	self.Phone1TextBox.MoveAfterInTabOrder(self.CountryTextBox)
	self.Phone2TextBox.MoveAfterInTabOrder(self.Phone1TextBox)
	self.EmailTextBox.MoveAfterInTabOrder(self.Phone2TextBox)
	self.NotesEditBox.MoveAfterInTabOrder(self.EmailTextBox)
	self.SaveButton.MoveAfterInTabOrder(self.NotesEditBox)


def setupMenu(self):
	self.fillFileOpenMenu()
	self.fillEditPrefsMenu()
	self.fillReportsMenu()


