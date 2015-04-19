# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dCheckBox-dPanel-828
def onHit(self, evt):
	#box D
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-357
def onHit(self, evt):
	# Incomplete box (4)
	if self.Form.IncompleteCheckBox.Value == True:
		if self.Form.FailedCheckBox.Value == True:
			self.Form.FailedCheckBox.Value = False
			self.Form.FailedCheckBox.raiseEvent(dabo.dEvents.Hit)
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-823
def onHit(self, evt):
	#box B
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-629
def onHit(self, evt):
	#box X
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel
def onHit(self, evt):
	# Greeting box (1)
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-800
def onHit(self, evt):
	# Failed box (3)
	if self.Form.FailedCheckBox.Value == True:
		if self.Form.IncompleteCheckBox.Value == True:
			self.Form.IncompleteCheckBox.Value = False
			self.Form.IncompleteCheckBox.raiseEvent(dabo.dEvents.Hit)
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-403
def onHit(self, evt):
	#box Z
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dButton-dScrollPanel-589
def onHit(self, evt):
	#cancel button
	self.Form.Accepted = False
	self.Form.hide()



## *!* ## Dabo Code ID: dCheckBox-dPanel-343
def onHit(self, evt):
	#box R
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-425
def onHit(self, evt):
	#box J
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-684
def onHit(self, evt):
	# Closing box (2)
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-995
def onHit(self, evt):
	#box V
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dTextBox-dPanel
def _delActiveCommentString(self):
	return


def _getActiveCommentString(self):
	try:
		return self._activeCommentString
	except AttributeError:
		return None


def _setActiveCommentString(self, val):
	self._activeCommentString = val
	self.Value = self._activeCommentString


def delActiveCommentString(self):
	return


def getActiveCommentString(self):
	try:
		return self._activeCommentString
	except AttributeError:
		return None


def setActiveCommentString(self, val):
	self._activeCommentString = val



## *!* ## Dabo Code ID: dCheckBox-dPanel-461
def onHit(self, evt):
	#box C
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-892
def onHit(self, evt):
	#box O
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-429
def onHit(self, evt):
	#box I
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-566
def onHit(self, evt):
	#box U
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-219
def onHit(self, evt):
	#box R
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-334
def onHit(self, evt):
	#box Y
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-605
def onHit(self, evt):
	#box N
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-339
def onHit(self, evt):
	#box L
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dScrollPanel-dPanel
def initProperties(self):
	app = self.Application
	import wx
	self._addWindowStyleFlag(wx.ALWAYS_SHOW_SB)
	self.Icon = "icons/wbs.ico"



## *!* ## Dabo Code ID: dDialog-top
def afterInitAll(self):
	#dDialog
	import wx
	#self.ScrollPanel._addWindowStyleFlag(wx.ALWAYS_SHOW_SB)
	#self.ScrollPanel.update()
	#self.ScrollPanel.refresh()
	self.Accepted = False
	self.GreetingEditBoxSizer = self.GreetingEditBox.ControllingSizer
	print self.GreetingEditBoxSizer
	self.CommentSizer = self.GreetingEditBoxSizer.ControllingSizer
	print self.CommentSizer
	self.letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
				'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4']
	self.BorderSizerList = []
	for letter in self.letterList:
		newBorderSizer = dabo.ui.dBorderSizer(self.ScrollPanel, Caption = letter, Orientation='Vertical', Visible = False)
		if newBorderSizer.Caption == '1':
			newBorderSizer.Caption = 'Greeting'
		elif newBorderSizer.Caption == '2':
			newBorderSizer.Caption = 'Closing'
		if newBorderSizer.Caption == '3':
			newBorderSizer.Caption = 'Failed'
		elif newBorderSizer.Caption == '4':
			newBorderSizer.Caption = 'Incomplete'
		newEditBox = dabo.ui.uiwx.dEditBox(self.ScrollPanel, Visible = False, MinimumSize = (500, 200))
		newBorderSizer.append(newEditBox, layout = 'expand', proportion = 1, halign = 'right')
		for item in self.CommentDictList:
			if item['Name'] == letter:
				newEditBox.Value = item['Comment']
				self.BorderSizerList.append(newBorderSizer)
	if self.FailedCheckBox.Value == True:
		self.FailedCheckBox.raiseEvent(dabo.dEvents.Hit)
	if self.IncompleteCheckBox.Value == True:
		self.IncompleteCheckBox.raiseEvent(dabo.dEvents.Hit)


