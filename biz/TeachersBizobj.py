# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo
class TeachersBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.AutoPopulatePK = True
		self.SaveNewUnchanged = True
		self.DataSource = "Teachers"
		self.KeyField = "TeacherRecNo"
		self.addFrom("Teachers")
		self.addField("TeacherRecNo")
		self.addField("TeacherWBSID")
		self.addField("TeacherFirstName")
		self.addField("TeacherLastName")
		self.addField("TeacherPictureName")
		self.addField("TeacherPictureData")
		self.DefaultValues = {"TeacherWBSID": 'AL-091',}
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		return ret
	def getAvailableTypes(self):
			"""Return a 2-tuple of lists of the types and their keys."""
			crs = self.getTempCursor()
			crs.execute("select TeacherRecNo, concat(TeacherFirstName, ' ', TeacherLastName) as TeacherFullName from Teachers order by TeacherLastName")
			ds = crs.getDataSet()
			# Create the lists
			names = [rec["TeacherFullName"] for rec in ds]
			keys = [rec["TeacherRecNo"] for rec in ds]
			return (names, keys)