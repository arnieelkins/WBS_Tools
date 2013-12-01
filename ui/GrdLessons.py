# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdLessons(GrdBase):

	def afterInitAll(self):
		super(GrdLessons, self).afterInitAll()
		biz = self.Form.getBizobj("Lessons")

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

		self.addColumn(dabo.ui.dColumn(self, DataField="Name", 
				Caption=biz.getColCaption("Name"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="ShortName", 
				Caption=biz.getColCaption("ShortName"),
				Sortable=True, Searchable=True, Editable=False))



if __name__ == "__main__":
	from FrmLessons import FrmLessons
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmLessons):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdLessons", Testing=True)
	test = GrdLessons(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