def buildCommentDictList(self, bizobj):
	app = self.Application
	self.CommentDictList = [{'Name':'A','Caption':'A','Comment':'','Box':self.dCheckBoxA},
							{'Name':'B','Caption':'B','Comment':'','Box':self.dCheckBoxB},
							{'Name':'C','Caption':'C','Comment':'','Box':self.dCheckBoxC},
							{'Name':'D','Caption':'D','Comment':'','Box':self.dCheckBoxD},
							{'Name':'E','Caption':'E','Comment':'','Box':self.dCheckBoxE},
							{'Name':'F','Caption':'F','Comment':'','Box':self.dCheckBoxF},
							{'Name':'G','Caption':'G','Comment':'','Box':self.dCheckBoxG},
							{'Name':'H','Caption':'H','Comment':'','Box':self.dCheckBoxH},
							{'Name':'I','Caption':'I','Comment':'','Box':self.dCheckBoxI},
							{'Name':'J','Caption':'J','Comment':'','Box':self.dCheckBoxJ},
							{'Name':'K','Caption':'K','Comment':'','Box':self.dCheckBoxK},
							{'Name':'L','Caption':'L','Comment':'','Box':self.dCheckBoxL},
							{'Name':'M','Caption':'M','Comment':'','Box':self.dCheckBoxM},
							{'Name':'N','Caption':'N','Comment':'','Box':self.dCheckBoxN},
							{'Name':'O','Caption':'O','Comment':'','Box':self.dCheckBoxO},
							{'Name':'P','Caption':'P','Comment':'','Box':self.dCheckBoxP},
							{'Name':'Q','Caption':'Q','Comment':'','Box':self.dCheckBoxQ},
							{'Name':'R','Caption':'R','Comment':'','Box':self.dCheckBoxR},
							{'Name':'S','Caption':'S','Comment':'','Box':self.dCheckBoxS},
							{'Name':'T','Caption':'T','Comment':'','Box':self.dCheckBoxT},
							{'Name':'U','Caption':'U','Comment':'','Box':self.dCheckBoxU},
							{'Name':'V','Caption':'V','Comment':'','Box':self.dCheckBoxV},
							{'Name':'W','Caption':'W','Comment':'','Box':self.dCheckBoxW},
							{'Name':'X','Caption':'X','Comment':'','Box':self.dCheckBoxX},
							{'Name':'Y','Caption':'Y','Comment':'','Box':self.dCheckBoxY},
							{'Name':'Z','Caption':'Z','Comment':'','Box':self.dCheckBoxZ},
							{'Name':'1','Caption':self.lessonShortName + 'Greeting','Comment':'','Box':self.GreetingCheckBox},
							{'Name':'2','Caption':self.lessonShortName + 'Closing','Comment':'','Box':self.ClosingCheckBox},
							{'Name':'3','Caption':'Failed','Comment':'','Box':self.FailedCheckBox},
							{'Name':'4','Caption':'Incomplete','Comment':'','Box':self.IncompleteCheckBox},
							]
	self.lookupComments(self.CommentDictList, bizobj, self.TextTags)
	for item in self.CommentDictList:
		box = item['Box']
		box.Tag == item['Name']
		box.Caption = item['Caption']
		box.ToolTipText = item['Comment']
		if box.ToolTipText == '':
			box.Visible = False


def clearCommentCheckBoxes(self):
	app = self.Application
	for box in self.CommentCheckBoxList:
		box.Value = False
	self.refresh()


def initProperties(self):
	app = self.Application
	self.BasePrefKey = app.BasePrefKey
	self.bizobj = None
	self.BorderResizable = True
	self.FontSize = app.PreferenceManager.getValue('fontsize')
	# self.ActiveCommentDict is a list of dictionaries, each of which will hold information
	# on one of the currently selected comments
	self.ActiveCommentDict = []
	self.MinimumSize = (720, 600)
	#self.Centered = True


def lookupComments(self, dictList, bizObj, tagDict):
	print "lookupComments is running\n"
	if len(dictList) >= 1:
		tempCursor = bizObj.getTempCursor()
		tempString = '('
		for item in dictList:
			tempString = tempString + "'" + item['Caption'] + "',"
		tempString = tempString[0:-1] + ")"
		tempCursor.UserSQL = 'select CommentTag, CommentContent from Comments where CommentTag in ' + tempString
		tempCursor.requery()
		for item in dictList:
			for record in tempCursor:
				if item['Caption'] == record['CommentTag']:
					thisComment = record['CommentContent']
					# replace any tags in the comment with the actual values
					for key in tagDict:
						if key in thisComment:
							thisComment = thisComment.replace(key, tagDict[key])
					item['Comment'] = thisComment



