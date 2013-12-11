# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPage-596
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPage-928
def onHit(self, evt):
	self.Form.prior()



## *!* ## Dabo Code ID: dButton-dPage-163
def onHit(self, evt):
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel-619
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel-498
def onHit(self, evt):
	self.Form.last()



## *!* ## Dabo Code ID: dDropdownList-dPanel
def afterInit(self):
	mybiz = self.Form.getBizobj('Contacts')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.update()


def onMouseRightDown(self, evt):
	# right-click on Contact field should open Contacts form
	self.Form.openContactsForm()
	self.afterInit()



## *!* ## Dabo Code ID: dButton-dPanel-614
def onHit(self, evt):
	self.Form.prior()



## *!* ## Dabo Code ID: dButton-dPanel-202
def onHit(self, evt):
	# Delete button
	print 'bizobj deleteChildLogic == ' + str(self.Form.PrimaryBizobj.deleteChildLogic) + '\n'
	self.Form.delete(dataSource='Students')
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-558
def onHit(self, evt):
	# Save Button
	try:
		dlg = dabo.ui.info('Output from Form.save operation = ' + str(self.Form.save()) + '.\n')
		self.Form.requery()
		self.Form.update()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")



## *!* ## Dabo Code ID: dButton-dPanel-713
def onHit(self, evt):
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPage-275
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
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")



## *!* ## Dabo Code ID: dButton-dPanel-174
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
	newForm.show()
	newForm.safeDestroy()
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPage-239
def onHit(self, evt):
	self.Form.requery()



## *!* ## Dabo Code ID: dGrid-dPage
def onGridMouseLeftDoubleClick(self, evt):
	if self.CurrentRow >= 0:
		self.Form.moveToRowNumber(self.CurrentRow)
		self.Form.StudentDataPage.showContainingPage()



## *!* ## Dabo Code ID: dButton-dPanel-759
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
			dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")
		self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPage-69
def onHit(self, evt):
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPage
def onHit(self, evt):
	# Lookup button on Lookup tab
	bizObj = self.Form.PrimaryBizobj
	#bizObj.LogEvents = ['All']
	studentID = self.Form.StudentIDText.Value
	fName = self.Form.FirstNameText.Value
	lName = self.Form.LastNameText.Value
	contact = self.Form.ContactText.Value
	teacher = self.Form.TeacherText.Value
	recNo = self.Form.StudentRecordText.Value
	phone = self.Form.PhoneText.Value
	StudentIDDict = {"field":"StudentID", "value":studentID}
	FirstNameDict = {"field":"StudentFirstName", "value":fName}
	LastNameDict = {"field":"StudentLastName", "value":lName}
	ContactDict = {"field":"ContactFirstName", "value":contact}
	TeacherDict = {"field":"TeacherFirstName", "value":teacher}
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
			whereString = tempDict["field"] + " LIKE '" + tempDict["value"] + "%'"
			bizObj.addWhere(whereString)
	self.Form.requery()
	rowCount = bizObj.RowCount
	if rowCount >= 0:
		if rowCount == 0:
			dabo.ui.exclaim('No records found with those search parameters!')
		elif rowCount == 1:
			self.Form.StudentDataPage.showContainingPage()
		elif rowCount >= 2:
			self.Form.StudentTablePage.showContainingPage()



## *!* ## Dabo Code ID: dButton-dPanel-986
def onHit(self, evt):
	# Refresh button
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPage-470
def onHit(self, evt):
	bizObj = self.Form.PrimaryBizobj
	self.Form.StudentIDText.Value = ""
	self.Form.FirstNameText.Value = ""
	self.Form.LastNameText.Value = ""
	self.Form.ContactText.Value = ""
	self.Form.TeacherText.Value = ""
	self.Form.StudentRecordText.Value = ""
	self.Form.PhoneText.Value = ""
	bizObj.setWhereClause("")
	self.Form.requery()



## *!* ## Dabo Code ID: dButton-dPanel-606
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



