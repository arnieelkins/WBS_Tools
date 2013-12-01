# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdLessons import GrdLessons
from PagSelectLessons import PagSelectLessons
from PagEditLessons import PagEditLessons


class FrmLessons(FrmBase):

	def initProperties(self):
		super(FrmLessons, self).initProperties()
		self.NameBase = "frmLessons"
		self.Caption = "Lessons"
		self.SelectPageClass = PagSelectLessons
		self.BrowseGridClass = GrdLessons
		self.EditPageClass = PagEditLessons


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizLessons = app.biz.Lessons(app.dbConnection)
			self.addBizobj(bizLessons)
		super(FrmLessons, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmLessons(Caption="Test Of FrmLessons", Testing=True)
	frm.show()
	app.start()
