# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import wx


## *!* ## Dabo Code ID: dButton-dPanel-373
def onHit(self, evt):
	# WriteToDB button
	self.Form.saveCurrentGradeRecord()



## *!* ## Dabo Code ID: dButton-dPanel-71
def onHit(self, evt):
	# Comments button
	self.Form.openCommentSelectorForm()



## *!* ## Dabo Code ID: dButton-dPanel-646
def onHit(self, evt):
	#clearoutput button
	app = self.Application
	self.Form.clearOutBox()



## *!* ## Dabo Code ID: dButton-dPanel-253
def onHit(self, evt):
	# SavePDF button
	app = self.Application
	self.Form.savePDF()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	#resetform button
	self.Form.clearAnswerCheckBoxes()
	self.Form.clearOutBox()



## *!* ## Dabo Code ID: dButton-dPanel-3
def onHit(self, evt):
	# Score button
	app = self.Application
	self.Form.scoreLesson()
	self.Form.CommentsButton.Enabled = True
	self.Form.CommentsButton.update()



## *!* ## Dabo Code ID: dForm-top
def GetFormattedSelection(self, format):
	app = self.Application
	""" Return a string with the formatted contents of just the RichText control's current selection.
		format can either be 'XML' or 'RTF'. """
	# If a valid format is NOT passed ...
	if not format in ['XML', 'RTF']:
		# ... return a blank string
		return ''
	
	# NOTE:  The wx.RichTextCtrl doesn't provide an easy way to get a formatted selection that I can figure out.
	#		This is a hack, but it works.

	# Freeze the control so things will work faster
	self.OutBox.Freeze()
	# We'll need to undo everything from this point on.  Let's do it as ONE operation.
	self.OutBox.BeginBatchUndo('RTCBufferSelection')
	# Get the start and end of the current selection
	sel = self.OutBox.GetSelection()
	# Delete everything AFTER the end of the current selection
	self.OutBox.Delete((sel[1], self.OutBox.GetLastPosition()))
	# Delete everything BEFORE the start of the current selection
	self.OutBox.Delete((0, sel[0]))
	# This leaves us with JUST the selection in the control!

	# If XML format is requested ...
	if format == 'XML':
		# Create a Stream
		stream = cStringIO.StringIO()
		# Get an XML Handler
		handler = richtext.RichTextXMLHandler()
		# Save the contents of the control to the stream
		handler.SaveStream(self.OutBox.GetBuffer(), stream)
		# Convert the stream to a usable string
		tmpBuffer = stream.getvalue()
	# If RTF format is requested ....
	elif format == 'RTF':
		# Get an RTF Handler
		handler = app.lib.PyRTFParser.PyRichTextRTFHandler()
		# Get the string representation by leaving off the filename parameter
		tmpBuffer = handler.SaveFile(self.OutBox.GetBuffer())

	# End Undo batching
	self.OutBox.EndBatchUndo()
	# Undo the changes.  This restores ALL the text
	self.OutBox.Undo()
	# Now thaw the control so that updates will be displayed again
	self.OutBox.Thaw()
		
	# Return the buffer's XML string
	return tmpBuffer


def OnCutCopy(self, event):
	""" Handle Cut and Copy events, over-riding the RichTextCtrl versions.
		This implementation supports Rich Text Formatted text, and at least on Windows can
		share formatted text with other programs. """
	# Create a Composite Data Object for the Clipboard
	compositeDataObject = wx.DataObjectComposite()

	# Get the current selection in RTF format
	rtfSelection = self.GetFormattedSelection('RTF')
	# Create a Custom Data Format for RTF
	if 'wxMac' in wx.PlatformInfo:
		rtfFormat = wx.CustomDataFormat('public.rtf')
	else:
		# Create a Custom Data Format for RTF
		rtfFormat = wx.CustomDataFormat('Rich Text Format')
	# Create a Custom Data Object for the RTF format
	rtfDataObject = wx.CustomDataObject(rtfFormat)
	# Save the RTF version of the control selection to the RTF Custom Data Object
	rtfDataObject.SetData(rtfSelection)
	# Add the RTF Custom Data Object to the Composite Data Object
	compositeDataObject.Add(rtfDataObject)

	# Get the current selection in Plain Text
	txtSelection = self.OutBox.GetStringSelection()
	# Create a Text Data Object
	txtDataObject = wx.TextDataObject()
	# Save the Plain Text version of the control selection to the Text Data Object
	txtDataObject.SetText(txtSelection)
	# Add the Plain Text Data Object to the Composite Data object
	compositeDataObject.Add(txtDataObject)

	# Open the Clipboard
	if wx.TheClipboard.Open():
		# Place the Composite Data Object (with RTF and Plain Text) on the Clipboard
		wx.TheClipboard.SetData(compositeDataObject)
		# Close the Clipboard
		wx.TheClipboard.Close()

	# If we are CUTting (rather than COPYing) ...
	if event.GetId() == wx.ID_CUT:
		# ... delete the selection from the Rich Text Ctrl.
		self.OutBox.DeleteSelection()


