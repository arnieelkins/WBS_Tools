# -*- coding: utf-8 -*-

import datetime
import decimal
import dabo
import csv
import os

def getIntroGradingFormDataSet(bizObj, recordNumber):
	"""Return the dataset for the sample report.
	Your real code here would run ad-hoc sql queries and build up a
	dataset (list of dicts).
	"""
	#ds = [{'studentfirstname': 'Burton Lazaro', 'studentbible': '0', 'gradelessonsrecno': '1', 'studentage': '33', 'teacherfullname': 'Alyssa Boulton', 'studentchurchname': 'Church of Christ', 'studentwbsid': 'AL-091', 'studentrecno': '862', 'studentmaritalstatus': 'Married', 'studentwbsbefore': '0', 'studentfullname': 'Burton Lazaro Mwansamale', 'contactfullname': 'Willy Yudah', 'gradescore': '100', 'studentcountry': '', 'studentstreetaddress': '', 'studentphone1': '', 'studentphone2': '', 'studentbaptismtype': 'NULL', 'studentreligion': 'Christian', 'studentlastname': 'Mwansamale', 'studentrequestedbaptism': '0', 'gradedategraded': '2011-11-22', 'studentstate': '', 'studentid': '', 'studentpostaladdress': '', 'studentcontactsrecno': '1', 'studentemailaddress': '', 'studentnotes': '', 'studenttown': '', 'studenthasbeenbaptized': '0', 'studentgender': 'M', 'studentbirthdate': '1978-12-11', 'studentoccupation': 'Teacher', 'studentteachersrecno': '1'},  {'studentfirstname': 'Eliah Leonard', 'studentbible': '0', 'gradelessonsrecno': '6', 'studentage': '42', 'teacherfullname': 'Juan Boulton', 'studentchurchname': 'Lutheran', 'studentwbsid': 'AL-091', 'studentrecno': '1226', 'studentmaritalstatus': 'Married', 'studentwbsbefore': '0', 'studentfullname': 'Eliah Leonard Njenje', 'contactfullname': 'Willy Yudah', 'gradescore': '99', 'studentcountry': '', 'studentstreetaddress': 'P.O. Box 557Mbeya CityMbeya, Tanzania', 'studentphone1': '', 'studentphone2': '', 'studentbaptismtype': 'NULL', 'studentreligion': 'Christian', 'studentlastname': 'Njenje', 'studentrequestedbaptism': '0', 'gradedategraded': '2012-09-08', 'studentstate': '', 'studentid': 'W0001', 'studentpostaladdress': 'P.O. Box 557Mbeya CityMbeya, Tanzania', 'studentcontactsrecno': '1', 'studentemailaddress': '', 'studentnotes': '', 'studenttown': '', 'studenthasbeenbaptized': '0', 'studentgender': 'M', 'studentbirthdate': '1969-07-17', 'studentoccupation': '', 'studentteachersrecno': '2'}]
	#return ds
	'''
	inputFileName = 'db/IntroGradingFormData.csv'
	print os.getcwd()
	print os.path.isfile(inputFileName)
	newDataSet = []
	if os.path.isfile(inputFileName):
		file_to_read = open(inputFileName, "rb")
		reader = csv.DictReader(file_to_read)
		count = 0
		for line in reader:
			count = count + 1
			print "count = " + str(count)
			newDataSet.append(line)
		file_to_read.close()
		print "final dataSet begin"
		print newDataSet
		print "final dataSet end"
		return(newDataSet)
		'''
	tempCursor = bizObj.getTempCursor()
	sqlString = "SELECT concat(StudentFirstName, ' ', StudentLastName) as StudentFullName, concat(TeacherFirstName, ' ', TeacherLastName) as TeacherFullName, concat(ContactFirstName, ' ', ContactLastName) as ContactFullName, StudentAge, StudentBaptismType, StudentHasBible, StudentBirthDate, StudentChurchName, StudentContactsRecNo, StudentCountry, StudentEmailAddress, StudentFirstName, StudentGender, StudentHasBeenBaptized, StudentID, StudentLastName, StudentMaritalStatus, StudentNotes, StudentOccupation, StudentPhone1, StudentPhone2, StudentPostalAddress, StudentRecNo, StudentReligion, StudentRequestedBaptism, StudentState, StudentStreetAddress, StudentTeachersRecNo, StudentTown, StudentWBSBefore, StudentWBSID, GradeData, GradeStudentsRecNo FROM Teachers, Contacts, Students left join (select GradeStudentsRecNo, group_concat(GradeDateGraded, '\t', LessonShortName, '\t', GradeScore, '\t', coalesce(GradeComments, '') separator '\n') as GradeData from (select * from (select * from Grades left join Lessons on GradeLessonsRecNo = LessonRecNo) as GradesWithLesson where GradeStudentsRecNo in (select StudentRecNo from Students)) as StudentRecs group by GradeStudentsRecNo) as Gradestuff on Gradestuff.GradeStudentsRecNo = StudentRecNo where StudentteachersRecNo = TeacherRecNo and StudentContactsRecNo = ContactRecNo and StudentRecNo in"
	tempString = "(" + str(recordNumber) + ")"
	sqlString = sqlString + tempString
	print sqlString
	tempCursor.UserSQL = sqlString
	tempCursor.requery()
	return tempCursor.getDataSet()

