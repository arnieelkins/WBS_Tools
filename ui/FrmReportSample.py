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


class FrmReportSample(FrmReportBase):

    def initProperties(self):
    	app = self.Application
    	self.ReportName = _("Sample Report")
    	super(FrmReportSample, self).initProperties()
    	self.ReportForm = os.path.join(app.HomeDirectory, "reports/sampleReport.rfxml")
    	self.DataSetFunction = app.db.getSampleDataSet


    def addControls(self):
    	"""Add any controls here, such as record selection choices."""
    	super(FrmReportSample, self).addControls()


    def requery(self):
    	"""Called by preview in FrmReportBase, it's time to requery the dataset."""
    	# Send whatever parameters your function requires, perhaps as entered by the
    	# user in the controls you've exposed in this form.
    	self.DataSet = self.DataSetFunction()

