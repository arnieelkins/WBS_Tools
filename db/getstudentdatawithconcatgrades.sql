SELECT 
concat(StudentFirstName, " ", StudentLastName) as studentfullname,
concat(TeacherFirstName, " ", TeacherLastName) as teacherfullname,
concat(ContactFirstName, " ", ContactLastName) as contactfullname,
studentage,
studentbaptismtype,
studentbible,
studentbirthdate,
studentchurchname,
studentcontactsrecno,
studentcountry,
studentemailaddress,
studentfirstname,
studentgender,
studenthasbeenbaptized,
studentid,
studentlastname,
studentmaritalstatus,
studentnotes,
studentoccupation,
studentphone1,
studentphone2,
studentpostaladdress,
studentrecno,
studentreligion,
studentrequestedbaptism,
studentstate,
studentstreetaddress,
studentteachersrecno,
studenttown,
studentwbsbefore,
studentwbsid,
gradedata, gradestudentsrecno
FROM teachers,
contacts,
students left join 
(select gradestudentsrecno, group_concat(graderecno, ' ', GradeDateGraded, ' ', LessonShortName, ' ', GradeScore, ' ',
 coalesce(GradeComments, '') separator "\n") as gradedata from (select * from (select * from grades left join lessons
on gradelessonsrecno = lessonrecno) as gradeswithlesson where gradestudentsrecno in 
(select studentrecno from students)) as studentrecs group by gradestudentsrecno) as gradestuff  
 on gradestuff.gradestudentsrecno = studentrecno
where studentteachersrecno = teacherrecno and
studentcontactsrecno = contactrecno
