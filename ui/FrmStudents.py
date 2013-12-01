# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdStudents import GrdStudents
from PagSelectStudents import PagSelectStudents
from PagEditStudents import PagEditStudents


class FrmStudents(FrmBase):

	def initProperties(self):
		super(FrmStudents, self).initProperties()
		self.NameBase = "frmStudents"
		self.Caption = "Students"
		self.SelectPageClass = PagSelectStudents
		self.BrowseGridClass = GrdStudents
		self.EditPageClass = PagEditStudents


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizStudents = app.biz.Students(app.dbConnection)
			self.addBizobj(bizStudents)
		super(FrmStudents, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmStudents(Caption="Test Of FrmStudents", Testing=True)
	frm.show()
	app.start()
