# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdGrades(GrdBase):

	def afterInitAll(self):
		super(GrdGrades, self).afterInitAll()
		biz = self.Form.getBizobj("Grades")

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

		self.addColumn(dabo.ui.dColumn(self, DataField="Date", 
				Caption=biz.getColCaption("Date"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="LessonsRecNo", 
				Caption=biz.getColCaption("LessonsRecNo"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="Score", 
				Caption=biz.getColCaption("Score"),
				Sortable=True, Searchable=True, Editable=False))

		self.addColumn(dabo.ui.dColumn(self, DataField="StudentsRecNo", 
				Caption=biz.getColCaption("StudentsRecNo"),
				Sortable=True, Searchable=True, Editable=False))



if __name__ == "__main__":
	from FrmGrades import FrmGrades
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmGrades):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of GrdGrades", Testing=True)
	test = GrdGrades(frm)
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
