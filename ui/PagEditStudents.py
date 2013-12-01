# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from PagEditBase import PagEditBase


class PagEditStudents(PagEditBase):

	def createItems(self):
		"""Called by the datanav framework, when it is time to create the controls."""

		biz = self.Form.getBizobj("Students")
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

		## Field Students.RecNo
		label = dabo.ui.dLabel(self, NameBase="lblRecNo", 
					Caption=biz.getColCaption("RecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="RecNo",
				DataSource="Students", DataField="RecNo",
				ToolTipText=biz.getColToolTip("RecNo"),
				HelpText=biz.getColHelpText("RecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.StudentID
		label = dabo.ui.dLabel(self, NameBase="lblStudentID", 
					Caption=biz.getColCaption("StudentID"))
		objectRef = dabo.ui.dTextBox(self, NameBase="StudentID",
				DataSource="Students", DataField="StudentID",
				ToolTipText=biz.getColToolTip("StudentID"),
				HelpText=biz.getColHelpText("StudentID")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.WBSIDSRecNo
		label = dabo.ui.dLabel(self, NameBase="lblWBSIDSRecNo", 
					Caption=biz.getColCaption("WBSIDSRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="WBSIDSRecNo",
				DataSource="Students", DataField="WBSIDSRecNo",
				ToolTipText=biz.getColToolTip("WBSIDSRecNo"),
				HelpText=biz.getColHelpText("WBSIDSRecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.TeachersRecNo
		label = dabo.ui.dLabel(self, NameBase="lblTeachersRecNo", 
					Caption=biz.getColCaption("TeachersRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="TeachersRecNo",
				DataSource="Students", DataField="TeachersRecNo",
				ToolTipText=biz.getColToolTip("TeachersRecNo"),
				HelpText=biz.getColHelpText("TeachersRecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.ContactsRecNo
		label = dabo.ui.dLabel(self, NameBase="lblContactsRecNo", 
					Caption=biz.getColCaption("ContactsRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="ContactsRecNo",
				DataSource="Students", DataField="ContactsRecNo",
				ToolTipText=biz.getColToolTip("ContactsRecNo"),
				HelpText=biz.getColHelpText("ContactsRecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.FirstName
		label = dabo.ui.dLabel(self, NameBase="lblFirstName", 
					Caption=biz.getColCaption("FirstName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="FirstName",
				DataSource="Students", DataField="FirstName",
				ToolTipText=biz.getColToolTip("FirstName"),
				HelpText=biz.getColHelpText("FirstName")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.LastName
		label = dabo.ui.dLabel(self, NameBase="lblLastName", 
					Caption=biz.getColCaption("LastName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="LastName",
				DataSource="Students", DataField="LastName",
				ToolTipText=biz.getColToolTip("LastName"),
				HelpText=biz.getColHelpText("LastName")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Age
		label = dabo.ui.dLabel(self, NameBase="lblAge", 
					Caption=biz.getColCaption("Age"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Age",
				DataSource="Students", DataField="Age",
				ToolTipText=biz.getColToolTip("Age"),
				HelpText=biz.getColHelpText("Age")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Birthdate
		label = dabo.ui.dLabel(self, NameBase="lblBirthdate", 
					Caption=biz.getColCaption("Birthdate"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Birthdate",
				DataSource="Students", DataField="Birthdate",
				ToolTipText=biz.getColToolTip("Birthdate"),
				HelpText=biz.getColHelpText("Birthdate")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Gender
		label = dabo.ui.dLabel(self, NameBase="lblGender", 
					Caption=biz.getColCaption("Gender"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Gender",
				DataSource="Students", DataField="Gender",
				ToolTipText=biz.getColToolTip("Gender"),
				HelpText=biz.getColHelpText("Gender")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.MaritalStatus
		label = dabo.ui.dLabel(self, NameBase="lblMaritalStatus", 
					Caption=biz.getColCaption("MaritalStatus"))
		objectRef = dabo.ui.dTextBox(self, NameBase="MaritalStatus",
				DataSource="Students", DataField="MaritalStatus",
				ToolTipText=biz.getColToolTip("MaritalStatus"),
				HelpText=biz.getColHelpText("MaritalStatus")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Religion
		label = dabo.ui.dLabel(self, NameBase="lblReligion", 
					Caption=biz.getColCaption("Religion"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Religion",
				DataSource="Students", DataField="Religion",
				ToolTipText=biz.getColToolTip("Religion"),
				HelpText=biz.getColHelpText("Religion")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.ChurchName
		label = dabo.ui.dLabel(self, NameBase="lblChurchName", 
					Caption=biz.getColCaption("ChurchName"))
		objectRef = dabo.ui.dTextBox(self, NameBase="ChurchName",
				DataSource="Students", DataField="ChurchName",
				ToolTipText=biz.getColToolTip("ChurchName"),
				HelpText=biz.getColHelpText("ChurchName")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.WBSBefore
		label = dabo.ui.dLabel(self, NameBase="lblWBSBefore", 
					Caption=biz.getColCaption(""))
		objectRef = dabo.ui.dCheckBox(self, NameBase="WBSBefore",
				DataSource="Students", DataField="WBSBefore", Caption=biz.getColCaption("WBSBefore"),
				ToolTipText=biz.getColToolTip("WBSBefore"),
				HelpText=biz.getColHelpText("WBSBefore")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Country
		label = dabo.ui.dLabel(self, NameBase="lblCountry", 
					Caption=biz.getColCaption("Country"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Country",
				DataSource="Students", DataField="Country",
				ToolTipText=biz.getColToolTip("Country"),
				HelpText=biz.getColHelpText("Country")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.State
		label = dabo.ui.dLabel(self, NameBase="lblState", 
					Caption=biz.getColCaption("State"))
		objectRef = dabo.ui.dTextBox(self, NameBase="State",
				DataSource="Students", DataField="State",
				ToolTipText=biz.getColToolTip("State"),
				HelpText=biz.getColHelpText("State")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.City
		label = dabo.ui.dLabel(self, NameBase="lblCity", 
					Caption=biz.getColCaption("City"))
		objectRef = dabo.ui.dTextBox(self, NameBase="City",
				DataSource="Students", DataField="City",
				ToolTipText=biz.getColToolTip("City"),
				HelpText=biz.getColHelpText("City")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.PostalAddress
		label = dabo.ui.dLabel(self, NameBase="lblPostalAddress", 
					Caption=biz.getColCaption("PostalAddress"))
		objectRef = dabo.ui.dTextBox(self, NameBase="PostalAddress",
				DataSource="Students", DataField="PostalAddress",
				ToolTipText=biz.getColToolTip("PostalAddress"),
				HelpText=biz.getColHelpText("PostalAddress")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.EmailAddress
		label = dabo.ui.dLabel(self, NameBase="lblEmailAddress", 
					Caption=biz.getColCaption("EmailAddress"))
		objectRef = dabo.ui.dTextBox(self, NameBase="EmailAddress",
				DataSource="Students", DataField="EmailAddress",
				ToolTipText=biz.getColToolTip("EmailAddress"),
				HelpText=biz.getColHelpText("EmailAddress")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Phone1
		label = dabo.ui.dLabel(self, NameBase="lblPhone1", 
					Caption=biz.getColCaption("Phone1"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Phone1",
				DataSource="Students", DataField="Phone1",
				ToolTipText=biz.getColToolTip("Phone1"),
				HelpText=biz.getColHelpText("Phone1")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Phone2
		label = dabo.ui.dLabel(self, NameBase="lblPhone2", 
					Caption=biz.getColCaption("Phone2"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Phone2",
				DataSource="Students", DataField="Phone2",
				ToolTipText=biz.getColToolTip("Phone2"),
				HelpText=biz.getColHelpText("Phone2")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.StreetAddress
		label = dabo.ui.dLabel(self, NameBase="lblStreetAddress", 
					Caption=biz.getColCaption("StreetAddress"))
		objectRef = dabo.ui.dTextBox(self, NameBase="StreetAddress",
				DataSource="Students", DataField="StreetAddress",
				ToolTipText=biz.getColToolTip("StreetAddress"),
				HelpText=biz.getColHelpText("StreetAddress")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Occupation
		label = dabo.ui.dLabel(self, NameBase="lblOccupation", 
					Caption=biz.getColCaption("Occupation"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Occupation",
				DataSource="Students", DataField="Occupation",
				ToolTipText=biz.getColToolTip("Occupation"),
				HelpText=biz.getColHelpText("Occupation")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.HasBeenBaptized
		label = dabo.ui.dLabel(self, NameBase="lblHasBeenBaptized", 
					Caption=biz.getColCaption(""))
		objectRef = dabo.ui.dCheckBox(self, NameBase="HasBeenBaptized",
				DataSource="Students", DataField="HasBeenBaptized", Caption=biz.getColCaption("HasBeenBaptized"),
				ToolTipText=biz.getColToolTip("HasBeenBaptized"),
				HelpText=biz.getColHelpText("HasBeenBaptized")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.TypeOfBaptism
		label = dabo.ui.dLabel(self, NameBase="lblTypeOfBaptism", 
					Caption=biz.getColCaption("TypeOfBaptism"))
		objectRef = dabo.ui.dTextBox(self, NameBase="TypeOfBaptism",
				DataSource="Students", DataField="TypeOfBaptism",
				ToolTipText=biz.getColToolTip("TypeOfBaptism"),
				HelpText=biz.getColHelpText("TypeOfBaptism")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.RequestedBaptism
		label = dabo.ui.dLabel(self, NameBase="lblRequestedBaptism", 
					Caption=biz.getColCaption(""))
		objectRef = dabo.ui.dCheckBox(self, NameBase="RequestedBaptism",
				DataSource="Students", DataField="RequestedBaptism", Caption=biz.getColCaption("RequestedBaptism"),
				ToolTipText=biz.getColToolTip("RequestedBaptism"),
				HelpText=biz.getColHelpText("RequestedBaptism")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Bible
		label = dabo.ui.dLabel(self, NameBase="lblBible", 
					Caption=biz.getColCaption(""))
		objectRef = dabo.ui.dCheckBox(self, NameBase="Bible",
				DataSource="Students", DataField="Bible", Caption=biz.getColCaption("Bible"),
				ToolTipText=biz.getColToolTip("Bible"),
				HelpText=biz.getColHelpText("Bible")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Students.Notes
		label = dabo.ui.dLabel(self, NameBase="lblNotes", 
					Caption=biz.getColCaption("Notes"))
		objectRef = dabo.ui.dEditBox(self, NameBase="Notes",
				DataSource="Students", DataField="Notes",
				ToolTipText=biz.getColToolTip("Notes"),
				HelpText=biz.getColHelpText("Notes")
)

		gs.append(label, alignment=("top", "right") )
		currRow = gs.findFirstEmptyCell()[0]
		gs.setRowExpand(True, currRow)
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		gs.setColExpand(True, 1)

		mainSizer.insert(0, gs, "expand", 1, border=20)

		# Add top and bottom margins
		mainSizer.insert( 0, (-1, 10), 0)
		mainSizer.append( (-1, 20), 0)

		self.Sizer.layout()
		self.itemsCreated = True

		super(PagEditStudents, self).createItems()


if __name__ == "__main__":
	from FrmStudents import FrmStudents
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmStudents):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagEditStudents", Testing=True)
	test = PagEditStudents(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
