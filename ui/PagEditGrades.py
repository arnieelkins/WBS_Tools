# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from PagEditBase import PagEditBase


class PagEditGrades(PagEditBase):

	def createItems(self):
		"""Called by the datanav framework, when it is time to create the controls."""

		biz = self.Form.getBizobj("Grades")
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

		## Field Grades.RecNo
		label = dabo.ui.dLabel(self, NameBase="lblRecNo", 
					Caption=biz.getColCaption("RecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="RecNo",
				DataSource="Grades", DataField="RecNo",
				ToolTipText=biz.getColToolTip("RecNo"),
				HelpText=biz.getColHelpText("RecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Grades.Date
		label = dabo.ui.dLabel(self, NameBase="lblDate", 
					Caption=biz.getColCaption("Date"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Date",
				DataSource="Grades", DataField="Date",
				ToolTipText=biz.getColToolTip("Date"),
				HelpText=biz.getColHelpText("Date")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Grades.LessonsRecNo
		label = dabo.ui.dLabel(self, NameBase="lblLessonsRecNo", 
					Caption=biz.getColCaption("LessonsRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="LessonsRecNo",
				DataSource="Grades", DataField="LessonsRecNo",
				ToolTipText=biz.getColToolTip("LessonsRecNo"),
				HelpText=biz.getColHelpText("LessonsRecNo")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Grades.Score
		label = dabo.ui.dLabel(self, NameBase="lblScore", 
					Caption=biz.getColCaption("Score"))
		objectRef = dabo.ui.dTextBox(self, NameBase="Score",
				DataSource="Grades", DataField="Score",
				ToolTipText=biz.getColToolTip("Score"),
				HelpText=biz.getColHelpText("Score")
)

		gs.append(label, alignment=("top", "right") )
		gs.append(objectRef, "expand")
		gs.append( (25, 1) )

		## Field Grades.StudentsRecNo
		label = dabo.ui.dLabel(self, NameBase="lblStudentsRecNo", 
					Caption=biz.getColCaption("StudentsRecNo"))
		objectRef = dabo.ui.dTextBox(self, NameBase="StudentsRecNo",
				DataSource="Grades", DataField="StudentsRecNo",
				ToolTipText=biz.getColToolTip("StudentsRecNo"),
				HelpText=biz.getColHelpText("StudentsRecNo")
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

		super(PagEditGrades, self).createItems()


if __name__ == "__main__":
	from FrmGrades import FrmGrades
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmGrades):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagEditGrades", Testing=True)
	test = PagEditGrades(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
