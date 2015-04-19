# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo.ui
from dabo.ui.uiwx.dDialog import dOkCancelDialog
import wx
from wxPython.lib import colourdb
import traceback
import datetime
import os


## *!* ## Dabo Code ID: dButton-dPanel-183
def onHit(self, evt):
	#clearoutput button
	app = self.Application
	self.Form.clearHeaderOutBox()
	self.Form.clearMissedOutBox()
	self.Form.clearCommentOutBox()



## *!* ## Dabo Code ID: dButton-dPanel-606
def onHit(self, evt):
	# Save button
	app = self.Application
	self.Form.saveCurrentGradeRecord()
	self.Form.savePDF()
	self.Form.safeDestroy()



## *!* ## Dabo Code ID: dButton-dPanel-347
def onHit(self, evt):
	# Score button
	app = self.Application
	self.Form.scoreLesson()



## *!* ## Dabo Code ID: dCheckBox-dPanel
def onHit(self, evt):
	# Failed checkbox
	app = self.Application
	self.Form.onFailedCheckBox()



## *!* ## Dabo Code ID: dCheckBox-dPanel-554
def onHit(self, evt):
	# Incomplete checkbox
	self.Form.onIncompleteCheckBox()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	#resetform button
	self.Form.onResetButton()



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	import wx
	app = self.Application
	# self.lessonShortName is set by the LessonSelector form when calling GradingForm
	# look up the record number and the full name in the database
	tempCursor = self.getBizobj('Lessons').getTempCursor("select LessonName from Lessons where LessonShortName = %s", (self.lessonShortName,))
	self.lessonFullName = tempCursor.Record.LessonName
	tempCursor = self.getBizobj('Lessons').getTempCursor("select LessonRecNo from Lessons where LessonShortName = %s", (self.lessonShortName,))
	self.lessonRecNo = tempCursor.Record.LessonRecNo
	self.OutputLabel.Caption = self.lessonShortName + ' Output'
	self.Caption = self.lessonShortName + ' Grading Form'
	self.OutputScrollPanel.Sizer.remove(self.HeaderOutBox, destroy=True)
	self.OutputScrollPanel.Sizer.remove(self.MissedOutBox, destroy=True)
	self.OutputScrollPanel.Sizer.remove(self.CommentOutBox, destroy=True)
	self.HeaderOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel, RegID = "HeaderOutBox", Height=140)
	self.HeaderOutBox.ReadOnly=True
	self.MissedOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel)
	self.MissedOutBox.ReadOnly=True
	self.CommentOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel)
	self.CommentOutBox._addWindowStyleFlag(wx.WANTS_CHARS|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
	self.OutputScrollPanel.Sizer.prepend(self.CommentOutBox, proportion=4, layout='expand', border=2)
	self.OutputScrollPanel.Sizer.prepend(self.MissedOutBox, proportion=1, layout='expand', border=2)
	self.OutputScrollPanel.Sizer.prepend(self.HeaderOutBox, proportion=0, layout='expand', border=2)
	# getAnswerData needs the lesson number to look up the answer data
	(self.answerDataSet, totalQuestions) = self.getAnswerData(self.lessonRecNo, self.getBizobj('Answers'))
	# TIGNa is lessonRecNo 8, which is a copy of lessonRecNo 3 with different question numbers
	# once we get the data with the right question numbers, we need to update the info to act
	# as if it is just the normal TIGN data
	if self.lessonRecNo == 8:
		self.lessonRecNo = 3
		self.lessonShortName = 'TIGN'
		self.lessonFullName = 'This Is Good News'
		self.OutputLabel.Caption = self.lessonShortName + ' Output'
		for record in self.answerDataSet:
			record['AnswerLessonsRecNo'] = 3
	#print self.answerDataSet
	self.AnswerPanel.Freeze()
	self.answerCheckBoxList = self.buildBoxes(self.answerDataSet, self.AnswerPanel, self.testMode)
	self.AnswerPanel.Thaw()
	self.PrimaryBizobj.addWhere("StudentRecNo = " + str(self.StudentRecNo))
	self.requery()
	studentRecord = self.PrimaryBizobj.Record
	# now we have the info we need to initialize the gradeRecord
	self.gradeRecord = {'studentRecNo':self.StudentRecNo,
						'currentDate':datetime.date.today(),
						'lessonShortName':self.lessonShortName,
						'lessonFullName':self.lessonFullName,
						'studentFullName':studentRecord['StudentFullName'],
						'studentFirstName':studentRecord['StudentFirstName'],
						'teacherFullName':studentRecord['TeacherFullName'],
						'teacherFirstName':studentRecord['TeacherFirstName'],
						'contactFullName':studentRecord['ContactFullName'],
						'contactFirstName':studentRecord['ContactFirstName'],
						'studentID':studentRecord['StudentID'],
						'totalQuestions':totalQuestions,
						'numberCorrect':-1,
						'numberMissed':-1,
						'grade':-1,
						'missedList':[],
						'commentString':'',
						'commentList':[],
						}
	self.refresh()


def buildBoxes(self, answerData, AnswerPanel, testMode):
	colordb = wx.TheColourDatabase
	print "buildBoxes is running\n"
	answerCheckBoxList = []
	checkBoxSizer = AnswerPanel.Sizer
	checkBoxSizer.clear(destroy=True)
	rowNum = 0
	lessonStartNumber = 1
	for item in answerData:
		questionNumber = item['AnswerQuestionNo']
		if '-' in questionNumber:
			index = questionNumber.find('-')
			lessonNumber = int(questionNumber[:index])
			if lessonNumber > lessonStartNumber:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
				lessonStartNumber = lessonNumber
		else:
			lessonNumber = int(questionNumber)
			if lessonNumber == 11:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 21:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 31:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 41:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 51:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 61:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 71:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 81:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
			elif lessonNumber == 91:
				checkBoxSizer.appendSpacer(10)
				rowNum = rowNum + 1
		questionNumberLabel = wx.StaticText(AnswerPanel, wx.ID_ANY, str(questionNumber) + ')')
		checkBoxSizer.append(questionNumberLabel, row=rowNum, col=0, halign='left')
		#checkBoxSizer.setItemProps(questionNumberLabel, {'ColExpand': True, 'BorderSides': ['All'], 'ColSpan': 1, 'Proportion': 0, 'HAlign': 'Center', 'RowSpan': 1, 'VAlign': 'Middle', 'Border': 8, 'Expand': False, 'RowExpand': False})
		CheckBoxA = wx.CheckBox(AnswerPanel, wx.ID_ANY, 'A')
		checkBoxSizer.append(CheckBoxA, row=rowNum, col=1)
		CheckBoxB = wx.CheckBox(AnswerPanel, wx.ID_ANY, 'B')
		checkBoxSizer.append(CheckBoxB, row=rowNum, col=2)
		CheckBoxC = wx.CheckBox(AnswerPanel, wx.ID_ANY, 'C')
		checkBoxSizer.append(CheckBoxC, row=rowNum, col=3)
		CheckBoxNA = wx.CheckBox(AnswerPanel, wx.ID_ANY, 'NA')
		checkBoxSizer.append(CheckBoxNA, row=rowNum, col=4)
		if testMode:
			if item['AnswerCorrectAnswer'] == 'A':
				CheckBoxA.SetForegroundColour('green')
				CheckBoxA.Refresh()
			else:
				CheckBoxA.SetForegroundColour('black')
				CheckBoxA.Refresh()
			if item['AnswerCorrectAnswer'] == 'B':
				CheckBoxB.SetForegroundColour('green')
				CheckBoxB.Refresh()
			else:
				CheckBoxB.SetForegroundColour('black')
				CheckBoxB.Refresh()
			if item['AnswerCorrectAnswer'] == 'C':
				CheckBoxC.SetForegroundColour('green')
				CheckBoxC.Refresh()
			else:
				CheckBoxC.SetForegroundColour('black')
				CheckBoxC.Refresh()
			CheckBoxNA.SetForegroundColour('black')
			CheckBoxNA.Refresh()
		else:
			CheckBoxA.SetForegroundColour('black')
			CheckBoxA.Refresh()
			CheckBoxB.SetForegroundColour('black')
			CheckBoxB.Refresh()
			CheckBoxC.SetForegroundColour('black')
			CheckBoxC.Refresh()
			CheckBoxNA.SetForegroundColour('black')
			CheckBoxNA.Refresh()
		answerCheckBoxList.append({'questionNumber': questionNumber,
									'questionNumberLabel':questionNumberLabel,
									'A': CheckBoxA,
									'B': CheckBoxB,
									'C': CheckBoxC,
									'NA': CheckBoxNA,
									})
		rowNum = rowNum + 1
	#dabo.ui.info("CheckBoxes created!")
	checkBoxSizer.layout()
	checkBoxSizer.FitInside(AnswerPanel)
	#dabo.ui.info("CheckBox layout complete!")
	return(answerCheckBoxList)


def buildPDFGradeReport(self):
	print "buildPDFGradeReport is running\n"
	app = self.Application
	# self.PDFHeaders is a list of lists of 3 strings
	self.PDFHeaders = []
	if self.gradeRecord['studentID'] != None and self.gradeRecord['studentID'] != '':
		self.PDFHeaders.append([str(self.gradeRecord['currentDate']), self.gradeRecord['lessonFullName'], 'StudentID: ' + self.gradeRecord['studentID']])
	else:
		self.PDFHeaders.append([str(self.gradeRecord['currentDate']), self.gradeRecord['lessonFullName'], ''])
	self.PDFHeaders.append(['Student:', self.gradeRecord['studentFullName'], ''])
	self.PDFHeaders.append(['Teacher:', self.gradeRecord['teacherFullName'], ''])
	self.PDFHeaders.append(['Contact:', self.gradeRecord['contactFullName'], ''])
	if self.IncompleteCheckBox.Value == True:
		self.PDFHeaders.append(['Score:', 'Incomplete', ''])
	else:
		self.PDFHeaders.append(['Score:', str(int(self.gradeRecord['grade'])) + '%', ''])
	# self.PDFMissed is a list of lists of 3 strings
	self.PDFMissed = []
	if self.gradeRecord['numberMissed'] == 0 or self.IncompleteCheckBox.Value == True:
		# lesson was Incomplete, do not add any lines
		pass
	else:
		self.PDFMissed.append(["Question\nmissed", "Your\nanswer", "Correct\nanswer"])
		for line in self.gradeRecord['missedList']:
			self.PDFMissed.append(line)
	# self.PDFComments is a list of strings, which will be reportlab paragraphs
	self.PDFComments = self.CommentOutBox.Value.splitlines(False)


def buildScreenGradeReport(self):
	print "buildGradeReport is running\n"
	app = self.Application
	self.headerLines = []
	self.headerLines.append('<b>' + str(self.gradeRecord['currentDate']) + '\t' + self.gradeRecord['lessonFullName'] + '</b>\n')
	tempString = 'Student:\t<b>' + self.gradeRecord['studentFullName'] + '</b>'
	# if there is no StudentID, skip that line
	if self.gradeRecord['studentID'] != '' and self.gradeRecord['studentID'] != None:
		tempString = tempString + '\tStudent ID:\t<b>' + self.gradeRecord['studentID'] + '</b>'
	self.headerLines.append(tempString + '\n')
	self.headerLines.append('Teacher:\t<b>' + self.gradeRecord['teacherFullName'] + '</b>\n')
	self.headerLines.append('Contact:\t<b>' + self.gradeRecord['contactFullName'] + '</b>\n')
	if self.IncompleteCheckBox.Value == True:
		self.headerLines.append('Score:\t<b>Incomplete</b>')
	else:
		self.headerLines.append('Score:\t<b>' + str(int(self.gradeRecord['grade'])) + '%</b>')
	self.missedLines = []
	if not self.gradeRecord['numberMissed'] == 0 and not self.gradeRecord['numberMissed'] == -1:
		self.missedLines.append("<b>Question missed\tYour answer\tCorrect answer</b>\n")
		for line in self.gradeRecord['missedList']:
			self.missedLines.append('<b>' + line[0] + '\t' + line[1] + '\t' + line[2] + '</b>\n')
	self.commentLines = []
	if ' ' in self.gradeRecord['studentFirstName']:
		index = self.gradeRecord['studentFirstName'].find(' ')
		shortFirstName = self.gradeRecord['studentFirstName'][0:index]
	else:
		shortFirstName = self.gradeRecord['studentFirstName']
	self.commentLines.append('Dear ' + shortFirstName + ',\n\n')
	for line in self.gradeRecord['commentList']:
		self.commentLines.append(line + '\n\n')
	teacherFirst = self.gradeRecord['teacherFirstName']
	if '&' in teacherFirst:
		self.commentLines.append('Your study helpers,\n')
		teacherFirst = teacherFirst.replace("&", "and")
	else:
		self.commentLines.append('Your study helper,\n')
	self.commentLines.append(teacherFirst)


def clearAnswerCheckBoxes(self):
	app = self.Application
	for line in self.answerCheckBoxList:
		# self.answerCheckBoxList contains a list of dictionary objects
		# each row has 4 checkboxes and a label
		line['A'].Value = False
		line['B'].Value = False
		line['C'].Value = False
		line['NA'].Value = False
	self.refresh()


def clearCommentOutBox(self):
	app = self.Application
	self.CommentOutBox.Clear()
	self.CommentOutBox.refresh()


def clearHeaderOutBox(self):
	app = self.Application
	self.HeaderOutBox.Clear()
	self.HeaderOutBox.refresh()


def clearMissedOutBox(self):
	app = self.Application
	self.MissedOutBox.Clear()
	self.MissedOutBox.refresh()


def createBizobjs(self):
	app = self.Application

	studentsBizobj = app.biz.StudentsBizobj(app.dbConnection)
	self.addBizobj(studentsBizobj)

	answersBizobj = app.biz.AnswersBizobj(app.dbConnection)
	self.addBizobj(answersBizobj)

	gradesBizobj = app.biz.GradesBizobj(app.dbConnection)
	self.addBizobj(gradesBizobj)

	lessonsBizobj = app.biz.LessonsBizobj(app.dbConnection)
	self.addBizobj(lessonsBizobj)

	teachersBizobj = app.biz.TeachersBizobj(app.dbConnection)
	self.addBizobj(teachersBizobj)

	attachmentsBizobj = app.biz.AttachmentsBizobj(app.dbConnection)
	self.addBizobj(attachmentsBizobj)


def displayOutput(self):
	app = self.Application
	print "displayOutput is running\n"
	self.HeaderOutBox.Clear()
	self.HeaderOutBox.refresh()
	self.MissedOutBox.Clear()
	self.MissedOutBox.refresh()
	self.CommentOutBox.Clear()
	self.CommentOutBox.refresh()
	# output all lines, starting and ending Bold as needed
	self.outputLines(self.headerLines, self.HeaderOutBox)
	if not self.FailedCheckBox.Value and not self.IncompleteCheckBox.Value:
		self.outputLines(self.missedLines, self.MissedOutBox)
	self.outputLines(self.commentLines, self.CommentOutBox)


def getAnswerData(self, lessonNumber, bizObj):
	print "getAnswerData is running\n"
	tempCursor = bizObj.getTempCursor()
	sqlString = 'SELECT * from Answers where AnswerLessonsRecNo = ' + str(lessonNumber)
	tempCursor.UserSQL = sqlString
	tempCursor.requery()
	totalQuestions = len(tempCursor.getDataSet())
	return(tempCursor.getDataSet(), totalQuestions)


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.SaveRestorePosition = True
	self.FontSize = app.PreferenceManager.getValue('fontsize')
	self.RegID = 'GradingForm'
	# testMode colors the correct answers green
	self.testMode = True
	self.lessonScored = False
	self.commentsSelected = False
	#self.Centered = True
	self.Icon = "icons/wbs.ico"


def onClose(self, evt):
	import os
	import glob
	app = self.Application
	cwd = os.getcwd()
	os.chdir(app.TempDir)
	for name in glob.iglob('*.pdf'):
		try:
			if os.path.isfile(name):
				os.remove(name)
			else:
				dabo.ui.exclaim("file " + str(name) + " not found??!?!")
		except:
			dabo.ui.exclaim('Something went wrong trying to delete a temporary file called ' + str(name) + '.' + str(traceback.print_exc()))
	os.chdir(cwd)


def onFailedCheckBox(self):
	if self.FailedCheckBox.Value == True:
		if self.IncompleteCheckBox.Value == True:
			self.IncompleteCheckBox.Value = False
			self.IncompleteCheckBox.raiseEvent(dabo.dEvents.Hit)
		self.EnterGradeSpinner.Enabled = True
		self.EnterGradeSpinner.setFocus()
	else:
		self.EnterGradeSpinner.Enabled = False


def onIncompleteCheckBox(self):
	if self.IncompleteCheckBox.Value == True:
		if self.FailedCheckBox.Value == True:
			self.FailedCheckBox.Value = False
			self.FailedCheckBox.raiseEvent(dabo.dEvents.Hit)


def onResetButton(self):
	self.clearAnswerCheckBoxes()
	self.clearHeaderOutBox()
	self.clearMissedOutBox()
	self.clearCommentOutBox()
	if self.IncompleteCheckBox.Value == True:
		self.IncompleteCheckBox.Value = False
	if self.FailedCheckBox.Value == True:
		self.FailedCheckBox.Value = False
		self.EnterGradeSpinner.Enabled = False


def onUpdate_HeaderOutBox(self, evt):
	print "onUpdate_HeaderOutBox is running to scroll the header TextBox to the end\n"
	self.scrollToEnd()


def openCommentSelectorForm(self):
	app = self.Application
	print 'self.Form = ' + str(self.Form)
	newForm = app.ui.CommentSelectorForm(self.Form, Modal=True)
	print "self.gradeRecord start"
	print self.gradeRecord
	print "self.gradeRecord end"
	newForm.TextTags = ({'<ContactFullName>':self.gradeRecord['contactFullName'],
						'<NumberOfQuestionsMissed>':str(self.gradeRecord['totalQuestions'] - self.gradeRecord['numberCorrect']),
						'<ContactFirstName>':self.gradeRecord['contactFirstName']})
	newForm.lessonShortName = self.gradeRecord['lessonShortName']
	newForm.buildCommentDictList(self.PrimaryBizobj)
	newForm.SaveRestorePosition = True
	if self.FailedCheckBox.Value == True:
		newForm.FailedCheckBox.Value = True
	if self.IncompleteCheckBox.Value == True:
		newForm.IncompleteCheckBox.Value = True
	newForm.CenterOnParent()
	newForm.show()
	if newForm.Accepted:
		#get our value, then destroy the form
		self.gradeRecord['commentList'] = []
		self.gradeRecord['commentString'] = newForm.ActiveCommentTextBox.getActiveCommentString()
		for char in self.gradeRecord['commentString']:
			print 'char = ' + str(char) + '\n'
			for dict in newForm.ActiveCommentDict:
				print "dict['letter'] = " + str(dict['letter'])
				if char == dict['letter']:
					self.gradeRecord['commentList'].append(dict['control'].Value)
					break
		if newForm.FailedCheckBox.Value == True:
			self.FailedCheckBox.Value = True
		elif newForm.IncompleteCheckBox.Value == True:
			self.IncompleteCheckBox.Value = True
		self.buildScreenGradeReport()
		self.displayOutput()
	newForm.safeDestroy()


def outputLines(self, Lines, OutputBox):
	print Lines
	for line in Lines:
		# Two newlines in a row can cause this function to skip one of them.  Insert a space
		# to make sure that does not happen.
		line = line.replace('\n\n', '\n \n')
		line = line.replace('<sp>', ' ')
		countBold = line.count('<b>')
		if countBold > 0:
			for count in range(0, countBold):
				startBold = line.find('<b>')
				# found <b> in the output line, indicating a bolded word
				if startBold >= 0:
					endBold = line.find('</b>')
					if startBold >= 1:
						# do not perform WriteText if the line starts with a <b>, as this
						# will output an extra newline.  As long as there is anything else
						# before the tag, output that part before you continue.
						OutputBox.WriteText(line[0:startBold])
					OutputBox.BeginBold()
					OutputBox.WriteText(line[startBold + 3:endBold])
					OutputBox.EndBold()
					line = line[endBold + 4:]
		OutputBox.WriteText(line)


def saveAttachment(self, filePath, studentRecNo, contactRecNo):
	app = self.Application
	(pathOnly, attachmentName) = os.path.split(filePath)
	timeStamp = datetime.datetime.now()
	try:
		bizobj = self.getBizobj('Attachments')
		bizobj.new()
		bizobj.Record.AttachmentStudentsRecNo = studentRecNo
		bizobj.Record.AttachmentContactsRecNo = contactRecNo
		bizobj.Record.AttachmentName = attachmentName
		handle = open(filePath, 'rb')
		bizobj.Record.AttachmentData = handle.read()
		handle.close()
		bizobj.Record.AttachmentCreated = timeStamp
		bizobj.Record.AttachmentType = 2
		result = bizobj.save()
		if result == True or result == None:
			dabo.ui.info("Attachment saved successfully!")
		else:
			dabo.ui.exclaim("Uh oh, something went wrong!")
	except Exception, e:
		dabo.ui.exclaim("Hey, something went wrong!\n" + str(traceback.format_exc()))
		dabo.ui.exclaim(bizobj.Record.AttachmentType)


def saveCurrentGradeRecord(self):
	app = self.Application
	import datetime
	now = datetime.date.today()
	print 'attempting to save grade record\n'
	print self.PrimaryBizobj.Record
	self.saveGradeRecord(studentsRecNo = self.PrimaryBizobj.Record["StudentRecNo"],
						currentDate = now,
						lessonRecNo = self.lessonRecNo,
						score = self.gradeRecord['grade'],
						comments = self.gradeRecord['commentString'])


def saveGradeRecord(self, studentsRecNo, currentDate, lessonRecNo, score, comments):
	app = self.Application
	# Grading forms call this method to save a grade record to the database
	bizObj = self.getBizobj('Grades')
	# Need to check the database for a prior record for the same lesson
	# If one is found, inform the user and ask whether to update it, in case they chose the wrong
	# lesson.  If the user wants to update it, update the existing record.
	# If there is no existing record, create a new one.
	try:
		tempCursor = bizObj.getTempCursor('select count(*) as count from Grades where GradeStudentsRecNo = %s and GradeLessonsRecNo = %s', (studentsRecNo, lessonRecNo))
		numberOfRecords = tempCursor.Record.count
		if numberOfRecords > 1:
			dlg = dabo.ui.exclaim('Something is terribly wrong!\nThere are more than one grade records for this lesson!\nCall someone quick!')
			return()
		elif numberOfRecords == 1:
			bizObj.execute("""select * from Grades where GradeStudentsRecNo = %s and GradeLessonsRecNo = %s""", (studentsRecNo, lessonRecNo))
			message = 'A record for this lesson exists:'
			message = message + ' ' + str(bizObj.Record.GradeLessonsRecNo) + '\n'
			message = message + ' ' + str(bizObj.Record.GradeDateGraded) + '\n'
			message = message + ' ' + str(bizObj.Record.GradeScore) + '\n'
			message = message + ' ' + str(bizObj.Record.GradeComments) + '\n'
			message = message + 'Do you want to overwrite the existing record?\n'
			dlg = dabo.ui.areYouSure(message, cancelButton=False)
			if dlg == True:
				# here we need to update the record
				try:
					bizObj.Record.GradeDateGraded = currentDate
					bizObj.Record.GradeLessonsRecNo = lessonRecNo
					bizObj.Record.GradeScore = int(score)
					bizObj.Record.GradeComments = comments
					returnCode = bizObj.save()
					if returnCode == None:
						dabo.ui.info('Update successful!')
					else:
						dabo.ui.exclaim('Unexpected returnCode = ' + str(returnCode) + ' from save operation!')
					self.requery()
					return()
				except:
					dlg = dabo.ui.exclaim("Oh my! Something has gone wrong!")
			else:
				# what do we do if they say no?  Right now just return without saving
				return()
		else:
			# this runs if there is no existing record, so we create a new one
			bizObj.new()
			bizObj.setFieldVal("GradeStudentsRecNo", studentsRecNo)
			bizObj.setFieldVal("GradeDateGraded", currentDate)
			bizObj.setFieldVal("GradeLessonsRecNo", lessonRecNo)
			bizObj.setFieldVal("GradeScore", int(score))
			bizObj.setFieldVal("GradeComments", comments)
			returnCode = bizObj.save()
			if returnCode == None:
				dabo.ui.info('Grade record created successfully!')
			else:
				dabo.ui.exclaim('Unexpected returnCode = ' + str(returnCode) + ' attempting to create a new grade record!')
			self.requery()
	except:
		dlg = dabo.ui.exclaim("Oh my! Something has gone wrong!")


def savePDF(self):
	import os
	app = self.Application
	self.buildPDFGradeReport()
	print "self.gradeRecord['studentFullName'] = " + self.gradeRecord['studentFullName']
	if self.gradeRecord['studentID'] != '' and self.gradeRecord['studentID'] != None:
		# use StudentID for filename as long as one is present
		studentID = self.gradeRecord['studentID']
		grade = str(int(self.gradeRecord['grade']))
		lesson = self.gradeRecord['lessonShortName']
		fileName = app.TempDir + os.sep + studentID + '_' + lesson + '_' + grade + '.pdf'
	else:
		# if no StudentID, use last name in filename
		idx = self.gradeRecord['studentFullName'].rfind(" ")
		print 'index = ' + str(idx)
		if idx != None:
			lastName = self.gradeRecord['studentFullName'][idx + 1:]
		else:
			lastName = self.gradeRecord['studentFullName']
		grade = str(int(self.gradeRecord['grade']))
		lesson = self.gradeRecord['lessonShortName']
		fileName = app.TempDir + os.sep + lastName + '_' + lesson + '_' + grade + '.pdf'
	if os.path.exists(fileName):
		try:
			os.remove(fileName)
		except:
			dabo.ui.exclaim("Cannot delete temp file!  File " + fileName + \
							" already exists and cannot be removed!\nPerhaps you still have the file open?")
	from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate, FrameBreak, NextPageTemplate
	from reportlab.lib.styles import getSampleStyleSheet
	from reportlab.lib import colors
	from reportlab.lib.pagesizes import letter, inch
	from reportlab.platypus import Table, TableStyle, Image

	styles = getSampleStyleSheet()
	doc = BaseDocTemplate(fileName,
							pagesize=letter,
							leftMargin = .5*inch,
							rightMargin = 8*inch,
							topMargin = 10.5*inch,
							bottomMargin = .5*inch,
							allowSplitting=1,
							showBoundary=0,
							)
	# fullPageFrame is always used for a possible second page
	fullPageFrame = Frame(doc.leftMargin, doc.bottomMargin, 7.5*inch, 10*inch, id='commentpage')
	if lesson == 'Intro':
		# Intro response includes a picture of the teacher if we have one, so formatting is different
		headerFrame = Frame(doc.leftMargin, doc.topMargin-2*inch, 5.5*inch, 2*inch, id='headers')
		pictureFrame = Frame(doc.rightMargin-2*inch, doc.topMargin-2*inch, 2*inch, 2*inch, id='picture')
		# frames for 3 columns of question data
		questionFrame1 = Frame(doc.leftMargin, doc.topMargin-4.36*inch, 2.35*inch, 2.35*inch, id='col1')
		questionFrame2 = Frame(doc.leftMargin+2.50*inch, doc.topMargin-4.36*inch, 2.35*inch, 2.35*inch, id='col2')
		questionFrame3 = Frame(doc.leftMargin+5*inch, doc.topMargin-4.36*inch, 2.35*inch, 2.35*inch, id='col3')
		# frame for comment text
		commentsFrame = Frame(doc.leftMargin, doc.bottomMargin, 7.5*inch, 5.64*inch, id='comments')
		commentsFrameLarge = Frame(doc.leftMargin, doc.bottomMargin, 7.5*inch, 7.89*inch, id='commentslarge')
		if self.FailedCheckBox.Value == True or self.IncompleteCheckBox.Value == True or self.gradeRecord['grade'] == 100:
			# if the student failed, had an Incomplete, or missed none, do not leave space for answer data
			doc.addPageTemplates([PageTemplate(id='GradeReport',frames=[headerFrame, pictureFrame, commentsFrameLarge]),
								PageTemplate(id = 'CommentPage', frames=[fullPageFrame])])
		else:
			doc.addPageTemplates([PageTemplate(id='GradeReport',frames=[headerFrame, pictureFrame, questionFrame1, questionFrame2, questionFrame3, commentsFrame]),
							PageTemplate(id = 'CommentPage', frames=[fullPageFrame])])
	else:
		# we are not on an Intro lesson, so ignore the pictureFrame
		headerFrame = Frame(doc.leftMargin, doc.topMargin-1.14*inch, 5.5*inch, 1.14*inch, id='headers')
		# frames for 3 columns of question data
		questionFrame1 = Frame(doc.leftMargin, doc.topMargin-3.5*inch, 2.35*inch, 2.35*inch, id='col1')
		questionFrame2 = Frame(doc.leftMargin+2.50*inch, doc.topMargin-3.5*inch, 2.35*inch, 2.35*inch, id='col2')
		questionFrame3 = Frame(doc.leftMargin+5*inch, doc.topMargin-3.5*inch, 2.35*inch, 2.35*inch, id='col3')
		# frame for comment text
		commentsFrame = Frame(doc.leftMargin, doc.bottomMargin, 7.5*inch, 6.5*inch, id='comments')
		commentsFrameLarge = Frame(doc.leftMargin, doc.bottomMargin, 7.5*inch, 8.75*inch, id='commentslarge')
		if self.FailedCheckBox.Value == True or self.IncompleteCheckBox.Value == True or self.gradeRecord['grade'] == 100:
			# if the student failed, had an Incomplete, or missed none, do not leave space for answer data
			doc.addPageTemplates([PageTemplate(id='GradeReport',frames=[headerFrame, commentsFrameLarge]),
								PageTemplate(id = 'CommentPage', frames=[fullPageFrame])])
		else:
			doc.addPageTemplates([PageTemplate(id='GradeReport',frames=[headerFrame, questionFrame1, questionFrame2, questionFrame3, commentsFrame]),
							PageTemplate(id = 'CommentPage', frames=[fullPageFrame])])

	# container for the 'Flowable' objects
	elements = []
	 
	Hdata = self.PDFHeaders
	#print "Hdata start"
	#print Hdata
	#print "Hdata end"
	headerTable=Table(Hdata,[.75*inch, 2*inch, 1.5*inch], 14)
	headerTable.setStyle(TableStyle([('ALIGN',(0,0), (0,4),'RIGHT'),
							('FONT',(0,0), (2,0),'Helvetica-Bold'),
							('FONT',(1,0), (1,4),'Helvetica-Bold'),
							('ALIGN',(1,0), (1,4),'LEFT'),
							]))
	headerTable.hAlign = 'LEFT'
	elements.append(headerTable)
	self.tempFile = ''
	if lesson == 'Intro':
		tempCursor = self.getBizobj('Teachers').getTempCursor('Select TeacherPictureData as pic, TeacherPictureName as picname from Teachers where concat(TeacherFirstName, " ", TeacherLastName) =%s', (self.gradeRecord['teacherFullName'],))
		pic = tempCursor.Record.pic
		picname = tempCursor.Record.picname
		if picname == None or picname == '':
			self.tempFile = ''
			# no picture data, but we are on Intro, so skip the pictureFrame
			elements.append(FrameBreak())
			elements.append(FrameBreak())
		else:
			# we have picture data, so create a temporary file, create a Platypus Image, and add it to the pictureFrame
			try:
				# a Platypus Image has to read data from a file, so we have to create one
				self.tempFile = app.TempDir + os.sep + picname
				tempFileHandle = open(self.tempFile, 'wb')
				tempFileHandle.write(pic)
				tempFileHandle.close()
				im = Image(self.tempFile, 1.8*inch, 1.8*inch)
				elements.append(im)
			except Exception, e:
				dabo.ui.exclaim('Error trying to load teacher picture! ')
				dabo.ui.exclaim(traceback.format_exc())
	elements.append(NextPageTemplate('CommentPage'))
	if self.FailedCheckBox.Value == True or self.IncompleteCheckBox.Value == True or self.gradeRecord['grade'] == 100:
		# skip output of answer data
		pass
	else:
		# include answer data
		Mdata = self.PDFMissed
		if len(Mdata) == 1:
			questionTable=Table(Mdata, None, [28])
			questionTable.setStyle(TableStyle([('ALIGN',(0,0), (-1,-1),'LEFT'),
									('ALIGN',(0,1), (0,-1),'RIGHT'),
									]))
		elif len(Mdata) >=2:
			heightList = []
			heightList.append(28)
			for value in range(1, len(Mdata)):
				heightList.append(14)
			questionTable=Table(Mdata, None, heightList)
			questionTable.setStyle(TableStyle([('ALIGN',(0,0), (-1,-1),'CENTER'),
									('FONT',(0,0), (-1,-1),'Helvetica-Bold'),
									('ALIGN',(0,1), (0,-1),'RIGHT'),
									('GRID', (0,0), (-1,-1), .5, colors.black),
									]))
		questionTable.hAlign = 'LEFT'
		elements.append(questionTable)
		print "len(Mdata)=" + str(len(Mdata))
		if len(Mdata)>=22:
			elements.append(FrameBreak())
		elif len(Mdata)>=11:
			elements.append(FrameBreak())
			elements.append(FrameBreak())
		elif len(Mdata)>=1:
			elements.append(FrameBreak())
			elements.append(FrameBreak())
			elements.append(FrameBreak())
	for line in self.PDFComments:
		para = Paragraph(line, styles["BodyText"])
		elements.append(para)
	# write the document to disk
	doc.build(elements)
	tempCursor = self.getBizobj('Students')
	tempCursor.execute("select StudentContactsRecNo from Students where StudentRecNo = %s" % self.gradeRecord['studentRecNo'])
	contactRecNo = tempCursor.Record.StudentContactsRecNo
	self.saveAttachment(fileName, self.gradeRecord['studentRecNo'], contactRecNo)
	#dabo.lib.reportUtils.previewPDF(fileName)
	if os.path.isfile(self.tempFile):
		os.remove(self.tempFile)


def scoreLesson(self):
	app = self.Application
	self.HeaderOutBox.Clear()
	self.HeaderOutBox.refresh()
	self.MissedOutBox.Clear()
	self.MissedOutBox.refresh()
	self.CommentOutBox.Clear()
	self.CommentOutBox.refresh()
	if self.FailedCheckBox.Value == True:
		if int(self.EnterGradeSpinner.Value) >= 0 and int(self.EnterGradeSpinner.Value) <=100:
			self.gradeRecord['grade'] = int(self.EnterGradeSpinner.Value)
		else:
			dabo.ui.exclaim("Grade must be an integer between 0 and 100!")
			return
	else:
		if self.IncompleteCheckBox.Value == True:
			self.gradeRecord['grade'] = -1
			self.gradeRecord['numberMissed'] = -1
		else:
			if self.EnterWrongAnswersCheckBox.Value == True:
				(self.gradeRecord['numberCorrect'], self.gradeRecord['missedList']) = self.scoreWrongAnswers(self.answerCheckBoxList, self.answerDataSet)
			else:
				(self.gradeRecord['numberCorrect'], self.gradeRecord['missedList']) = self.scoreQuestions(self.answerCheckBoxList, self.answerDataSet)
			self.gradeRecord['numberMissed'] = self.gradeRecord['totalQuestions'] - self.gradeRecord['numberCorrect']
			self.gradeRecord['grade'] = ((100.0 / self.gradeRecord['totalQuestions']) * self.gradeRecord['numberCorrect'])
	self.buildScreenGradeReport()
	self.displayOutput()
	self.CommentsButton.Enabled = True
	self.CommentsButton.update()


def scoreQuestions(self, answerCheckBoxList, answerDataSet):
	print "scoreQuestions is running\n"
	numberCorrect = 0
	numberMissed = 0
	missedList = []
	for dict in answerCheckBoxList:
		questionNumber = dict['questionNumber']
		boxAValue = dict['A'].Value
		boxBValue = dict['B'].Value
		boxCValue = dict['C'].Value
		boxNAValue = dict['NA'].Value
		# for each answer from our answer key file, see if the student's answer matches
		# the answer from the file
		for item in answerDataSet:
			questionMissedDict = {}
			if item['AnswerQuestionNo'] == questionNumber:
				correctAnswer = item['AnswerCorrectAnswer']
				gotItRight = False
				if correctAnswer == 'A':
					if boxAValue == True:
						if boxBValue == False and boxCValue == False:
							gotItRight = True
						else:
							pass
					else:
						pass
				elif correctAnswer == 'B':
					if boxBValue == True:
						if boxAValue == False and boxCValue == False:
							gotItRight = True
						else:
							pass
					else:
						pass
				elif correctAnswer == 'C':
					if boxCValue == True:
						if boxAValue == False and boxBValue == False:
							gotItRight = True
						else:
							pass
					else:
						pass
				if gotItRight == True:
					numberCorrect = numberCorrect + 1
				else:
					numberMissed = numberMissed + 1
					studentAnswer = ''
					if boxNAValue == True:
						if boxAValue == False and boxBValue == False and boxCValue == False:
							studentAnswer = 'NA'
							questionMissedDict['questionNumber'] = questionNumber
							questionMissedDict['correctAnswer'] = correctAnswer
							questionMissedDict['studentAnswer'] = studentAnswer
							print 'studentAnswer is NA'
						else:
							# present error dialog if both NA and another answer are marked
							errorMessage = "You can't answer NA and something else too!\nQuestion " + questionNumber + " has NA and another answer!"
							dlg = dabo.ui.info(errorMessage)
							return(0, '')
					else:
						if boxAValue == True:
							studentAnswer = 'A'
						if boxBValue == True:
							if len(studentAnswer) > 0:
								studentAnswer = studentAnswer + ',B'
							else:
								studentAnswer = 'B'
						if boxCValue == True:
							if len(studentAnswer) > 0:
								studentAnswer = studentAnswer + ',C'
							else:
								studentAnswer = 'C'
						# when a question is missed, store the question number, the student answer,
						# and the correct answer for that question
						questionMissedDict['questionNumber'] = questionNumber
						questionMissedDict['studentAnswer'] = studentAnswer
						questionMissedDict['correctAnswer'] = correctAnswer
			if questionMissedDict.has_key('questionNumber'):
				# add the missed question info to missedList so we can reference
				# that list to build the output dataset
				missedList.append([questionMissedDict['questionNumber'], questionMissedDict['studentAnswer'], questionMissedDict['correctAnswer']])
	return(numberCorrect, missedList)


def scoreWrongAnswers(self, answerCheckBoxList, answerDataSet):
	print "scoreWrongAnswers is running\n"
	numberCorrect = 0
	numberMissed = 0
	missedList = []
	for dict in answerCheckBoxList:
		questionNumber = dict['questionNumber']
		boxAValue = dict['A'].Value
		boxBValue = dict['B'].Value
		boxCValue = dict['C'].Value
		boxNAValue = dict['NA'].Value
		# for each answer from our answer key file, see if the student's answer matches
		# the answer from the file
		for item in answerDataSet:
			questionMissedDict = {}
			if item['AnswerQuestionNo'] == questionNumber:
				correctAnswer = item['AnswerCorrectAnswer']
				if boxAValue == False and boxBValue == False and boxCValue == False and boxNAValue == False:
					# question was answered correctly by the student, thus no answer was provided
					numberCorrect = numberCorrect + 1
				else:
					# make sure the correct answer is NOT marked!  If it is, but another answer is 
					# also marked, that is OK, as it is still WRONG if you mark more than one
					numberMissed = numberMissed + 1
					studentAnswer = ''
					if boxNAValue == True:
						#student provided no answer
						if boxAValue == False and boxBValue == False and boxCValue == False:
							studentAnswer = 'NA'
							questionMissedDict['questionNumber'] = questionNumber
							questionMissedDict['correctAnswer'] = correctAnswer
							questionMissedDict['studentAnswer'] = studentAnswer
						else:
							# present error dialog if both NA and another answer are marked
							errorMessage = "You can't answer NA and something else too!\nQuestion " + questionNumber + " has NA and another answer!"
							dlg = dabo.ui.info(errorMessage)
							return(0, '')
					else:
						# one or more answers were provided, so compile a list
						if boxAValue == True:
							studentAnswer = 'A'
						if boxBValue == True:
							if len(studentAnswer) > 0:
								studentAnswer = studentAnswer + ',B'
							else:
								studentAnswer = 'B'
						if boxCValue == True:
							if len(studentAnswer) > 0:
								studentAnswer = studentAnswer + ',C'
							else:
								studentAnswer = 'C'
						if studentAnswer == correctAnswer:
							# present error dialog if the only answer marked is the correct one
							errorMessage = "Hey, you said you were entering only wrong answers!\nQuestion " + questionNumber + " has the correct answer marked!"
							dlg = dabo.ui.info(errorMessage)
							return(0, '')
						else:
							# All questions for which we have an answer should be wrong when running this function.
							# Store the question number, the student answer,and the correct answer for that question
							questionMissedDict['questionNumber'] = questionNumber
							questionMissedDict['correctAnswer'] = correctAnswer
							questionMissedDict['studentAnswer'] = studentAnswer
			if questionMissedDict.has_key('questionNumber'):
				# add the missed question info to missedList so we can reference
				# that list to build the output dataset
				missedList.append([questionMissedDict['questionNumber'], questionMissedDict['studentAnswer'], questionMissedDict['correctAnswer']])
	return(numberCorrect, missedList)



## *!* ## Dabo Code ID: dButton-dPanel-922
def onHit(self, evt):
	# Comments button
	self.Form.openCommentSelectorForm()


