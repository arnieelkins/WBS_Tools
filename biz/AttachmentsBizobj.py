#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo

class AttachmentsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.DataSource = "Attachments"
		self.LinkField = "AttachmentContactsRecNo"
		self.KeyField = "AttachmentRecNo"
		self.addFrom("Attachments")
		self.addField("AttachmentRecNo")
		self.addField("AttachmentContactsRecNo")
		self.addField("AttachmentStudentsRecNo")
		self.addField("AttachmentName")
		self.addField("AttachmentData")
		self.addField("AttachmentType")
		self.addField("AttachmentCreated")
		self.addField("AttachmentSentToContact")
		self.addField("AttachmentSelected")
		self.addJoin("Contacts", "AttachmentContactsRecNo = ContactRecNo")
		self.addField("ContactFirstName")
		self.addField("ContactLastName")
		self.addJoin("Students", "AttachmentStudentsRecNo = StudentRecNo")
		self.addField("StudentFirstName")
		self.addField("StudentLastName")
		self.VirtualFields = {"StudentFullName":self.getStudentFullName,
							"ContactFullName":self.getContactFullName,}
		self.DefaultValues = {"AttachmentType": 'Graded Lesson',
								"AttachmentSentToContact": None,
								"AttachmentSelected": False,
								}
		#set bizobj to ignore referential integrity when deleting a child record
		self.deleteChildLogic = 1

	def initPropterties(self):
		self.DataStructure = (
				("AttachmentRecNo", "I", True, "Attachments", "AttachmentRecNo"),
				("AttachmentContactsRecNo", "I", False, "Attachments", "AttachmentContactsRecNo"),
				("AttachmentStudentsRecNo", "I", False, "Attachments", "AttachmentStudentsRecNo"),
				("AttachmentName", "C", False, "Attachments", "AttachmentName"),
				("AttachmentData", "C", False, "Attachments", "AttachmentData"),
				("AttachmentType", "I", False, "Attachments", "AttachmentType"),
				("AttachmentCreated", "D", False, "Attachments", "AttachmentCreated"),
				("AttachmentSentToContact", "D", False, "Attachments", "AttachmentSentToContact"),
				("AttachmentSelected", "C", False, "Attachments", "AttachmentSelected"),
				("StudentFullName", "C", False, "Attachments", "StudentFullName"),
				("ContactFullName", "C", False, "Attachments", "ContactFullName"),
		)


	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		ret = ""
		# Add your business rules here.
		return ret
	def getStudentFullName(self):
		return self.Record.StudentFirstName + " " + self.Record.StudentLastName
	def getContactFullName(self):
		return self.Record.ContactFirstName + " " + self.Record.ContactLastName