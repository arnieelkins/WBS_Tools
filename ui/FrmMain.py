# -*- coding: utf-8 -*-

import dabo.ui
from MenFileOpen import MenFileOpen
from MenEditPrefs import MenEditPrefs


class FrmMain(dabo.ui.dFormMain):

	def afterInit(self):
		super(FrmMain, self).afterInit()
		print "adding FileOpenMenu"
		self.fillFileOpenMenu()
		print "adding EditPrefsMenu"
		self.fillEditPrefsMenu()



	def initProperties(self):
		app = self.Application
		self.BasePrefKey = app.BasePrefKey
		self.FontSize = app.PreferenceManager.getValue("fontsize")
		super(FrmMain, self).initProperties()
		self.Icon = "daboIcon.ico"
		self.BasePrefKey = app.BasePrefKey



	def fillFileOpenMenu(self):
		"""Add the File|Open menu, with menu items for opening each form."""
		app = self.Application
		fileMenu = self.MenuBar.getMenu("base_file")
		fileMenu.prependMenu(MenFileOpen(fileMenu))

	def fillEditPrefsMenu(self):
		app = self.Application
		print "finding base_edit menu"
		editMenu = self.MenuBar.getMenu("base_edit")
		print "editMenu = " + str(editMenu)
		editMenu.prependMenu(MenEditPrefs(editMenu))



