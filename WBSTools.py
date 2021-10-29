#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If this is a web application, set the remote host here
remotehost = ""

import sys
import os
import wx
import dabo.ui
from dabo.dLocalize import _
# The loading of the UI needs to happen before the importing of the
# db, biz, and ui packages:
dabo.ui.loadUI("wx")
print sys.platform
if sys.platform[:3] == "win":
	dabo.MDI = True

if sys.platform == "darwin":
	dabo.MDI = True
# hack for locale error on OSX
#    import locale
#    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
import db
import biz
import ui
import reports

# included for PyInstaller
#import wx.gizmos, wx.lib.calendar 

from App import App
app = App(SourceURL=remotehost)
app.db = db
app.biz = biz
app.ui = ui
app.reports = reports

# Make it easy to find any images or other files you put in the resources
# directory.
sys.path.append(os.path.join(app.HomeDirectory, "resources"))

app.setup()

#app.PreferenceManager.setValue("basedir", None)
app.BaseDir = app.PreferenceManager.getValue("basedir")
print "basedir = " + str(app.BaseDir)
if app.BaseDir == None or app.BaseDir == '':
	dabo.ui.info("Please choose a directory for me to use for creating temporary files, etc.")
	response = dabo.ui.getFolder()
	if response == None or response == '':
		dabo.ui.exclaim("Hey, I really need a directory to write stuff!  That's it, I quit!")
		sys.exit()
	else:
		print "response = ;" + str(response) + ";" 
		app.BaseDir = response
		app.PreferenceManager.setValue("basedir", app.BaseDir)
if app.BaseDir:
	app.tempdir = str(os.path.join(app.BaseDir, 'tmp'))
	if not os.path.exists(app.tempdir):
		try:
			os.mkdir(app.tempdir)
		except:
			dabo.ui.exclaim('Unable to create a temp directory!!')

app.MainFormClass = app.ui.FrmMain
app.PreferenceManager.setValue("fontsize", 11)
app.NoneDisplay = ""
# Set up a global connection to the database that all bizobjs will share:
app.dbConnectionName = "wbs_monro_user"
app.dbConnection = app.getConnectionByName(app.dbConnectionName)
#app.dbConnection.LogEvents = ['All']


# Open one or more of the defined forms. A default one was picked by the app
# generator, but you can change that here. Additionally, if form names were
# passed on the command line, they will be opened instead of the default one
# as long as they exist.
app.ui.AnswersForm = dabo.ui.createClass("ui" + os.sep + "AnswersForm.cdxml")
app.ui.AttachmentsForm = dabo.ui.createClass("ui" + os.sep + "AttachmentsForm.cdxml")
app.ui.CommentsForm = dabo.ui.createClass("ui" + os.sep + "CommentsForm.cdxml")
app.ui.ContactsForm = dabo.ui.createClass("ui" + os.sep + "ContactsForm.cdxml")
app.ui.GetFilesForContactForm = dabo.ui.createClass("ui" + os.sep + "GetFilesForContactForm.cdxml")
app.ui.GradesForm = dabo.ui.createClass("ui" + os.sep + "GradesForm.cdxml")
app.ui.LessonsForm = dabo.ui.createClass("ui" + os.sep + "LessonsForm.cdxml")
app.ui.StudentsForm = dabo.ui.createClass("ui" + os.sep + "StudentsForm.cdxml")
app.ui.TeachersForm = dabo.ui.createClass("ui" + os.sep + "TeachersForm.cdxml")
app.ui.PrintOrPreviewForm = dabo.ui.createClass("ui" + os.sep + "PrintOrPreviewForm.cdxml")
app.ui.LessonSelector = dabo.ui.createClass("ui" + os.sep + "LessonSelector.cdxml")
app.ui.CommentSelectorForm = dabo.ui.createClass("ui" + os.sep + "CommentSelectorForm.cdxml")
app.DefaultForm = app.ui.StudentsForm
app.FormsToOpen = [app.DefaultForm]
app.startupForms()
if app.MainForm != None:
	app.MainForm.Caption = 'WBSTools version ' + str(app.getAppInfo('appVersion') + ' user = ' + str(app.dbConnectionName))
# Start the application event loop:
app.start()
