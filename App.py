# -*- coding: utf-8 -*-

import dabo
from dabo.dApp import dApp
from dabo.dLocalize import _
from registerFonts import registerFonts
import os

__version__ = "0.9.5.1"
class App(dApp):
	def initProperties(self):
		# Manages how preferences are saved
		self.BasePrefKey = "dabo.app.WBSTools"
		self.setAppInfo("appShortName", "WBSTools")
		self.setAppInfo("appName", "WBSTools")
		self.setAppInfo("copyright", "(c) 2013-2021")
		self.setAppInfo("companyName", "Monrovia Church of Christ")
		self.setAppInfo("companyAddress1", "595 Nance Road")
		self.setAppInfo("companyAddress2", "Madison, AL 35757")
		self.setAppInfo("companyPhone", "256.837.5255")
		self.setAppInfo("companyEmail", "wbs@monrovia.org")
		self.setAppInfo("companyUrl", "http://monrovia.org")

		self.setAppInfo("appDescription", _("Tools for grading World Bible School lessons and recording \
											student information in a MySQL database"))

		## Information about the developer of the software:
		self.setAppInfo("authorName", "Arnie Elkins")
		self.setAppInfo("authorEmail", "arnie.elkins@gmail.com")

		## Set app version information:
		self.setAppInfo("appVersion", __version__)
		self.CryptoKey = "WeHoldTheseTruths"
		print os.getcwd()
		registerFonts(os.getcwd())

	def setup(self):
		if dabo.MDI:
			#self.MainFormClass = dabo.ui.createForm("ui/StudentsForm.cdxml")
			self.MainFormClass = dabo.ui.dFormMain
		else:
			# no need for main form in SDI mode
			self.MainFormClass = None
		super(App, self).setup()