def processSelected(self, evt):
	app = self.Application
	source = evt.EventObject
	# is box checked?
	if 'dCheckBox' in str(type(source)):
		print 'source = ' + str(source)
		letter = str(source.Tag)
		print 'letter = ' + letter
		if source.Value:
			# box is checked, add letter to active comments
			activeComments = self.ActiveCommentTextBox.getActiveCommentString()
			print 'activeComments = ' + str(activeComments) + ' which is of type ' + str(type(activeComments))
			print 'letter = ' + str(letter) + ' which is of type ' + str(type(letter))
			activeComments = activeComments + letter
			self.ActiveCommentTextBox.setActiveCommentString(activeComments)
			self.ActiveCommentTextBox.update()
			print 'self.CommentSizer.ChildObjects = ' + str(self.CommentSizer.ChildObjects) + '\n'
			for item in self.CommentSizer.ChildObjects:
				print 'CommentSizer child = '
				print item
				print '\n'
				self.CommentSizer.remove(item)
			print 'self.CommentSizer.ChildObjects = ' + str(self.CommentSizer.ChildObjects) + '\n'
			foundIt = False
			print "=================================\n"
			print 'about to search ActiveCommentDict\n'
			print 'ActiveCommentDict = ' + str(self.ActiveCommentDict)
			for dict in self.ActiveCommentDict:
				print 'dict["letter"] = ' + str(dict["letter"])
				if dict['letter'] == letter:
					foundIt = True
					print "foundIt!"
					dict['control'].ControllingSizer.Visible = True
					dict['control'].Visible = True
					break
			if not foundIt:
				# set the dictionary entry to control = borderSizer, comment = check
				print 'did not find it!'
				newDict = {}
				newDict['letter'] = letter
				borderSizerIndex = self.letterList.index(letter)
				print 'borderSizerIndex = ' 
				print borderSizerIndex
				editBox = self.BorderSizerList[borderSizerIndex].ChildObjects[0]
				newDict['control'] = editBox
				newDict['comment'] = editBox.Value
				self.ActiveCommentDict.append(newDict)
				editBox.ControllingSizer.Visible = True
				editBox.Visible = True
			for dict in self.ActiveCommentDict:
				dict['control'].ReadOnly = True
				self.CommentSizer.append(dict['control'].ControllingSizer, layout='expand', proportion = 1, halign = 'right')
				self.CommentSizer.setItemProps(dict['control'], {'BorderSides': ['All'], 'Proportion': 1, 'HAlign': 'Center', 'VAlign': 'Top', 'Border': 0, 'Expand': True})
			self.CommentSizer.layout()
			self.layout()
			self.update()
			self.refresh()

		else:
			# box is not checked, remove letter from active comments
			#print 'dCheckBox is NOT checked\n'
			activeComments = self.ActiveCommentTextBox.getActiveCommentString()
			# find the position of the letter in the activeComments string
			stringPosition = activeComments.find(letter)
			print 'stringPosition = ' + str(stringPosition)
			#print 'activeComments = ' + activeComments
			activeComments = activeComments.replace(letter, '')
			#print 'activeComments = ' + activeComments
			self.ActiveCommentTextBox.setActiveCommentString(activeComments)
			self.ActiveCommentTextBox.update()
			print self.CommentSizer.listMembers()
			control = self.CommentSizer.GetItem(stringPosition)
			control.Visible = False
			self.CommentSizer.Detach(stringPosition)
			self.CommentSizer.layout()
			# remove the comment from the dictlist by making a copy of the list and
			# adding all the items except the one we are removing.  For the one being
			# removed, set the EditBox and the ControllingSizer to not be visible
			tempList = []
			for item in self.ActiveCommentDict:
				print item
				if item['letter'] == letter:
					item['control'].ControllingSizer.Visible = False
					item['control'].Visible = False
				else:
					tempList.append(item)
			self.ActiveCommentDict = tempList
			self.layout()
			self.update()
			self.refresh()



## *!* ## Dabo Code ID: dCheckBox-dPanel-791
def onHit(self, evt):
	#box T
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-793
def onHit(self, evt):
	#box E
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-795
def onHit(self, evt):
	#box S
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-63
def onHit(self, evt):
	#box W
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-516
def onHit(self, evt):
	#box M
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-775
def onHit(self, evt):
	#box A
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-691
def onHit(self, evt):
	#box F
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dButton-dScrollPanel
def onHit(self, evt):
	#OK button
	# build list of comments for calling form
	# then hide this form until the calling form destroys it
	self.Form.CommentString = self.Form.ActiveCommentTextBox.Value
	self.Form.Accepted = True
	self.Form.hide()



## *!* ## Dabo Code ID: dCheckBox-dPanel-884
def onHit(self, evt):
	#box G
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-307
def onHit(self, evt):
	#box P
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-90
def onHit(self, evt):
	#box K
	self.Form.processSelected(evt)



## *!* ## Dabo Code ID: dCheckBox-dPanel-894
def onHit(self, evt):
	#box H
	self.Form.processSelected(evt)


