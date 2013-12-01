CREATE DATABASE  IF NOT EXISTS `wbs_monrovia` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `wbs_monrovia`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: mysql.monrovia.org    Database: wbs_dabo
-- ------------------------------------------------------
-- Server version	5.1.56-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Answers`
--

DROP TABLE IF EXISTS `Answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Answers` (
  `AnswerRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `AnswerLessonsRecNo` int(11) DEFAULT NULL,
  `AnswerQuestionNo` varchar(5) NOT NULL,
  `AnswerCorrectAnswer` varchar(1) NOT NULL,
  PRIMARY KEY (`AnswerRecNo`),
  KEY `FK_LessonsRecNo_idx` (`AnswerLessonsRecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=571 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Comments`
--

DROP TABLE IF EXISTS `Comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comments` (
  `CommentRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `CommentTag` varchar(45) NOT NULL,
  `CommentContent` text NOT NULL,
  PRIMARY KEY (`CommentRecNo`),
  KEY `Tags` (`CommentTag`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Contacts`
--

DROP TABLE IF EXISTS `Contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Contacts` (
  `ContactRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `ContactWBSID` varchar(10) NOT NULL,
  `ContactFirstName` varchar(32) NOT NULL,
  `ContactLastName` varchar(17) NOT NULL,
  PRIMARY KEY (`ContactRecNo`),
  UNIQUE KEY `Contacts_RecNo_UNIQUE` (`ContactRecNo`),
  KEY `FK_Contacts_WBSRecNo_idx` (`ContactWBSID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Grades`
--

DROP TABLE IF EXISTS `Grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Grades` (
  `GradeRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `GradeDateGraded` date DEFAULT NULL,
  `GradeLessonsRecNo` int(11) DEFAULT NULL,
  `GradeScore` int(11) DEFAULT NULL,
  `GradeStudentsRecNo` int(11) DEFAULT NULL,
  `GradeDateSent` date NOT NULL DEFAULT '0001-01-01',
  `GradeDateReceived` date NOT NULL DEFAULT '0001-01-01',
  `GradeComments` text NOT NULL,
  PRIMARY KEY (`GradeRecNo`),
  UNIQUE KEY `idx_students_lessons` (`GradeLessonsRecNo`,`GradeStudentsRecNo`),
  KEY `fk_lessons_idx` (`GradeLessonsRecNo`),
  KEY `fk_students_idx` (`GradeStudentsRecNo`),
  CONSTRAINT `fk_lessons` FOREIGN KEY (`GradeLessonsRecNo`) REFERENCES `Lessons` (`LessonRecNo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_students` FOREIGN KEY (`GradeStudentsRecNo`) REFERENCES `Students` (`StudentRecNo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2222 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Lessons`
--

DROP TABLE IF EXISTS `Lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Lessons` (
  `LessonRecNo` int(11) NOT NULL,
  `LessonName` varchar(30) NOT NULL,
  `LessonShortName` varchar(6) NOT NULL,
  PRIMARY KEY (`LessonRecNo`),
  UNIQUE KEY `RecNo_UNIQUE` (`LessonRecNo`),
  UNIQUE KEY `Name_UNIQUE` (`LessonName`),
  UNIQUE KEY `ShortName_UNIQUE` (`LessonShortName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Students` (
  `StudentRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `StudentID` varchar(10) DEFAULT NULL,
  `StudentWBSID` varchar(10) DEFAULT 'AL-091',
  `StudentTeachersRecNo` int(11) DEFAULT '1',
  `StudentContactsRecNo` int(11) DEFAULT '1',
  `StudentFirstName` varchar(32) DEFAULT NULL,
  `StudentLastName` varchar(17) DEFAULT NULL,
  `StudentAge` int(11) DEFAULT NULL,
  `StudentBirthdate` date DEFAULT NULL,
  `StudentGender` char(1) NOT NULL DEFAULT '',
  `StudentMaritalStatus` enum('','Single','Married') DEFAULT NULL,
  `StudentReligion` varchar(45) DEFAULT NULL,
  `StudentChurchName` varchar(45) DEFAULT NULL,
  `StudentWBSBefore` enum('','Yes','No') DEFAULT NULL,
  `StudentCountry` varchar(45) DEFAULT NULL,
  `StudentState` varchar(45) DEFAULT NULL,
  `StudentCity` varchar(45) DEFAULT NULL,
  `StudentPostalAddress` varchar(255) DEFAULT NULL,
  `StudentEmailAddress` varchar(45) DEFAULT NULL,
  `StudentPhone1` varchar(45) DEFAULT NULL,
  `StudentPhone2` varchar(45) DEFAULT NULL,
  `StudentStreetAddress` varchar(255) DEFAULT NULL,
  `StudentOccupation` varchar(45) DEFAULT NULL,
  `StudentHasBeenBaptized` enum('','Yes','No') DEFAULT NULL,
  `StudentBaptismType` enum('','Immersed','Sprinkled','Poured','Other') DEFAULT NULL,
  `StudentRequestedBaptism` enum('','Yes','No') DEFAULT NULL,
  `StudentHasBible` enum('','Yes','No') DEFAULT NULL,
  `StudentNotes` longtext,
  PRIMARY KEY (`StudentRecNo`),
  UNIQUE KEY `Students_RecNo_UNIQUE` (`StudentRecNo`),
  UNIQUE KEY `StudentID_UNIQUE` (`StudentID`),
  KEY `FK_Students_TeachersRecNo_idx` (`StudentTeachersRecNo`),
  KEY `FK_Students_ContactsRecNot_idx` (`StudentContactsRecNo`),
  KEY `FK_Students_WBSIDS_idx` (`StudentWBSID`),
  KEY `fk_hasbible_idx` (`StudentHasBible`),
  KEY `fk_baptismtypes_idx` (`StudentBaptismType`),
  KEY `fk_hasbeenbaptized_idx` (`StudentHasBeenBaptized`),
  KEY `fk_maritalstatus_idx` (`StudentMaritalStatus`),
  KEY `fk_requestedbaptism_idx` (`StudentRequestedBaptism`),
  KEY `fk_wbsbefore_idx` (`StudentWBSBefore`),
  CONSTRAINT `fk_contacts` FOREIGN KEY (`StudentContactsRecNo`) REFERENCES `Contacts` (`ContactRecNo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_teachers` FOREIGN KEY (`StudentTeachersRecNo`) REFERENCES `Teachers` (`TeacherRecNo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1981 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Teachers`
--

DROP TABLE IF EXISTS `Teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Teachers` (
  `TeacherRecNo` int(11) NOT NULL AUTO_INCREMENT,
  `TeacherWBSID` varchar(10) NOT NULL,
  `TeacherFirstName` varchar(32) NOT NULL,
  `TeacherLastName` varchar(17) NOT NULL,
  PRIMARY KEY (`TeacherRecNo`),
  UNIQUE KEY `Teachers_RecNo_UNIQUE` (`TeacherRecNo`),
  KEY `FK_Teachers_WBSRecNo_idx` (`TeacherWBSID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-01  2:36:26
