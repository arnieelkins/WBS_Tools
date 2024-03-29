# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dObject import dObject
import dabo.dEvents as dEvents
import dabo.lib.datanav as datanav

IGNORE_STRING = datanav.QRY_OPERATOR.IGNORE


# Controls for the select page:
class SelectControlMixin(dObject):
    def initProperties(self):
    	super(SelectControlMixin, self).initProperties()
    	self.SaveRestoreValue = True

class SelectTextBox(SelectControlMixin, dabo.ui.dTextBox): pass
class SelectCheckBox(SelectControlMixin, dabo.ui.dCheckBox): pass
class SelectLabel(SelectControlMixin, dabo.ui.dLabel):
    def afterInit(self):
    	# Basically, we don't want anything to display, but it's
    	# easier if every selector has a matching control.
    	self.Caption = ""
class SelectDateTextBox(SelectControlMixin, dabo.ui.dDateTextBox): pass
class SelectSpinner(SelectControlMixin, dabo.ui.dSpinner): pass

class SelectionOpDropdown(dabo.ui.dDropdownList):
    def initProperties(self):
    	super(SelectionOpDropdown, self).initProperties()
    	self.SaveRestoreValue = True

    def initEvents(self):
    	super(SelectionOpDropdown, self).initEvents()
    	self.bindEvent(dEvents.Hit, self.onChoiceMade)
    	self.bindEvent(dEvents.ValueChanged, self.onValueChanged)

    def onValueChanged(self, evt):
    	# italicize if we are ignoring the field:
    	self.FontItalic = (IGNORE_STRING in self.Value)
    	if self.Target:
    		self.Target.FontItalic = self.FontItalic

    def onChoiceMade(self, evt):
    	if IGNORE_STRING not in self.StringValue:
    		# A comparison op was selected; let 'em enter a value
    		self.Target.setFocus()

    def _getTarget(self):
    	try:
    		_target = self._target
    	except AttributeError:
    		_target = self._target = None
    	return _target

    def _setTarget(self, tgt):
    	self._target = tgt
    	if self.Target:
    		self.Target.FontItalic = self.FontItalic

    Target = property(_getTarget, _setTarget, None, "Holds a reference to the edit control.")


class SortLabel(dabo.ui.dLabel):
    def initEvents(self):
    	super(SortLabel, self).initEvents()
    	self.bindEvent(dEvents.MouseRightClick, self.Parent.Parent.onSortLabelRClick)
    	# Add a property for the related field
    	self.relatedDataField = ""


class PagSelectBase(datanav.SelectPage):
    pass
