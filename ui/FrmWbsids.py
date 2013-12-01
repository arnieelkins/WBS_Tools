# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdWbsids import GrdWbsids
from PagSelectWbsids import PagSelectWbsids
from PagEditWbsids import PagEditWbsids


class FrmWbsids(FrmBase):

	def initProperties(self):
		super(FrmWbsids, self).initProperties()
		self.NameBase = "frmWbsids"
		self.Caption = "Wbsids"
		self.SelectPageClass = PagSelectWbsids
		self.BrowseGridClass = GrdWbsids
		self.EditPageClass = PagEditWbsids


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizWbsids = app.biz.Wbsids(app.dbConnection)
			self.addBizobj(bizWbsids)
		super(FrmWbsids, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmWbsids(Caption="Test Of FrmWbsids", Testing=True)
	frm.show()
	app.start()
