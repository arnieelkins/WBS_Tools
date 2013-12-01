# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdStudents(GrdBase):

	def afterInitAll(self):
		super(GrdStudents, self).afterInitAll()
		biz = self.Form.getBizobj("Students")

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

		self.addColumn(dabo.ui.dColumn(self, DataField="StudentID", 
				Caption=biz.getColCaption("StudentID"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="WBSIDSRecNo", 
				Caption=biz.getColCaption("WBSIDSRecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="TeachersRecNo", 
				Caption=biz.getColCaption("TeachersRecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="ContactsRecNo", 
				Caption=biz.getColCaption("ContactsRecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="FirstName", 
				Caption=biz.getColCaption("FirstName"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="LastName", 
				Caption=biz.getColCaption("LastName"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Age", 
				Caption=biz.getColCaption("Age"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Birthdate", 
				Caption=biz.getColCaption("Birthdate"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Gender", 
				Caption=biz.getColCaption("Gender"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="MaritalStatus", 
				Caption=biz.getColCaption("MaritalStatus"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Religion", 
				Caption=biz.getColCaption("Religion"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="ChurchName", 
				Caption=biz.getColCaption("ChurchName"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="WBSBefore", 
				Caption=biz.getColCaption("WBSBefore"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Country", 
				Caption=biz.getColCaption("Country"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="State", 
				Caption=biz.getColCaption("State"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="City", 
				Caption=biz.getColCaption("City"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="PostalAddress", 
				Caption=biz.getColCaption("PostalAddress"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="EmailAddress", 
				Caption=biz.getColCaption("EmailAddress"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Phone1", 
				Caption=biz.getColCaption("Phone1"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Phone2", 
				Caption=biz.getColCaption("Phone2"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="StreetAddress", 
				Caption=biz.getColCaption("StreetAddress"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Occupation", 
				Caption=biz.getColCaption("Occupation"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="HasBeenBaptized", 
				Caption=biz.getColCaption("HasBeenBaptized"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="TypeOfBaptism", 
				Caption=biz.getColCaption("TypeOfBaptism"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="RequestedBaptism", 
				Caption=biz.getColCaption("RequestedBaptism"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Bible", 
				Caption=biz.getColCaption("Bible"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Notes", 
				Caption=biz.getColCaption("Notes"),
				Sortable=True, Searchable=True, Editable=False))



if __name__ == "__main__":
	from FrmStudents import FrmStudents
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmStudents):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdStudents", Testing=True)
	test = GrdStudents(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
