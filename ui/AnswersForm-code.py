# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dDropdownList-dPanel
def afterInit(self):
	mybiz = self.Form.getBizobj('Lessons')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()
	self.SaveRestorePosition="True"

def onInteractiveChange(self, evt):
	self.Form.PrimaryBizobj.moveToRowNumber(self.KeyValue - 1)
	self.Form.update()



## *!* ## Dabo Code ID: dButton-dPanel-265
def onHit(self, evt):
	print self.Form.getBizobj('Lessons').getSQL()
	print self.Form.getBizobj('Answers').getSQL()
	self.Form.save()



## *!* ## Dabo Code ID: dGrid-dPanel
def afterInit(self):
	self.RowColorOdd = "azure"
	self.RowColorEven = "whitesmoke"
	self.AlternateRowColoring = True



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	self.Form.cancel()



## *!* ## Dabo Code ID: dForm-top
def initProperties(self):
	app = self.Application
	self.FontSize = app.PreferenceManager.getValue("fontsize")

def afterInitAll(self):
	self.setupMenu()
	self.requery()


def createBizobjs(self):
	app = self.Application

	lessonsBizobj = app.biz.LessonsBizobj(app.dbConnection)
	self.addBizobj(lessonsBizobj)

	answersBizobj = app.biz.AnswersBizobj(app.dbConnection)
	self.addBizobj(answersBizobj)

	lessonsBizobj.addChild(answersBizobj)


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

def setupMenu(self):

	self.fillFileOpenMenu()
	self.fillReportsMenu()


## *!* ## Dabo Code ID: dDropdownList-dPanel-309
def afterInit(self):
	mybiz = self.Form.getBizobj('Lessons')
	(self.Choices, self.Keys) = mybiz.getAvailableTypes()


