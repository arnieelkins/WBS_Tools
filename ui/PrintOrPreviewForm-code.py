# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

from dabo.dLocalize import _
import dabo.ui
import dabo.lib.datanav
import dabo.lib.reportUtils as reportUtils


## *!* ## Dabo Code ID: dButton-dPanel-222
def onHit(self, evt):
	import os
	app = self.Application
	reportList = []
	checkBoxDict = {self.Form.IntroCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "IntroGradingForm.rfxml"),
									self.Form.GHSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml"),
									self.Form.TIGNCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml"),
									self.Form.KJCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml"),
									self.Form.FOGCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml"),
									self.Form.BWSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml"),
									self.Form.LLLCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml"),
									self.Form.GHS50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHS50QGradingForm.rfxml"),
									self.Form.TIGN50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGN50QGradingForm.rfxml"),
									self.Form.KJ50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJ50QGradingForm.rfxml"),
									self.Form.FOG50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOG50QGradingForm.rfxml"),
									self.Form.BWS50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWS50QGradingForm.rfxml"),
									self.Form.LLL50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLL50QGradingForm.rfxml")}
	for checkBox in checkBoxDict.keys():
		if checkBox.Value == True:
			reportList.append(checkBoxDict[checkBox])
	for report in reportList:
		self.Form.ReportForm = report
		self.Form.runReport("print")
	self.Form.safeDestroy()



## *!* ## Dabo Code ID: dForm-top
def GetDataSet(self, bizObj, recordNumber):
	tempCursor = bizObj.getTempCursor()
	sqlString = "SELECT concat(StudentFirstName, ' ', StudentLastName) as StudentFullName, concat(TeacherFirstName, ' ', TeacherLastName) as TeacherFullName, concat(ContactFirstName, ' ', ContactLastName) as ContactFullName, StudentAge, StudentBaptismType, StudentHasBible, StudentBirthDate, StudentChurchName, StudentContactsRecNo, StudentCountry, StudentEmailAddress, StudentFirstName, StudentGender, StudentHasBeenBaptized, StudentID, StudentLastName, StudentMaritalStatus, StudentNotes, StudentOccupation, StudentPhone1, StudentPhone2, StudentPostalAddress, StudentRecNo, StudentReligion, StudentRequestedBaptism, StudentState, StudentStreetAddress, StudentTeachersRecNo, StudentCity, StudentWBSBefore, StudentWBSID, GradeData, GradeStudentsRecNo FROM Teachers, Contacts, Students left join (select GradeStudentsRecNo, group_concat(GradeDateGraded, '\t', LessonShortName, '\t', GradeScore, '\t', coalesce(GradeComments, '') separator '\n') as GradeData from (select * from (select * from Grades left join Lessons on GradeLessonsRecNo = LessonRecNo) as GradesWithLesson where GradeStudentsRecNo in (select StudentRecNo from Students)) as StudentRecs group by GradeStudentsRecNo) as Gradestuff on Gradestuff.GradeStudentsRecNo = StudentRecNo where StudentteachersRecNo = TeacherRecNo and StudentContactsRecNo = ContactRecNo and StudentRecNo in"
	tempString = "(" + str(recordNumber) + ")"
	sqlString = sqlString + tempString
	print sqlString
	tempCursor.UserSQL = sqlString
	tempCursor.requery()
	return tempCursor.getDataSet()


def afterInitAll(self):
	self.DataSet = self.GetDataSet(self.bizObj, self.recordNumber)
	print self.DataSet


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.SaveRestorePosition = True
	self.FontSize = app.PreferenceManager.getValue("fontsize")
	from dabo.dReportWriter import dReportWriter
	self.ReportForm = None
	self.DataSet = []
	self.ReportWriter = dReportWriter(Encoding=dabo.defaultEncoding)
	self.SizerBorder = 7
	self.BorderResizable = False
	self.bizObj = dabo.biz.dBizobj
	self.recordNumber = 1
	# self.MinimumSize = (233, 381)
	# self.MaximumSize = (233, 381)
	self.Icon = "icons/wbs.ico"


def runReport(self, mode):
	"""Run the report and then preview or print it."""
	self.requery()
	f = self.write()
	if mode == "preview":
		reportUtils.previewPDF(f)
	elif mode == "print":
		reportUtils.printPDF(f)
	else:
		raise ValueError, "Mode needs to be 'preview' or 'print'."


def write(self):
	"""Write the report to a temporary file, and return the file name."""
	rw = self.ReportWriter
	rw.ReportFormFile = self.ReportForm
	rw.Cursor = self.DataSet
	f = rw.OutputFile = reportUtils.getTempFile()
	rw.write()
	return f



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	import os
	app = self.Application
	reportList = []
	checkBoxDict = {self.Form.IntroCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "IntroGradingForm.rfxml"),
									self.Form.GHSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml"),
									self.Form.TIGNCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml"),
									self.Form.KJCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml"),
									self.Form.FOGCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml"),
									self.Form.BWSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml"),
									self.Form.LLLCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml"),
									self.Form.GHS50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHS50QGradingForm.rfxml"),
									self.Form.TIGN50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGN50QGradingForm.rfxml"),
									self.Form.KJ50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJ50QGradingForm.rfxml"),
									self.Form.FOG50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOG50QGradingForm.rfxml"),
									self.Form.BWS50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWS50QGradingForm.rfxml"),
									self.Form.LLL50QCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLL50QGradingForm.rfxml")}
	for checkBox in checkBoxDict.keys():
		if checkBox.Value == True:
			reportList.append(checkBoxDict[checkBox])
	for report in reportList:
		self.Form.ReportForm = report
		self.Form.runReport("preview")
	self.Form.safeDestroy()


