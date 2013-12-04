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

## *!* ## Dabo Code ID: dButton-dPanel-739
def onHit(self, evt):
	# Score button
	app = self.Application
	self.Form.scoreLesson()
	self.Form.CommentsButton.Enabled = True
	self.Form.CommentsButton.update()



## *!* ## Dabo Code ID: dButton-dPanel-47
def onHit(self, evt):
	# Comments button
	self.Form.openCommentSelectorForm()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	#resetform button
	self.Form.clearAnswerCheckBoxes()
	self.Form.clearHeaderOutBox()
	self.Form.clearMissedOutBox()
	self.Form.clearCommentOutBox()



## *!* ## Dabo Code ID: dButton-dPanel-455
def onHit(self, evt):
	# SavePDF button
	app = self.Application
	self.Form.savePDF()



## *!* ## Dabo Code ID: dButton-dPanel-637
def onHit(self, evt):
	#clearoutput button
	app = self.Application
	self.Form.clearHeaderOutBox()
	self.Form.clearMissedOutBox()
	self.Form.clearCommentOutBox()



## *!* ## Dabo Code ID: dForm-top
def buildBoxes(self, answerData, AnswerPanel, testMode):
	colordb = wx.TheColourDatabase
	print "buildBoxes is running\n"
	answerCheckBoxList = []
	checkBoxSizer = AnswerPanel.Sizer
	checkBoxSizer.clear(destroy=True)
	rowNum = 0
	for item in answerData:
		questionNumber = item['AnswerQuestionNo']
		questionNumberLabel = wx.StaticText(AnswerPanel, wx.ID_ANY, str(questionNumber) + ') ')
		checkBoxSizer.append(questionNumberLabel, row=rowNum, col=0)
		#checkBoxSizer.setItemProps(questionNumberLabel, {'ColExpand': True, 'BorderSides': ['All'], 'ColSpan': 1, 'Proportion': 0, 'HAlign': 'Center', 'RowSpan': 1, 'VAlign': 'Middle', 'Border': 1, 'Expand': False, 'RowExpand': False})
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
				CheckBoxA.SetBackgroundColour(colordb.Find('PALE GREEN'))
				CheckBoxA.Refresh()
			if item['AnswerCorrectAnswer'] == 'B':
				CheckBoxB.SetBackgroundColour(colordb.Find('PALE GREEN'))
				CheckBoxB.Refresh()
			if item['AnswerCorrectAnswer'] == 'C':
				CheckBoxC.SetBackgroundColour(colordb.Find('PALE GREEN'))
				CheckBoxC.Refresh()
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
	#dabo.ui.info("CheckBox layout complete!")
	return(answerCheckBoxList)


def buildGradeReport(self):
	print "buildGradeReport is running\n"
	app = self.Application
	self.headerLines = []
	self.headerLines.append('<b>' + str(self.gradeRecord['currentDate']) + '\t\t\t' + self.gradeRecord['lessonFullName'] + '</b>\n\n')
	tempString = 'Student:\t<b>' + self.gradeRecord['studentFullName'] + '</b>'
	# if there is no StudentID, skip that line
	if self.gradeRecord['studentID'] != '' and self.gradeRecord['studentID'] != None:
		tempString = tempString + '\tStudent ID:\t<b>' + self.gradeRecord['studentID'] + '</b>'
	self.headerLines.append(tempString + '\n')
	self.headerLines.append('Teacher:\t<b>' + self.gradeRecord['teacherFullName'] + '</b>\n')
	self.headerLines.append('Contact:\t<b>' + self.gradeRecord['contactFullName'] + '</b>\n')
	self.headerLines.append('Score:\t<b>' + self.gradeRecord['grade'] + '%</b>\n\n')
	self.missedLines = []
	if self.gradeRecord['numberMissed'] == 0:
		self.missedLines.append("<b>No questions missed!</b>")
	else:
		self.missedLines.append("<b>Question missed\tYour answer\tCorrect answer</b>\n")
	for line in self.gradeRecord['missedList']:
		self.missedLines.append('<b>' + line[0] + '\t' + line[1] + '\t' + line[2] + '</b>\n')
		print 'self.missedLines start'
		print self.missedLines
		print 'self.missedLines end'
	self.commentLines = []
	if ' ' in self.gradeRecord['studentFirstName']:
		index = self.gradeRecord['studentFirstName'].find(' ')
		shortFirstName = self.gradeRecord['studentFirstName'][0:index]
	else:
		shortFirstName = self.gradeRecord['studentFirstName']
	self.commentLines.append('\nDear ' + shortFirstName + ',\n\n')
	for line in self.gradeRecord['commentList']:
		self.commentLines.append(line + '\n\n')
	self.commentLines.append('Your study helper,\n')
	self.commentLines.append(self.gradeRecord['teacherFirstName'])



