# -*- coding: utf-8 -*-

import dabo.ui
import dabo.dEvents as dEvents
from dabo.ui.dialogs.PreferenceDialog import PreferenceDialog


class MenEditPrefs(dabo.ui.dMenu):

	def initProperties(self):
		super(MenEditPrefs, self).initProperties()
		self.Caption = "Preferences"
		self.HelpText = "Set/clear preference database entries for directories used by the program"
		self.MenuID = "prefs"


	def afterInit(self):
		app = self.Application
		autoHotKeys = False
		prefItem = dabo.ui.dMenuItem(self, Caption=self.Caption, HelpText=self.HelpText)
		prefItem.bindEvent(dEvents.Hit, self.openPrefs)
		self.appendItem(prefItem)


	def openPrefs(self, evt):
		app = self.Application
		mainForm = app.MainForm
		dialog = PreferenceDialog()
		dialog.SaveRestorePosition = True
		dialog.FontSize = app.PreferenceManager.getValue('fontsize')
		dialog.pm = app.PreferenceManager
		prefPage = dialog.addCategory("Prefs", pos=0)
		downloadDirLabel = dabo.ui.dLabel(prefPage, Caption = 'Download Directory')
		prefPage.Sizer.append(downloadDirLabel, layout="expand")
		downloadDir = dabo.ui.dTextBox(prefPage, Caption = 'Download Directory', DataSource = dialog.pm, DataField = 'downloaddir', RegID = "downloadDirTextBox")
		prefPage.Sizer.append(downloadDir, layout="expand")
		tempDirLabel = dabo.ui.dLabel(prefPage, Caption = 'Temp Directory')
		prefPage.Sizer.append(tempDirLabel, layout="expand")
		tempDir = dabo.ui.dTextBox(prefPage, Caption = 'Temp Directory', DataSource = dialog.pm, DataField = 'TempDir')
		prefPage.Sizer.append(tempDir, layout="expand")
		dialog.downloadDirTextBox.showContainingPage()
		dialog.ShowModal()
