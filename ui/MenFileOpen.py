# -*- coding: utf-8 -*-

import dabo.ui
import dabo.dEvents as dEvents


class MenFileOpen(dabo.ui.dMenu):

	def initProperties(self):
		super(MenFileOpen, self).initProperties()
		self.RegID = "fileOpenMenu"
		self.Name = "FileOpenMenu"
		self.Caption = "&Open"
		self.HelpText = "Open a module"


	def afterInit(self):
		app = self.Application
		autoHotKeys = True

		# Define the forms you want in your open menu here. Insert a ("-", None)
		# tuple and the code below will insert a separator in its place. Explicitly
		# set up which character has the hotkey by adding a & in front of it and
		# by turning off the autoHotKeys flag.

		forms = (("Answers Form", app.ui.AnswersForm),
				("Attachments Form", app.ui.AttachmentsForm),
				("Comments Form", app.ui.CommentsForm),
				("Contacts Form", app.ui.ContactsForm),
				("Grades Form", app.ui.GradesForm),
				("Lessons Form", app.ui.LessonsForm),
				("Students Form", app.ui.StudentsForm),
				("Teachers Form", app.ui.TeachersForm),
				)

		for form in forms:
			caption = form[0]
			if caption == "-":
				# insert separator instead:
				self.appendSeparator()
			else:
				if autoHotKeys and "&" not in caption:
					caption = "&%s" % caption
				plainCaption = caption.replace("&", "")
				itm = dabo.ui.dMenuItem(self, Caption=caption,
						HelpText="Open the %s module" % plainCaption,
						Tag=form[1])
				itm.bindEvent(dEvents.Hit, self.openForm)
				self.appendItem(itm)


	def openForm(self, evt):
		app = self.Application
		mainForm = app.MainForm
		print 'evt = ' + str(evt)
		print 'EventObject = ' + str(evt.EventObject)
		print 'Tag = ' + str(evt.EventObject.Tag)
		frm = evt.EventObject.Tag(mainForm)
		frm.show()
