# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdContacts import GrdContacts
from PagSelectContacts import PagSelectContacts
from PagEditContacts import PagEditContacts


class FrmContacts(FrmBase):

	def initProperties(self):
		super(FrmContacts, self).initProperties()
		self.NameBase = "frmContacts"
		self.Caption = "Contacts"
		self.SelectPageClass = PagSelectContacts
		self.BrowseGridClass = GrdContacts
		self.EditPageClass = PagEditContacts


	def afterInit(self):
		if not self.Testing:
			# Instantiate the bizobj and register it with dForm, and then let the
			# superclass take over.
			app = self.Application
			bizContacts = app.biz.Contacts(app.dbConnection)
			self.addBizobj(bizContacts)
		super(FrmContacts, self).afterInit()


if __name__ == "__main__":
	app = dApp(MainFormClass=None)
	app.setup()
	frm = FrmContacts(Caption="Test Of FrmContacts", Testing=True)
	frm.show()
	app.start()
