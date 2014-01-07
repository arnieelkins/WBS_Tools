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
app.tempdir = str(os.path.join(os.getcwd(), 'tmp'))
if not os.path.exists(app.tempdir):
	try:
		os.mkdir(app.tempdir)
	except:
		dabo.ui.exclaim('Unable to create a temp directory!!')

# Make it easy to find any images or other files you put in the resources
# directory.
sys.path.append(os.path.join(app.HomeDirectory, "resources"))

app.setup()
app.MainFormClass = app.ui.FrmMain
app.PreferenceManager.setValue("fontsize", 11)
app.NoneDisplay = ""
# Set up a global connection to the database that all bizobjs will share:
app.dbConnection = app.getConnectionByName("wbs_dabo_admin")
#app.dbConnection.LogEvents = ['All']


# Open one or more of the defined forms. A default one was picked by the app
# generator, but you can change that here. Additionally, if form names were
# passed on the command line, they will be opened instead of the default one
# as long as they exist.
app.ui.AnswersForm = dabo.ui.createClass("ui//AnswersForm.cdxml")
app.ui.CommentsForm = dabo.ui.createClass("ui//CommentsForm.cdxml")
app.ui.ContactsForm = dabo.ui.createClass("ui//ContactsForm.cdxml")
app.ui.GradesForm = dabo.ui.createClass("ui//GradesForm.cdxml")
app.ui.LessonsForm = dabo.ui.createClass("ui//LessonsForm.cdxml")
app.ui.StudentsForm = dabo.ui.createClass("ui//StudentsForm.cdxml")
app.ui.TeachersForm = dabo.ui.createClass("ui//TeachersForm.cdxml")
app.ui.PrintOrPreviewForm = dabo.ui.createClass("ui//PrintOrPreviewForm.cdxml")
app.ui.LessonSelector = dabo.ui.createClass("ui//LessonSelector.cdxml")
app.ui.CommentSelectorForm = dabo.ui.createClass("ui//CommentSelectorForm.cdxml")
app.DefaultForm = app.ui.StudentsForm
app.FormsToOpen = [app.DefaultForm]
app.startupForms()
if app.MainForm != None:
	app.MainForm.Caption = 'WBSTools version ' + str(app.getAppInfo('appVersion'))
# Start the application event loop:
app.start()
