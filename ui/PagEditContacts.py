# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from PagEditBase import PagEditBase


class PagEditContacts(PagEditBase):

	def createItems(self):
		"""Called by the datanav framework, when it is time to create the controls."""

		biz = self.Form.getBizobj("Contacts")
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

		## Field Contacts.RecNo
		label = dabo.ui.dLabel(self, NameBase="lblRecNo", 
					Caption=biz.getColCaption("RecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="RecNo",
				DataSource="Contacts", DataField="RecNo",
				ToolTipText=biz.getColToolTip("RecNo"),
				HelpText=biz.getColHelpText("RecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Contacts.WBSIDSRecNo
		label = dabo.ui.dLabel(self, NameBase="lblWBSIDSRecNo", 
					Caption=biz.getColCaption("WBSIDSRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="WBSIDSRecNo",
				DataSource="Contacts", DataField="WBSIDSRecNo",
				ToolTipText=biz.getColToolTip("WBSIDSRecNo"),
				HelpText=biz.getColHelpText("WBSIDSRecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Contacts.FirstName
		label = dabo.ui.dLabel(self, NameBase="lblFirstName", 
					Caption=biz.getColCaption("FirstName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="FirstName",
				DataSource="Contacts", DataField="FirstName",
				ToolTipText=biz.getColToolTip("FirstName"),
				HelpText=biz.getColHelpText("FirstName")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Contacts.LastName
		label = dabo.ui.dLabel(self, NameBase="lblLastName", 
					Caption=biz.getColCaption("LastName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="LastName",
				DataSource="Contacts", DataField="LastName",
				ToolTipText=biz.getColToolTip("LastName"),
				HelpText=biz.getColHelpText("LastName")
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

		super(PagEditContacts, self).createItems()


if __name__ == "__main__":
	from FrmContacts import FrmContacts
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmContacts):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagEditContacts", Testing=True)
	test = PagEditContacts(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
