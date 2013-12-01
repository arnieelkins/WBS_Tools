# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo
class WbsIdsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.DataSource = "WBSIDS"
		self.KeyField = "RecNo"
		self.addFrom("WBSIDS")
		self.addField("RecNo")
		self.addField("WBSID")
		self.addField("CongregationName")
		self.RegID = "WbsIdsBizobj"
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		return ret
