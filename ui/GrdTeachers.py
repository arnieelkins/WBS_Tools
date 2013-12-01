# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdTeachers(GrdBase):

	def afterInitAll(self):
		super(GrdTeachers, self).afterInitAll()
		biz = self.Form.getBizobj("Teachers")

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
	from FrmTeachers import FrmTeachers
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmTeachers):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdTeachers", Testing=True)
	test = GrdTeachers(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
