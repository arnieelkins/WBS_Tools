# -*- coding: utf-8 -*-

import dabo.ui
import dabo.lib.datanav as datanav
from MenFileOpen import MenFileOpen
from MenReports import MenReports


class FrmBase(datanav.Form):

	def initProperties(self):
		super(FrmBase, self).initProperties()
		# Setting RequeryOnLoad to True will result in an automatic requery upon
		# form load, which may be appropriate for your app (if it is reasonably
		# certain that the dataset will be small no matter what).
		self.RequeryOnLoad = False
		self.Icon = "wbs.ico"


	def setupMenu(self):
		super(FrmBase, self).setupMenu()
		self.fillFileOpenMenu()
		self.fillReportsMenu()


	def fillFileOpenMenu(self):
		"""Add the File|Open menu, with menu items for opening each form."""
		app = self.Application
		fileMenu = self.MenuBar.getMenu("base_file")
		fileMenu.prependMenu(MenFileOpen(fileMenu))


	def fillReportsMenu(self):
		"""Add the Reports menu."""
		from dabo.dLocalize import _
		app = self.Application
		menReports = MenReports()

		# We want the reports menu right after the View menu:
		idx = self.MenuBar.getMenuIndex(_("View"))
		if idx is None:
			# punt:
			idx = 2
		idx += 1
		self.MenuBar.insertMenu(idx, menReports)
