# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
### 		'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo
class GradesBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.setLimit(None)
		self.AutoPopulatePK = True
		self.SaveNewUnchanged = True
		self.DataSource = "Grades"
		self.KeyField = "GradeRecNo"
		self.LinkField = "GradeStudentsRecNo"
		self.addFrom("Grades")
		self.addField("GradeRecNo")
		self.addField("GradeLessonsRecNo")
		self.addField("GradeStudentsRecNo")
		self.addField("GradeDateSent")
		self.addField("GradeDateReceived")
		self.addField("GradeDateGraded")
		self.addField("GradeScore")
		self.addField("GradeComments")
		self.addJoin("Lessons", "GradeLessonsRecNo = LessonRecNo")
		self.addField("LessonShortName")
		self.addJoin("Students", "GradeStudentsRecNo = StudentRecNo")
		self.addField("StudentFirstName")
		self.addField("StudentLastName")
		self.ParentLinkField = "StudentRecNo"
		self.VirtualFields = {"StudentFullName":self.getStudentFullName}
	def getStudentFullName(self):
		return self.Record.StudentFirstName + " " + self.Record.StudentLastName
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		return ret
