# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdTeachers import GrdTeachers
from PagSelectTeachers import PagSelectTeachers
from PagEditTeachers import PagEditTeachers


class FrmTeachers(FrmBase):

	def initProperties(self):
		super(FrmTeachers, self).initProperties()
		self.NameBase = "frmTeachers"
		self.Caption = "Teachers"
		self.SelectPageClass = PagSelectTeachers
		self.BrowseGridClass = GrdTeachers
		self.EditPageClass = PagEditTeachers


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizTeachers = app.biz.Teachers(app.dbConnection)
			self.addBizobj(bizTeachers)
		super(FrmTeachers, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmTeachers(Caption="Test Of FrmTeachers", Testing=True)
	frm.show()
	app.start()
