# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdWbsids(GrdBase):

	def afterInitAll(self):
		super(GrdWbsids, self).afterInitAll()
		biz = self.Form.getBizobj("WBSIDS")

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

		self.addColumn(dabo.ui.dColumn(self, DataField="WBSID", 
				Caption=biz.getColCaption("WBSID"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="CongregationName", 
				Caption=biz.getColCaption("CongregationName"),
				Sortable=True, Searchable=True, Editable=False))



if __name__ == "__main__":
	from FrmWbsids import FrmWbsids
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmWbsids):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdWbsids", Testing=True)
	test = GrdWbsids(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
