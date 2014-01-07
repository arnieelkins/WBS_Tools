# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPanel-135
def onHit(self, evt):
	import os
	app = self.Application
	reportList = []
	checkBoxDict = {self.Form.IntroCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "IntroGradingForm.rfxml"),
									self.Form.GHSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml"),
									self.Form.TIGNCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml"),
									self.Form.KJCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml"),
									self.Form.FOGCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml"),
									self.Form.BWSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml"),
									self.Form.LLLCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml")}
	for checkBox in checkBoxDict.keys():
		if checkBox.Value == True:
			reportList.append(checkBoxDict[checkBox])
	for report in reportList:
		self.Form.ReportForm = report
		self.Form.runReport("print")
	self.Form.safeDestroy()



## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
	import os
	app = self.Application
	reportList = []
	checkBoxDict = {self.Form.IntroCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "IntroGradingForm.rfxml"),
									self.Form.GHSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "GHSGradingForm.rfxml"),
									self.Form.TIGNCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "TIGNGradingForm.rfxml"),
									self.Form.KJCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "KJGradingForm.rfxml"),
									self.Form.FOGCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "FOGGradingForm.rfxml"),
									self.Form.BWSCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "BWSGradingForm.rfxml"),
									self.Form.LLLCheckBox:os.path.join(app.HomeDirectory, "reports" + os.sep + "LLLGradingForm.rfxml")}
	for checkBox in checkBoxDict.keys():
		if checkBox.Value == True:
			reportList.append(checkBoxDict[checkBox])
	for report in reportList:
		self.Form.ReportForm = report
		self.Form.runReport("preview")
	self.Form.safeDestroy()


