# -*- coding: utf-8 -*-

from dabo.dLocalize import _

import dabo.ui
import dabo.lib.datanav
import dabo.lib.reportUtils as reportUtils


class FrmReportBase(dabo.ui.dDialog):
	def initProperties(self):
		super(FrmReportBase, self).initProperties()
		## Do this import here: in case prerequisites aren't installed, the app
		## will still start.
		from dabo.dReportWriter import dReportWriter

		if self.ReportName:
			self.Caption = self.ReportName
		else:
			self.Caption = "Run Report"
		self.Modal = True
		self.ReportForm = None
		self.DataSet = []
		self.ReportWriter = dReportWriter(Encoding=dabo.defaultEncoding)
		self.SizerBorder = 7
		self.BorderResizable = True
		self.MinimumWidth = 600
		self.MinimumHeight = 400

	def addControls(self):
		pass

	def onHit_butPreview(self, evt):
		self.runReport("preview")


	def onHit_butPrint(self, evt):
		self.runReport("print")


	def requery(self):
		"""Subclasses should override to fill self.DataSet"""
		pass


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

