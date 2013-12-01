#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo

class AnswersBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.DataSource = "Answers"
		self.LinkField = "AnswerLessonsRecNo"
		self.KeyField = "AnswerRecNo"
		self.addFrom("Answers")
		self.addField("AnswerRecNo")
		self.addField("AnswerLessonsRecNo")
		self.addField("AnswerQuestionNo")
		self.addField("AnswerCorrectAnswer")
		self.addJoin("Lessons", "AnswerLessonsRecNo = LessonRecNo")
		self.addField("LessonName")
		self.addField("LessonShortName")
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		# Add your business rules here.
		return ret
