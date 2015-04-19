#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo

class StudentsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.AutoPopulatePK = True
		self.SaveNewUnchanged = True
		self.DataSource = "Students"
		self.KeyField = "StudentRecNo"
		self.addFrom("Students")
		self.addField("StudentRecNo")
		self.addField("StudentContactsRecNo")
		self.addField("StudentTeachersRecNo")
		self.addField("StudentWBSID")
		self.addField("StudentFirstName")
		self.addField("StudentLastName")
		self.addField("StudentHasBeenBaptized")
		self.addField("StudentReligion")
		self.addField("StudentState")
		self.addField("StudentEmailAddress")
		self.addField("StudentRequestedBaptism")
		self.addField("StudentMaritalStatus")
		self.addField("StudentGender")
		self.addField("StudentID")
		self.addField("StudentNotes")
		self.addField("StudentChurchName")
		self.addField("StudentPhone1")
		self.addField("StudentPhone2")
		self.addField("StudentCity")
		self.addField("StudentCountry")
		self.addField("StudentAge")
		self.addField("StudentBirthdate")
		self.addField("StudentBaptismType")
		self.addField("StudentWBSBefore")
		self.addField("StudentHasBible")
		self.addField("StudentPostalAddress")
		self.addField("StudentStreetAddress")
		self.addField("StudentOccupation")
		self.addJoin("Contacts", "StudentContactsRecNo = ContactRecNo")
		self.addField("ContactFirstName")
		self.addField("ContactLastName")
		self.addJoin("Teachers", "StudentTeachersRecNo = TeacherRecNo")
		self.addField("TeacherFirstName")
		self.addField("TeacherLastName")
		self.VirtualFields = {"ContactFullName":self.getContactFullName,
								"TeacherFullName":self.getTeacherFullName,
								"StudentFullName":self.getStudentFullName,
								}
		self.DefaultValues = {"StudentID": None,
								"StudentTeachersRecNo": 1,
								"StudentContactsRecNo": 1,
								"StudentBirthdate": '0000-00-00',
								"StudentAge": 0,
								"StudentWBSID": 'AL-091',}
		#set bizobj to ignore referential integrity when deleting a child record
		self.deleteChildLogic = 1
	def getContactFullName(self):
		return self.Record.ContactFirstName + " " + self.Record.ContactLastName
	def getTeacherFullName(self):
		return self.Record.TeacherFirstName + " " + self.Record.TeacherLastName
	def getStudentFullName(self):
		return self.Record.StudentFirstName + " " + self.Record.StudentLastName
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		status = self.getRecordStatus()
		if 'StudentFirstName' in status or 'StudentLastName' in status:
			firstName = self.Record.StudentFirstName
			if firstName <> '' and firstName <> None:
				firstSpace = firstName.find(' ')
				if firstSpace:
					firstName = firstName[0:firstSpace]
				firstName = firstName + '%'
				lastName = self.Record.StudentLastName + '%'
				if lastName <> '' and lastName <> '':
					recNo = self.Record.StudentRecNo
					tempCursor = self.getTempCursor()
					tempCursor.UserSQL = "select StudentRecNo from Students where StudentFirstName like %s and StudentLastName like %s"
					tempCursor.requery((firstName, lastName,))
					dataSet = tempCursor.getDataSet()
					count = 0
					recNos = []
					for row in dataSet:
						count = count + 1
						recNos.append(row['StudentRecNo'])
					if count >=2:
						tempCursor.UserSQL = "select StudentRecNo, StudentFirstName, StudentLastName from Students where StudentRecNo in %s"
						tempCursor.requery((recNos,))
						recordString = ''
						for record in tempCursor.getDataSet():
							recordString = recordString + ' ' + str(record['StudentRecNo']) + ' ' \
										+ str(record['StudentFirstName']) + ' ' \
										+ str(record['StudentLastName']) + '\n'
						result = dabo.ui.areYouSure("Possible duplicate student record(s) detected!\n\n" + recordString + '\nSave anyway?',
																				title='Potential Duplicate!', 
																				cancelButton = False)
						if result == True:
								ret = ""
						else:
								ret = recordString
					else:
						ret = ""
					# Add your business rules here.
		return ret
