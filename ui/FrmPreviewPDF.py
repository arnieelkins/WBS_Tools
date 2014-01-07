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

class FrmPreviewPDF(FrmReportBase):

	def initProperties(self):
		app = self.Application
		self.FontSize = app.PreferenceManager.getValue("fontsize")
		self.ReportName=''
		super(FrmPreviewPDF, self).initProperties()
		self.ReportForm = ""

	def requery(self):
		"""Called by preview in FrmReportBase, it's time to requery the dataset."""
		# Send whatever parameters your function requires, perhaps as entered by the
		# user in the controls you've exposed in this form.
		self.DataSet = [{'headerblock':self.headerOutput + self.missedOutput + self.commentOutput}]

	def runReport(self, mode):
		"""Run the report and then preview or print it."""
		print "running report +++++++++++++++++++++++++++++++++"
		self.requery()
		f = self.write()
		if mode == "preview":
			dabo.lib.reportUtils.previewPDF(f)
		elif mode == "print":
			dabo.lib.reportUtils.printPDF(f)
		else:
			raise ValueError, "Mode needs to be 'preview' or 'print'."

	def FormatOutput(self, input):
		outputBlock = ''
		for line in input:
			for item in line:
				itemString = str(item)
				tempString = itemString.replace('\n', '<br/>')
				tempString = tempString.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
				tempString = tempString.replace('<sp>', '&nbsp;')
				outputBlock = outputBlock + tempString
		return(outputBlock)



	def write(self):
		"""Write the report to a temporary file, and return the file name."""
		rw = self.ReportWriter
		rw.ReportFormFile = self.ReportForm
		rw.Cursor = self.DataSet
		f = rw.OutputFile = dabo.lib.reportUtils.getTempFile()
		rw.write()
		return f

	def afterInitAll(self):
		import os
		app = self.Application
		self.headerOutput = self.FormatOutput(self.headerInput)
		self.missedOutput = self.FormatOutput(self.missedInput)
		self.commentOutput = self.FormatOutput(self.commentInput)
		self.ReportForm = "reports" + os.sep + "GradeReport.rfxml"
		self.runReport("preview")
		self.safeDestroy()
