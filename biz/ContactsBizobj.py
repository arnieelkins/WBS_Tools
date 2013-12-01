# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo
class ContactsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.AutoPopulatePK = True
		self.SaveNewUnchanged = True
		self.DataSource = "Contacts"
		self.KeyField = "ContactRecNo"
		self.addFrom("Contacts")
		self.addField("ContactRecNo")
		self.addField("ContactWBSID")
		self.addField("ContactFirstName")
		self.addField("ContactLastName")
		self.VirtualFields = {"ContactFullName":self.getContactFullName}
		self.DefaultValues = {"ContactWBSID": 'AL-091',}
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		return ret
	def getContactFullName(self):
		return self.Record.ContactFirstName + " " + self.Record.ContactLastName
	def getAvailableTypes(self):
			"""Return a 2-tuple of lists of the types and their keys."""
			crs = self.getTempCursor()
			crs.execute("select ContactRecNo, concat(ContactFirstName, ' ', ContactLastName) as ContactFullName from Contacts order by ContactLastName")
			ds = crs.getDataSet()
			# Create the lists
			names = [rec["ContactFullName"] for rec in ds]
			keys = [rec["ContactRecNo"] for rec in ds]
			return (names, keys)