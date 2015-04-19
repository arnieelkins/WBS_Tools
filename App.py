# -*- coding: utf-8 -*-

import dabo
from dabo.dApp import dApp
from dabo.dLocalize import _
from registerFonts import registerFonts
import os
import tempfile
import sys

class App(dApp):
	def initProperties(self):
		# Manages how preferences are saved
		self.BasePrefKey = "dabo.app.WBSToolsTEST"
		self.setAppInfo("appShortName", "WBSTools")
		self.setAppInfo("appName", "WBSTools")
		self.setAppInfo("copyright", "(c) 2013, 2014")
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
		self.setAppInfo("authorEmail", "arnie.elkins.wbs@gmail.com")
		self.setAppInfo("authorURL", "http://monrovia.org/wbs")

		## Set app version information:
		# This is the central place to keep your application's version updated. 
		__version__ = "0.9.4.7"
		self.setAppInfo("appVersion", __version__)
		self.CryptoKey = "WeHoldTheseTruths"
		print os.getcwd()
		#registerFonts(os.getcwd())
		self.Icon = "icons/wbs.ico"

	def setup(self):
		if dabo.MDI:
			#self.MainFormClass = dabo.ui.createForm("ui/StudentsForm.cdxml")
			self.MainFormClass = dabo.ui.dFormMain
		else:
			# no need for main form in SDI mode
			self.MainFormClass = None
		super(App, self).setup()


	def getTempDir(self):
		self.TempDir = tempfile.gettempdir()
		print 'self.TempDir = ', self.TempDir, type(self.TempDir)
		if not self.testTempDir:
			self.getTempDir()
		self.PreferenceManager.setValue("TempDir", self.TempDir)
	def testTempDir(self):
		if self.TempDir:
			if os.path.exists(self.TempDir):
				try:
					handle = open('testfile', 'wb')
					handle.write(fileData)
					handle.close()
					os.remove('testfile')
					self.PreferenceManager.setValue("TempDir", self.TempDir)
					return(True)
				except Exception, e:
					dabo.ui.exclaim("Oh No!  An exception while writing the file!  This is a Really, Really Bad Thing!\n" + str(traceback.format_exc()))
			else:
				response = dabo.ui.areYouSure(message = "TempDir is defined as " + str(self.TempDir) + " but it does not exist.  Attempt to create it?",
												defaultNo = True,
												cancelButton = False,
												requestUserAttention=True)
				if response == True:
					try:
						os.mkdir(self.TempDir)
						self.PreferenceManager.setValue("TempDir", self.TempDir)
						return(True)
					except:
						dabo.ui.exclaim('Unable to create a temp directory!!')
						dabo.ui.exclaim("Well alrighty then, since I can't work without one, I quit!")
						return(False)
						sys.exit(1)
						