## *!* ## Dabo Code ID: dGrid-dPanel
def afterInitAll(self):
	SaveRestorePosition="True"
	self.RowColorOdd = "azure"
	self.RowColorEven = "whitesmoke"
	self.AlternateRowColoring = True
	#self.Columns[3].Visible = True
	#self.Columns[4].Visible = True
	self.update()


def initProperties(self):

	SaveRestorePosition="True"
	self.SelectionMode = 'Row'


def onGridCellEdited(self, evt):
	# save the grade data if the user edits anything
	try:
		dlg = dabo.ui.info('Output from Form.save operation = ' + str(self.Form.save(dataSource='Grades')) + '.\n')
		self.Form.requery()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	# New Student button
	self.Form.addStudent()



## *!* ## Dabo Code ID: dButton-dPanel-891
def onHit(self, evt):
	# Delete grade button
	self.Form.deleteGrade()



## *!* ## Dabo Code ID: dForm-top
def addStudent(self):
	try:
		self.PrimaryBizobj.setWhereClause("")
		self.requery()
		self.new()
		dlg = dabo.ui.info('Output from Form.save operation = ' + str(self.save()) + '.\n')
		self.requery()
	except:
		dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")


def afterInitAll(self):
	SaveRestorePosition="True"
	app = self.Application
	self.setTabOrder()
	self.setupMenu()
	self.Caption = self.Caption + '-- WBSTools version ' + str(app.getAppInfo('appVersion'))
	print 'attempting to set focus to Lookup tab\n'
	self.StudentLookupPage.showContainingPage()
	#self.requery()


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
				dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")


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

	SaveRestorePosition="True"
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue("fontsize")


def openContactsForm(self):
	app = self.Application
	print "\nUser asked to edit Contacts, attempting to open ContactsForm\n"
	#app.LogEvents = ['All']
	newForm = app.ui.ContactsForm(self, Modal=True)
	newForm.show()
	newForm.safeDestroy()


def openPrintForm(self):
	app = self.Application
	print "\nPrint Forms button pressed, attempting to open PrintOrPreview form\n"
	#app.LogEvents = ['All']
	newForm = app.ui.PrintOrPreviewForm(app.MainForm, Modal=True)
	newForm.bizObj = self.PrimaryBizobj
	newForm.recordNumber = self.PrimaryBizobj.Record['StudentRecNo']
	newForm.show()
	newForm.safeDestroy()


def openTeachersForm(self):
	app = self.Application
	print "\nUser asked to edit Teachers, attempting to open TeachersForm\n"
	#app.LogEvents = ['All']
	newForm = app.ui.TeachersForm(self, Modal=True)
	newForm.show()
	newForm.safeDestroy()


def setTabOrder(self):
	self.FirstNameTextBox.MoveAfterInTabOrder(self.StudentIDTextBox)
	self.LastNameTextBox.MoveAfterInTabOrder(self.FirstNameTextBox)
	self.ContactDropdownList.MoveAfterInTabOrder(self.LastNameTextBox)
	self.TeacherDropdownList.MoveAfterInTabOrder(self.ContactDropdownList)
	self.GenderDropdownList.MoveAfterInTabOrder(self.TeacherDropdownList)
	self.OccupationTextBox.MoveAfterInTabOrder(self.GenderDropdownList)
	self.ReligionTextBox.MoveAfterInTabOrder(self.OccupationTextBox)
	self.ChurchNameTextBox.MoveAfterInTabOrder(self.ReligionTextBox)
	self.AgeTextBox.MoveAfterInTabOrder(self.ChurchNameTextBox)
	self.BirthdateTextBox.MoveAfterInTabOrder(self.AgeTextBox)
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
	self.fillReportsMenu()



## *!* ## Dabo Code ID: dDropdownList-dPanel-707
def afterInit(self):
	mybiz = self.Form.getBizobj('Teachers')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.update()


def onMouseRightDown(self, evt):
	# right-click on Teacher field should open the Teachers form
	self.Form.openTeachersForm()
	self.afterInit()


