#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo.ui
from dabo.ui.uiwx.dDialog import dOkCancelDialog
import wx
from wxPython.lib import colourdb

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


def buildGradeReport(self, GradeReportRecord, OutBox):
	print "buildGradeReport is running\n"
	app = self.Application
	import datetime
	currentDate = datetime.date.today()
	lessonName = GradeReportRecord['LessonName']
	studentFullName = GradeReportRecord['StudentFullName']
	studentFirstName = GradeReportRecord['StudentFirstName']
	teacherFullName = GradeReportRecord['TeacherFullName']
	teacherFirstName = GradeReportRecord['TeacherFirstName']
	contactFullName = GradeReportRecord['ContactFullName']
	contactFirstName = GradeReportRecord['ContactFirstName']
	studentID = GradeReportRecord['StudentID']
	grade = GradeReportRecord['Grade']
	numberMissed = str(GradeReportRecord['NumberMissed'])
	questionBlock = GradeReportRecord['QuestionBlock']
	commentBlock = GradeReportRecord['CommentBlock']
	headerLines = []
	questionLines = []
	commentLines = []
	OutBox.SetPage = ''
	OutBox.refresh()
	headerLines.append('<b>' + str(currentDate) + '\t\t\t' + lessonName + '</b>\n\n')
	tempString = 'Student:\t<b>' + studentFullName + '</b>'
	# if there is no StudentID, skip that line
	if studentID <> '':
		tempString = tempString + '\tStudent ID:\t<b>' + studentID + '</b>'
	headerLines.append(tempString + '\n')
	headerLines.append('Teacher:\t<b>' + teacherFullName + '</b>\n')
	headerLines.append('Contact:\t<b>' + contactFullName + '</b>\n')
	headerLines.append('Score:\t<b>' + grade + '%</b>\n\n')
	if numberMissed == '0':
		headerLines.append('<b>No questions missed!</b>\n')
	elif numberMissed == '1':
		headerLines.append('<b>Question missed:</b>\n')
	else:
		headerLines.append('<b>Questions missed:</b>\n')
	for line in questionBlock.splitlines():
		questionLines.append(line + '\n')
	if ' ' in studentFirstName:
		index = studentFirstName.find(' ')
		shortFirstName = studentFirstName[0:index]
	else:
		shortFirstName = studentFirstName
	commentLines.append('\nDear ' + shortFirstName + ',\n\n')
	for line in commentBlock.splitlines():
		commentLines.append(line + '\n')
	commentLines.append('Your study helper,\n')
	commentLines.append(teacherFirstName)
	combinedLines = []
	for line in headerLines:
		combinedLines.append(line)
	for line in questionLines:
		combinedLines.append(line)
	for line in commentLines:
		combinedLines.append(line)
	# output all lines, starting and ending Bold as needed
	app.ui.GradingMethods.outputLines(self, combinedLines, self.OutBox)
	return(combinedLines)

def outputLines(self, Lines, OutputBox):
	print Lines
	for line in Lines:
		# Two newlines in a row can cause this function to skip one of them.  Insert a space
		# to make sure that does not happen.
		line = line.replace('\n\n', '\n \n')
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


def getAnswerData(self, lessonNumber, bizObj):
	print "getAnswerData is running\n"
	tempCursor = bizObj.getTempCursor()
	sqlString = 'SELECT * from Answers where AnswerLessonsRecNo = ' + str(lessonNumber)
	tempCursor.UserSQL = sqlString
	tempCursor.requery()
	totalQuestions = len(tempCursor.getDataSet())
	return(tempCursor.getDataSet(), totalQuestions)


def lookupComments(self, dictList, bizObj, tagDict):
	print "lookupComments is running\n"
	if len(dictList) >= 1:
		tempCursor = bizObj.getTempCursor()
		tempString = '('
		for item in dictList:
			tempString = tempString + "'" + item['Caption'] + "',"
		tempString = tempString[0:-1] + ")"
		tempCursor.UserSQL = 'select CommentTag, CommentContent from Comments where CommentTag in ' + tempString
		tempCursor.requery()
		commentList = []
		for item in dictList:
			for record in tempCursor:
				if item['Caption'] == record['CommentTag']:
					thisComment = record['CommentContent']
					# replace any tags in the comment with the actual values
					for key in tagDict:
						if key in thisComment:
							thisComment = thisComment.replace(key, tagDict[key])
					item['Comment'] = thisComment



def getGradeReportRecord(self, curRec, missedList, commentList, numCorrect, totalQuestions, lessonName, bizObj):
	print "getGradeReportRecord is running\n"
	questionBlock = ''
	for line in missedList:
		qnum  = line['questionNumber']
		sans = line['studentAnswer']
		cans = line['correctAnswer']
		output = str(qnum) + ' - '
		if sans == '':
			answer = 'You did not answer.'
		else:
			answer = 'You answered <b>' + str(sans) + '</b>.'
		output = output + answer + ' The answer is <b>' + cans + '</b>.\n'
		questionBlock = questionBlock + output
	commentBlock = ''
	for line in commentList:
		commentBlock = commentBlock + line
	reportRecord = {}
	reportRecord['StudentID'] = curRec['StudentID']
	reportRecord['StudentFirstName'] = curRec['StudentFirstName']
	reportRecord['StudentFullName'] = curRec['StudentFullName']
	reportRecord['TeacherFirstName'] = curRec['TeacherFirstName']
	reportRecord['TeacherFullName'] = curRec['TeacherFullName']
	reportRecord['ContactFirstName'] = curRec['ContactFirstName']
	reportRecord['ContactFullName'] = curRec['ContactFullName']
	reportRecord['LessonName'] = lessonName
	pointValue = 100 / totalQuestions
	reportRecord['Grade'] = str(numCorrect * pointValue)
	reportRecord['NumberMissed'] = str(totalQuestions - numCorrect)
	reportRecord['QuestionBlock'] = questionBlock
	reportRecord['CommentBlock'] = commentBlock
	return(reportRecord)



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
					dlg = dabo.ui.info('Output from save operation = ' + str(bizObj.save()) + '.\nIf it says None, that is a Good Thing!')
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
			dlg = dabo.ui.info('Output from save operation = ' + str(bizObj.save()) + '.\nIf it says None, that is a Good Thing!')
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
					questionMissedDict['correctAnswer'] = correctAnswer
					questionMissedDict['studentAnswer'] = studentAnswer
			if questionMissedDict.has_key('questionNumber'):
				# add the missed question info to missedList so we can reference
				# that list to build the output dataset
				missedList.append(questionMissedDict)
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
