# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPanel-821
def onHit(self, evt):
	self.Form.next()



## *!* ## Dabo Code ID: dButton-dPanel-194
def onHit(self, evt):
	self.Form.save()



## *!* ## Dabo Code ID: dButton-dPanel-359
def onHit(self, evt):
	self.Form.first()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	self.Form.requery()



## *!* ## Dabo Code ID: dForm-top
def afterInitAll(self):
	self.setupMenu()
	self.requery()


def createBizobjs(self):
	app = self.Application

	gradesBizobj = app.biz.GradesBizobj(app.dbConnection)
	self.addBizobj(gradesBizobj)


def fillFileOpenMenu(self):
	from ui.MenFileOpen import MenFileOpen
	"""Add the File|Open menu, with menu items for opening each form."""
	app = self.Application
	fileMenu = self.MenuBar.getMenu("base_file")
	fileMenu.prependMenu(MenFileOpen(fileMenu))


def fillReportsMenu(self):
	"""Add the Reports menu."""
	from dabo.dLocalize import _
	app = self.Application
	from ui.MenReports import MenReports
	menReports = MenReports()

	# We want the reports menu right after the View menu:
	idx = self.MenuBar.getMenuIndex(_("View"))
	if idx is None:
		# punt:
		idx = 2
	idx += 1
	self.MenuBar.insertMenu(idx, menReports)


def initProperties(self):
	self.SaveRestorePosition = True
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue("fontsize")


def setupMenu(self):
	self.fillFileOpenMenu()
	self.fillReportsMenu()



## *!* ## Dabo Code ID: dButton-dPanel-282
def onHit(self, evt):
	self.Form.last()



## *!* ## Dabo Code ID: dButton-dPanel-944
def onHit(self, evt):
	self.Form.prior()


