#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo

class LessonsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.DataSource = "Lessons"
		self.KeyField = "LessonRecNo"
		self.addFrom("Lessons")
		self.addField("LessonRecNo")
		self.addField("LessonShortName")
		self.addField("LessonName")

	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		# Add your business rules here.
		return ret
	def getAvailableTypes(self):
			"""Return a 2-tuple of lists of the types and their keys."""
			crs = self.getTempCursor()
			crs.execute("select LessonRecNo, LessonShortName from Lessons")
			ds = crs.getDataSet()
			# Create the lists
			names = [rec["LessonShortName"] for rec in ds]
			keys = [rec["LessonRecNo"] for rec in ds]
			return (names, keys)
