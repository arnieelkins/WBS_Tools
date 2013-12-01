# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdGrades import GrdGrades
from PagSelectGrades import PagSelectGrades
from PagEditGrades import PagEditGrades


class FrmGrades(FrmBase):

	def initProperties(self):
		super(FrmGrades, self).initProperties()
		self.NameBase = "frmGrades"
		self.Caption = "Grades"
		self.SelectPageClass = PagSelectGrades
		self.BrowseGridClass = GrdGrades
		self.EditPageClass = PagEditGrades


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizGrades = app.biz.Grades(app.dbConnection)
			self.addBizobj(bizGrades)
		super(FrmGrades, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmGrades(Caption="Test Of FrmGrades", Testing=True)
	frm.show()
	app.start()
