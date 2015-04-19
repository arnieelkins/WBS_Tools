#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dabo
import traceback
import sys

class StudentsBizobj(dabo.biz.dBizobj):
	def afterInit(self):
		self.app = self.Application
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
		self.DefaultValues = {"StudentID":None,
								"StudentTeachersRecNo": 1,
								"StudentContactsRecNo": 1,
								"StudentBirthdate": '0000-00-00',
								"StudentAge": 0,
								"StudentWBSID": 'AL-025',}
		#set bizobj to ignore referential integrity when deleting a child record
		self.deleteChildLogic = 1
	def getContactFullName(self):
		try:
			return self.Record.ContactFirstName + " " + self.Record.ContactLastName
		except:
			dabo.ui.exclaim("Database error!  Please record the error message! " + str(traceback.format_exc()))
			sys.exit(1)
	def getTeacherFullName(self):
		try:
			return self.Record.TeacherFirstName + " " + self.Record.TeacherLastName
		except:
			dabo.ui.exclaim("Database error!  Please record the error message! " + str(traceback.format_exc()))
			sys.exit(1)
	def getStudentFullName(self):
		try:
			return self.Record.StudentFirstName + " " + self.Record.StudentLastName
		except:
			dabo.ui.exclaim("Database error!  Please record the error message! " + str(traceback.format_exc()))
			if self.app.Debug:
				dabo.ui.exclaim("StudentFirstName = " + str(self.Record.StudentFirstName) + " and StudentLastName = " + str(self.Record.StudentLastName))
				dabo.ui.exclaim("record number = " + str(self.Record.StudentRecNo))
			sys.exit(1)
	def validateRecord(self):
		"""Returning anything other than an empty string from
		this method will prevent the data from being saved.
		"""
		app = self.Application
		status = self.getRecordStatus()
		if 'StudentFirstName' in status or 'StudentLastName' in status:
			# either first name or last name was just changed, now check to make sure both exist
			firstName = self.Record.StudentFirstName
			print 'firstName = ' + str(firstName)
			if firstName == '' or firstName == None:
				return
			lastName = str(self.Record.StudentLastName)
			print 'lastName = ' + str(lastName)
			if lastName == '' or lastName == None:
				return
			firstSpace = firstName.find(' ')
			if firstSpace:
				firstName = firstName[0:firstSpace]
			firstName = firstName.lower() + '%'
			lastName = lastName.lower() + '%'
			recNo = str(self.Record.StudentRecNo)
			tempCursor = self.getTempCursor()
			tempCursor.UserSQL = "select StudentRecNo from Students where StudentFirstName like %s and StudentLastName like %s"
			tempCursor.requery((firstName, lastName,))
			dataSet = tempCursor.getDataSet()
			count = 0
			recNos = []
			for row in dataSet:
				count = count + 1
				recNos.append(str(row['StudentRecNo']))
			if count >=2:
				tempCursor.UserSQL = "select * from Students where StudentRecNo in %s"
				tempCursor.requery((recNos,))
				newForm = app.ui.DuplicateStudentForm(app.MainForm, Modal=True)
				newForm.DuplicateRecordsGrid.DataSet = tempCursor.getDataSet()
				newForm.CenterOnParent()
				newForm.show()
				# if user clicks Yes, newForm.Accepted will be true
				if newForm.Accepted:
					#returning an empty string will save the data
					ret = ""
				else:
					ret = recNo
				newForm.safeDestroy()
			else:
				ret = ""
			# Add your business rules here.
			return ret
