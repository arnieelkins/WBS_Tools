# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
	dabo.ui.loadUI("wx")
import dabo.dEvents as dEvents
from dabo.dLocalize import _, n_
from PagSelectBase import PagSelectBase, IGNORE_STRING, SelectTextBox, \
		SelectCheckBox, SelectLabel, SelectDateTextBox, SelectSpinner, \
		SelectionOpDropdown, SortLabel


class PagSelectStudents(PagSelectBase):

	
	def getSelectOptionsPanel(self):
		"""Return the panel to contain all the select options."""

		biz = self.Form.getBizobj()
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
		
		panel = dabo.ui.dPanel(self)
		gsz = dabo.ui.dGridSizer(VGap=5, HGap=10)
		gsz.MaxCols = 3
		label = dabo.ui.dLabel(panel)
		label.Caption = _("Please enter your record selection criteria:")
		label.FontSize = label.FontSize + 2
		label.FontBold = True
		gsz.append(label, colSpan=3, alignment="center")

		##
		## Field Students.RecNo
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("RecNo")
		lbl.relatedDataField = "RecNo"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("int", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("int")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["RecNo"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "int"
					}
		else:
			dabo.log.error("No control class found for field 'RecNo'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.StudentID
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("StudentID")
		lbl.relatedDataField = "StudentID"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["StudentID"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'StudentID'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.WBSIDSRecNo
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("WBSIDSRecNo")
		lbl.relatedDataField = "WBSIDSRecNo"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("int", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("int")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["WBSIDSRecNo"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "int"
					}
		else:
			dabo.log.error("No control class found for field 'WBSIDSRecNo'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.TeachersRecNo
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("TeachersRecNo")
		lbl.relatedDataField = "TeachersRecNo"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("int", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("int")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["TeachersRecNo"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "int"
					}
		else:
			dabo.log.error("No control class found for field 'TeachersRecNo'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.ContactsRecNo
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("ContactsRecNo")
		lbl.relatedDataField = "ContactsRecNo"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("int", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("int")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["ContactsRecNo"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "int"
					}
		else:
			dabo.log.error("No control class found for field 'ContactsRecNo'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.FirstName
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("FirstName")
		lbl.relatedDataField = "FirstName"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["FirstName"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'FirstName'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.LastName
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("LastName")
		lbl.relatedDataField = "LastName"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["LastName"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'LastName'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Age
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Age")
		lbl.relatedDataField = "Age"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("int", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("int")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Age"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "int"
					}
		else:
			dabo.log.error("No control class found for field 'Age'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Birthdate
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Birthdate")
		lbl.relatedDataField = "Birthdate"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("date", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("date")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Birthdate"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "date"
					}
		else:
			dabo.log.error("No control class found for field 'Birthdate'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Gender
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Gender")
		lbl.relatedDataField = "Gender"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Gender"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Gender'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.MaritalStatus
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("MaritalStatus")
		lbl.relatedDataField = "MaritalStatus"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["MaritalStatus"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'MaritalStatus'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Religion
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Religion")
		lbl.relatedDataField = "Religion"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Religion"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Religion'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.ChurchName
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("ChurchName")
		lbl.relatedDataField = "ChurchName"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["ChurchName"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'ChurchName'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.WBSBefore
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("WBSBefore")
		lbl.relatedDataField = "WBSBefore"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("bool", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("bool")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["WBSBefore"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "bool"
					}
		else:
			dabo.log.error("No control class found for field 'WBSBefore'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Country
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Country")
		lbl.relatedDataField = "Country"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Country"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Country'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.State
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("State")
		lbl.relatedDataField = "State"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["State"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'State'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.City
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("City")
		lbl.relatedDataField = "City"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["City"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'City'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.PostalAddress
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("PostalAddress")
		lbl.relatedDataField = "PostalAddress"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["PostalAddress"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'PostalAddress'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.EmailAddress
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("EmailAddress")
		lbl.relatedDataField = "EmailAddress"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["EmailAddress"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'EmailAddress'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Phone1
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Phone1")
		lbl.relatedDataField = "Phone1"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Phone1"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Phone1'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Phone2
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Phone2")
		lbl.relatedDataField = "Phone2"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Phone2"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Phone2'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.StreetAddress
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("StreetAddress")
		lbl.relatedDataField = "StreetAddress"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["StreetAddress"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'StreetAddress'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Occupation
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Occupation")
		lbl.relatedDataField = "Occupation"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Occupation"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'Occupation'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.HasBeenBaptized
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("HasBeenBaptized")
		lbl.relatedDataField = "HasBeenBaptized"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("bool", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("bool")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["HasBeenBaptized"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "bool"
					}
		else:
			dabo.log.error("No control class found for field 'HasBeenBaptized'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.TypeOfBaptism
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("TypeOfBaptism")
		lbl.relatedDataField = "TypeOfBaptism"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("char", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("char")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["TypeOfBaptism"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "char"
					}
		else:
			dabo.log.error("No control class found for field 'TypeOfBaptism'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.RequestedBaptism
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("RequestedBaptism")
		lbl.relatedDataField = "RequestedBaptism"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("bool", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("bool")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["RequestedBaptism"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "bool"
					}
		else:
			dabo.log.error("No control class found for field 'RequestedBaptism'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Bible
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Bible")
		lbl.relatedDataField = "Bible"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("bool", wordSearch=False)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("bool")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Bible"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "bool"
					}
		else:
			dabo.log.error("No control class found for field 'Bible'.")
			lbl.safeDestroy()
			opList.safeDestroy()


		##
		## Field Students.Notes
		##
		lbl = SortLabel(panel)
		lbl.Caption = biz.getColCaption("Notes")
		lbl.relatedDataField = "Notes"

		# Automatically get the selector options based on the field type:
		opt = self.getSelectorOptions("memo", wordSearch=True)

		# Add the blank choice and create the dropdown:
		opt = (IGNORE_STRING,) + tuple(opt)
		opList = SelectionOpDropdown(panel, Choices=opt)

		# Automatically get the control class based on the field type:
		ctrlClass = self.getSearchCtrlClass("memo")

		if ctrlClass is not None:
			ctrl = ctrlClass(panel)
			if not opList.StringValue:
				opList.PositionValue = 0
			opList.Target = ctrl

			gsz.append(lbl, halign="right")
			gsz.append(opList, halign="left")
			gsz.append(ctrl, "expand")

			# Store the info for later use when constructing the query
			self.selectFields["Notes"] = {
					"ctrl" : ctrl,
					"op" : opList,
					"type": "memo"
					}
		else:
			dabo.log.error("No control class found for field 'Notes'.")
			lbl.safeDestroy()
			opList.safeDestroy()

		# Now add the limit field
		lbl = dabo.ui.dLabel(panel)
		lbl.Caption =  _("&Limit:")
		limTxt = SelectTextBox(panel)
		if len(limTxt.Value) == 0:
			limTxt.Value = "1000"
		self.selectFields["limit"] = {"ctrl" : limTxt}
		gsz.append(lbl, alignment="right")
		gsz.append(limTxt)

		# Custom SQL checkbox:
		chkCustomSQL = dabo.ui.dCheckBox(panel, Caption=_("Use Custom SQL"))
		chkCustomSQL.bindEvent(dEvents.Hit, self.onCustomSQL)
		gsz.append(chkCustomSQL)

		# Requery button:
		requeryButton = dabo.ui.dButton(panel)
		requeryButton.Caption =  _("&Requery")
		requeryButton.DefaultButton = True
		requeryButton.bindEvent(dEvents.Hit, self.onRequery)
		btnRow = gsz.findFirstEmptyCell()[0] + 1
		gsz.append(requeryButton, "expand", row=btnRow, col=1,
				halign="right", border=3)

		# Make the last column growable
		gsz.setColExpand(True, 2)
		panel.Sizer = gsz

		vsz = dabo.ui.dSizer("v")
		vsz.append(gsz, 1, "expand")
		return panel





if __name__ == "__main__":
	from FrmStudents import FrmStudents
	app = dApp(MainFormClass=None)
	app.setup()
	class TestForm(FrmStudents):
		def afterInit(self): pass
	frm = TestForm(Caption="Test Of PagSelectStudents", Testing=True)
	test = PagSelectStudents(frm)
	test.createItems()
	frm.Sizer.append1x(test)
	frm.show()
	app.start()