def OnPaste(self, event):
	""" Handle Paste events, over-riding the RichTextCtrl version.
		This implementation supports Rich Text Formatted text, and at least on Windows can
		share formatted text with other programs. """
	# Open the Clipboard
	if wx.TheClipboard.Open():
		if 'wxMac' in wx.PlatformInfo:
			rtfFormat = wx.CustomDataFormat('public.rtf')
		else:
			# Create a Custom Data Format for RTF
			rtfFormat = wx.CustomDataFormat('Rich Text Format')
		# See if the RTF Format is supported by the current clipboard data object
		if wx.TheClipboard.IsSupported(rtfFormat):
			# Specify that the data object accepts data in RTF format
			customDataObject = wx.CustomDataObject(rtfFormat)
			# Try to get data from the Clipboard
			success = wx.TheClipboard.GetData(customDataObject)
			# If the data in the clipboard is in an appropriate format ...
			if success:
				# ... get the data from the clipboard
				formattedText = customDataObject.GetData()
				# Prepare the control for data
				self.OutBox.Freeze()
				self.OutBox.BeginSuppressUndo()
				# Start exception handling
				try:
					# Use the custom RTF Handler
					handler = PyRTFParser.PyRichTextRTFHandler()
					# Load the RTF data into the Rich Text Ctrl via the RTF Handler.
					# Note that for RTF, the wxRichTextCtrl CONTROL is passed with the RTF string.
					handler.LoadString(self.OutBox, formattedText)
				# exception handling
				except:
					print "Custom RTF Handler Load failed"
					print
					print sys.exc_info()[0], sys.exc_info()[1]
					print traceback.print_exc()
					print
					pass
				# Signal the end of changing the control
				self.OutBox.EndSuppressUndo()
				self.OutBox.Thaw()
		# If there's not RTF data, see if there's Plain Text data
		elif wx.TheClipboard.IsSupported(wx.DataFormat(wx.DF_TEXT)):
			# Create a Text Data Object
			textDataObject = wx.TextDataObject()
			# Get the Data from the Clipboard
			wx.TheClipboard.GetData(textDataObject)
			# Write the plain text into the Rich Text Ctrl
			self.OutBox.WriteText(textDataObject.GetText())
		# Close the Clipboard
		wx.TheClipboard.Close()


