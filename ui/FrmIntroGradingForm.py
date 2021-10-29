# -*- coding: utf-8 -*-

## This is a sample form for putting together a report form xml (rfxml file)
## and a dataset, and previewing the report. Study this code, as well as the
## code in FrmReportBase, and then rework it to your specific needs. To put
## your report in the reports menu, see MenReports.py.

import datetime
import os
from dabo.dLocalize import _
import dabo.ui
from FrmReportBase import FrmReportBase
import dabo.lib

class FrmIntroGradingForm(FrmReportBase):

	def initProperties(self):
		app = self.Application
		self.FontSize = app.PreferenceManager.getValue("fontsize")
		self.ReportName = _("Choose Lesson")
		super(FrmIntroGradingForm, self).initProperties()
		self.ReportForm = ""
		self.DataSetFunction = app.db.getIntroGradingFormDataSet

	def addControls(self):
		import os
		"""Add any controls here, such as record selection choices."""
		super(FrmIntroGradingForm, self).addControls()
		siz = self.Sizer
		printOrPreviewPanel = dabo.ui.createClass("ui" + os.sep + "PrintOrPreviewPanel.cdxml")
		newPanel = printOrPreviewPanel(self, RegID = 'PrintOrPreviewPanel')
		siz.append(newPanel, alignment='center')

	def afterInitAll(self):
		app = self.Application
		#app.LogEvents = ['All']


	def requery(self):
		"""Called by preview in FrmReportBase, it's time to requery the dataset."""
		# Send whatever parameters your function requires, perhaps as entered by the
		# user in the controls you've exposed in this form.
		self.DataSet = self.DataSetFunction(self.bizObj, self.recordNumber)
		#self.DataSet = [{'studentfirstname': 'Burton Lazaro', 'studentbible': '0', 'gradelessonsrecno': '1', 'studentage': '33', 'teacherfullname': 'Alyssa Boulton', 'studentchurchname': 'Church of Christ', 'studentwbsid': 'AL-091', 'studentrecno': '862', 'studentmaritalstatus': 'Married', 'studentwbsbefore': '0', 'studentfullname': 'Burton Lazaro Mwansamale', 'contactfullname': 'Willy Yudah', 'gradescore': '100', 'studentcountry': '', 'studentstreetaddress': '', 'studentphone1': '', 'studentphone2': '', 'studentbaptismtype': 'NULL', 'studentreligion': 'Christian', 'studentlastname': 'Mwansamale', 'studentrequestedbaptism': '0', 'gradedategraded': '2011-11-22', 'studentstate': '', 'studentid': '', 'studentpostaladdress': '', 'studentcontactsrecno': '1', 'studentemailaddress': '', 'studentnotes': '', 'studenttown': '', 'studenthasbeenbaptized': '0', 'studentgender': 'M', 'studentbirthdate': '1978-12-11', 'studentoccupation': 'Teacher', 'studentteachersrecno': '1'}]
		print "self.DataSet begin"
		print self.DataSet
		print "self.DataSet end"

	def runReport(self, mode):
		"""Run the report and then preview or print it."""
		self.requery()
		f = self.write()
		if mode == "preview":
			dabo.lib.reportUtils.previewPDF(f)
		elif mode == "print":
			dabo.lib.reportUtils.printPDF(f)
		else:
			raise ValueError, "Mode needs to be 'preview' or 'print'."


	def write(self):
		"""Write the report to a temporary file, and return the file name."""
		rw = self.ReportWriter
		rw.ReportFormFile = self.ReportForm
		rw.Cursor = self.DataSet
		print rw.Cursor
		f = rw.OutputFile = dabo.lib.reportUtils.getTempFile()
		rw.write()
		return f

	def onHit_butPreview(self, evt):
		app = self.Application
		if self.LessonRadioList.Value == 'Intro':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" +
			os.sep + "IntroGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'GHS':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'TIGN':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'KJ':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'FOG':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'BWS':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml")
			self.runReport("preview")
		if self.LessonRadioList.Value == 'LLL':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml")
			self.runReport("preview")
		self.Form.safeDestroy()

	def onHit_butPrint(self, evt):
		app = self.Application
		if self.LessonRadioList.Value == 'Intro':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "IntroGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'GHS':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'TIGN':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'KJ':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'FOG':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'BWS':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml")
			self.runReport("print")
		if self.LessonRadioList.Value == 'LLL':
			self.ReportForm = os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml")
			self.runReport("print")
		self.Form.safeDestroy()


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


	def setupMenu(self):
		self.fillFileOpenMenu()
		self.fillReportsMenu()


