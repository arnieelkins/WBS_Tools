# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdContacts(GrdBase):

	def afterInitAll(self):
		super(GrdContacts, self).afterInitAll()
		biz = self.Form.getBizobj("Contacts")

		if not biz:
			# needed for testing
			class Biz(object):
				def getColCaption(self, caption):
					return caption
			biz = Biz()



		# Delete or comment out any columns you don't want...
		self.addColumn(dabo.ui.dColumn(self, DataField="RecNo", 
				Caption=biz.getColCaption("RecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="WBSIDSRecNo", 
				Caption=biz.getColCaption("WBSIDSRecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="FirstName", 
				Caption=biz.getColCaption("FirstName"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="LastName", 
				Caption=biz.getColCaption("LastName"),
				Sortable=True, Searchable=True, Editable=False))



if __name__ == "__main__":
	from FrmContacts import FrmContacts
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmContacts):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdContacts", Testing=True)
	test = GrdContacts(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