def afterInitAll(self):
	import wx
	app = self.Application
	# self.lessonShortName is set by the LessonSelector form when calling GradingForm
	# look up the record number and the full name in the database
	tempCursor = self.getBizobj('Lessons').getTempCursor("select LessonName from Lessons where LessonShortName = %s", (self.lessonShortName,))
	self.lessonName = tempCursor.Record.LessonName
	tempCursor = self.getBizobj('Lessons').getTempCursor("select LessonRecNo from Lessons where LessonShortName = %s", (self.lessonShortName,))
	self.lessonRecNo = tempCursor.Record.LessonRecNo
	self.OutputPanel.Sizer.remove(self.OutBox, destroy=True)
	self.OutBox = dabo.ui.uiwx.dRichTextBox(self.OutputPanel)
	self.OutputLabel.Caption = self.lessonShortName + ' Output'
	self.Caption = self.lessonShortName + ' Grading Form'
	print self.OutBox.HasFlag(wx.TE_PROCESS_ENTER)
	self.OutBox._addWindowStyleFlag(wx.WANTS_CHARS|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
	print self.OutBox.HasFlag(wx.TE_PROCESS_ENTER)
	self.OutBox.Bind(wx.EVT_MENU, self.OnCutCopy, id=wx.ID_CUT)
	self.OutBox.Bind(wx.EVT_MENU, self.OnCutCopy, id=wx.ID_COPY)
	self.OutBox.Bind(wx.EVT_MENU, self.OnPaste, id=wx.ID_PASTE)
	self.OutputPanel.Sizer.insert(1, self.OutBox, proportion=1, layout='expand', border=2)
	# getAnswerData needs the lesson number to look up the answer data
	(self.answerDataSet, self.totalQuestions) = app.ui.GradingMethods.getAnswerData(self, self.lessonRecNo, self.getBizobj('Answers'))
	#print self.answerDataSet
	self.AnswerPanel.Freeze()
	self.answerCheckBoxList = app.ui.GradingMethods.buildBoxes(self, self.answerDataSet, self.AnswerPanel, self.testMode)
	self.AnswerPanel.Thaw()
	self.PrimaryBizobj.addWhere("StudentRecNo = " + str(self.StudentRecNo))
	self.requery()
	self.refresh()
	#dabo.eventLogging = True


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


def clearOutBox(self):
	app = self.Application
	self.OutBox.Clear()
	self.OutBox.refresh()


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


def displayOutput(self, outbox):
	app = self.Application
	print "displayOutput is running\n"
	outbox.Clear()
	outbox.refresh()
	self.curRec = self.PrimaryBizobj.Record
	self.GradeReportRecord = app.ui.GradingMethods.getGradeReportRecord(self,
																		self.curRec,
																		self.missedList,
																		self.commentList,
																		self.numCorrect,
																		self.totalQuestions,
																		self.lessonName,
																		self.PrimaryBizobj)
	print 'self.GradeReportRecord start\n'
	print self.GradeReportRecord
	print 'self.GradeReportRecord end\n'
	self.outboxContents = app.ui.GradingMethods.buildGradeReport(self, self.GradeReportRecord, outbox)


def initProperties(self):
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue('fontsize')
	self.RegID = 'GradingForm'
	# testMode colors the boxes for the correct answers green
	self.testMode = True
	self.commentList = []
	self.lessonScored = False
	self.commentsSelected = False
	self.outboxContents = []
	self.numCorrect = 0
	self.missedList = []
	self.Centered = True


def openCommentSelectorForm(self):
	app = self.Application
	newForm = app.ui.CommentSelectorForm(app.MainForm, Modal=True)
	newForm.TextTags = ({'<ContactFirstName>':self.curRec.ContactFirstName,
					'<NumberOfQuestionsMissed>':str(self.totalQuestions - self.numCorrect)})
	newForm.lessonName = self.lessonShortName
	newForm.buildCommentDictList(self.PrimaryBizobj)
	newForm.SaveRestorePosition = True
	newForm.show()
	if newForm.Accepted:
		#get our value, then destroy the form
		self.commentList = []
		self.selectedComments = newForm.ActiveCommentTextBox.getActiveCommentString()
		for char in self.selectedComments:
			print 'char = ' + str(char) + '\n'
			for dict in newForm.ActiveCommentDict:
				print "dict['letter'] = " + str(dict['letter'])
				if char == dict['letter']:
					self.commentList.append(dict['control'].Value + '\n\n')
					break
		self.displayOutput(self.OutBox)
	newForm.safeDestroy()


def saveCurrentGradeRecord(self):
	app = self.Application
	import datetime
	now = datetime.date.today()
	print 'attempting to save grade record\n'
	app.ui.GradingMethods.saveGradeRecord(self,
											studentsRecNo = self.PrimaryBizobj.Record["StudentRecNo"],
											currentDate = now,
											lessonRecNo = self.lessonRecNo,
											score = self.GradeReportRecord['Grade'],
											comments = self.selectedComments)


def savePDF(self):
	app = self.Application
	output = self.OutBox.Value
	print "printing output"
	print output
	print "end output"
	newForm = app.ui.FrmPreviewPDF(self)
	newForm.input = output
	newForm.show()


def scoreLesson(self):
	app = self.Application
	self.OutBox.Clear()
	self.OutBox.refresh()
	if self.EnterWrongAnswersCheckBox.Value == True:
		(self.numCorrect, self.missedList) = app.ui.GradingMethods.scoreWrongAnswers(self, self.answerCheckBoxList, self.answerDataSet)
	else:
		(self.numCorrect, self.missedList) = app.ui.GradingMethods.scoreQuestions(self, self.answerCheckBoxList, self.answerDataSet)
	'''
	self.OutBox.WriteText("Student got " + str(self.numCorrect) + \
					" questions right, out of " + str(self.totalQuestions) + \
					" for a score of " + str((100.0 / self.totalQuestions) * self.numCorrect) + '%\n')
	self.lessonScored = True
	'''
	self.curRec = self.PrimaryBizobj.Record
	self.displayOutput(self.OutBox)


