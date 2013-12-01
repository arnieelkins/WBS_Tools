#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo

class CommentsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.DataSource = "Comments"
		self.KeyField = "CommentRecNo"
		self.addFrom("Comments")
		self.addField("CommentContent")
		self.addField("CommentTag")
		self.addField("CommentRecNo")

	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		# Add your business rules here.
		return ret