def getAnswerData(self, lessonNumber, bizObj):
	print "getAnswerData is running\n"
	tempCursor = bizObj.getTempCursor()
	sqlString = 'SELECT * from Answers where AnswerLessonsRecNo = ' + str(lessonNumber)
	tempCursor.UserSQL = sqlString
	tempCursor.requery()
	totalQuestions = len(tempCursor.getDataSet())
	return(tempCursor.getDataSet(), totalQuestions)


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
			dlg = dabo.ui.exclaim('Something is terribly wrong!\nThere are more than one grade records for this student and lesson!\nCall someone quick!')
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
					dlg = dabo.ui.info('Output from save operation = ' + str(bizObj.save()) + '.\n')
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
			dlg = dabo.ui.info('Output from save operation = ' + str(bizObj.save()) + '.\n')
			self.requery()
	except:
		dlg = dabo.ui.exclaim("Oh my! Something has gone wrong!")


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
				missedList.append(questionMissedDict)
	return(numberCorrect, missedList)


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
	self.HeaderOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel)
	self.HeaderOutBox.ReadOnly=True
	self.MissedOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel)
	self.MissedOutBox.ReadOnly=True
	self.CommentOutBox = dabo.ui.uiwx.dRichTextBox(self.OutputScrollPanel)
	self.CommentOutBox._addWindowStyleFlag(wx.WANTS_CHARS|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
	self.OutputScrollPanel.Sizer.prepend(self.CommentOutBox, proportion=1, layout='expand', border=2)
	self.OutputScrollPanel.Sizer.prepend(self.MissedOutBox, proportion=1, layout='expand', border=2)
	self.OutputScrollPanel.Sizer.prepend(self.HeaderOutBox, proportion=1, layout='expand', border=2)
	# getAnswerData needs the lesson number to look up the answer data
	(self.answerDataSet, totalQuestions) = self.getAnswerData(self.lessonRecNo, self.getBizobj('Answers'))
	#print self.answerDataSet
	self.AnswerPanel.Freeze()
	self.answerCheckBoxList = self.buildBoxes(self.answerDataSet, self.AnswerPanel, self.testMode)
	self.AnswerPanel.Thaw()
	self.PrimaryBizobj.addWhere("StudentRecNo = " + str(self.StudentRecNo))
	self.requery()
	studentRecord = self.PrimaryBizobj.Record
	# now we have the info we need to initialize the gradeRecord
	self.gradeRecord = {'currentDate':datetime.date.today(),
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
	self.outputLines(self.missedLines, self.MissedOutBox)
	self.outputLines(self.commentLines, self.CommentOutBox)


def initProperties(self):
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue('fontsize')
	self.RegID = 'GradingForm'
	# testMode colors the boxes for the correct answers green
	self.testMode = True
	self.lessonScored = False
	self.commentsSelected = False
	self.Centered = True


def openCommentSelectorForm(self):
	app = self.Application
	newForm = app.ui.CommentSelectorForm(app.MainForm, Modal=True)
	print "self.gradeRecord start"
	print self.gradeRecord
	print "self.gradeRecord end"
	newForm.TextTags = ({'<ContactFirstName>':self.gradeRecord['contactFirstName'], '<NumberOfQuestionsMissed>':str(self.gradeRecord['totalQuestions'] - self.gradeRecord['numberCorrect'])})
	newForm.lessonShortName = self.gradeRecord['lessonShortName']
	newForm.buildCommentDictList(self.PrimaryBizobj)
	newForm.SaveRestorePosition = True
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
		self.buildGradeReport()
		self.displayOutput()
	newForm.safeDestroy()


def saveCurrentGradeRecord(self):
	app = self.Application
	import datetime
	now = datetime.date.today()
	print 'attempting to save grade record\n'
	self.saveGradeRecord(self,
											studentsRecNo = self.PrimaryBizobj.Record["StudentRecNo"],
											currentDate = now,
											lessonRecNo = self.lessonRecNo,
											score = self.GradeReportRecord['Grade'],
											comments = self.selectedComments)


def savePDF(self):
	app = self.Application
	newForm = app.ui.FrmPreviewPDF(self)
	newForm.headerInput = self.headerLines
	newForm.missedInput = self.missedLines
	newForm.commentInput = self.commentLines
	newForm.show()


def scoreLesson(self):
	app = self.Application
	self.HeaderOutBox.Clear()
	self.HeaderOutBox.refresh()
	self.MissedOutBox.Clear()
	self.MissedOutBox.refresh()
	self.CommentOutBox.Clear()
	self.CommentOutBox.refresh()
	if self.EnterWrongAnswersCheckBox.Value == True:
		(self.gradeRecord['numberCorrect'], self.gradeRecord['missedList']) = self.scoreWrongAnswers(self.answerCheckBoxList, self.answerDataSet)
	else:
		(self.gradeRecord['numberCorrect'], self.gradeRecord['missedList']) = self.scoreQuestions(self.answerCheckBoxList, self.answerDataSet)
	self.gradeRecord['numberMissed'] = self.gradeRecord['totalQuestions'] - self.gradeRecord['numberCorrect']
	self.gradeRecord['grade'] = str((100.0 / self.gradeRecord['totalQuestions']) * self.gradeRecord['numberCorrect'])
	self.buildGradeReport()
	self.displayOutput()



## *!* ## Dabo Code ID: dButton-dPanel-435
def onHit(self, evt):
	# WriteToDB button
	self.Form.saveCurrentGradeRecord()


