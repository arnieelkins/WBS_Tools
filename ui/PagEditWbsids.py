# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from PagEditBase import PagEditBase


class PagEditWbsids(PagEditBase):

	def createItems(self):
		"""Called by the datanav framework, when it is time to create the controls."""

		biz = self.Form.getBizobj("WBSIDS")
		if not biz:
			# needed for tsting
			class Biz(object):
				def getColCaption(self, caption):
					return caption
				def getColToolTip(self, tip):
					return tip
				def getColHelpText(self, txt):
					return txt
			biz = Biz()


		mainSizer = self.Sizer = dabo.ui.dSizer("v")
		gs = dabo.ui.dGridSizer(VGap=7, HGap=5, MaxCols=3)

		## Field WBSIDS.RecNo
		label = dabo.ui.dLabel(self, NameBase="lblRecNo", 
					Caption=biz.getColCaption("RecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="RecNo",
				DataSource="WBSIDS", DataField="RecNo",
				ToolTipText=biz.getColToolTip("RecNo"),
				HelpText=biz.getColHelpText("RecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field WBSIDS.WBSID
		label = dabo.ui.dLabel(self, NameBase="lblWBSID", 
					Caption=biz.getColCaption("WBSID"))
		objectRef = dabo.ui.dTextBox(self, NameBase="WBSID",
				DataSource="WBSIDS", DataField="WBSID",
				ToolTipText=biz.getColToolTip("WBSID"),
				HelpText=biz.getColHelpText("WBSID")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field WBSIDS.CongregationName
		label = dabo.ui.dLabel(self, NameBase="lblCongregationName", 
					Caption=biz.getColCaption("CongregationName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="CongregationName",
				DataSource="WBSIDS", DataField="CongregationName",
				ToolTipText=biz.getColToolTip("CongregationName"),
				HelpText=biz.getColHelpText("CongregationName")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		gs.setColExpand(True, 1)

		mainSizer.insert(0, gs, "expand", 1, border=20)

		# Add top and bottom margins
		mainSizer.insert( 0, (-1, 10), 0)
		mainSizer.append( (-1, 20), 0)

		self.Sizer.layout()
		self.itemsCreated = True

		super(PagEditWbsids, self).createItems()


if __name__ == "__main__":
	from FrmWbsids import FrmWbsids
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmWbsids):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagEditWbsids", Testing=True)
	test = PagEditWbsids(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
