# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from PagEditBase import PagEditBase


class PagEditLessons(PagEditBase):

	def createItems(self):
		"""Called by the datanav framework, when it is time to create the controls."""

		biz = self.Form.getBizobj("Lessons")
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

		## Field Lessons.RecNo
		label = dabo.ui.dLabel(self, NameBase="lblRecNo", 
					Caption=biz.getColCaption("RecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="RecNo",
				DataSource="Lessons", DataField="RecNo",
				ToolTipText=biz.getColToolTip("RecNo"),
				HelpText=biz.getColHelpText("RecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Lessons.Name
		label = dabo.ui.dLabel(self, NameBase="lblName", 
					Caption=biz.getColCaption("Name"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Name",
				DataSource="Lessons", DataField="Name",
				ToolTipText=biz.getColToolTip("Name"),
				HelpText=biz.getColHelpText("Name")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Lessons.ShortName
		label = dabo.ui.dLabel(self, NameBase="lblShortName", 
					Caption=biz.getColCaption("ShortName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="ShortName",
				DataSource="Lessons", DataField="ShortName",
				ToolTipText=biz.getColToolTip("ShortName"),
				HelpText=biz.getColHelpText("ShortName")
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

		super(PagEditLessons, self).createItems()


if __name__ == "__main__":
	from FrmLessons import FrmLessons
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmLessons):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagEditLessons", Testing=True)
	test = PagEditLessons(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
