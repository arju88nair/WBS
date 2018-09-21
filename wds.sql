-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: wds
-- ------------------------------------------------------
-- Server version	5.5.59-log

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
-- Table structure for table `blue_print`
--

DROP TABLE IF EXISTS `blue_print`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blue_print` (
  `id` int(11) NOT NULL,
  `slno` varchar(45) NOT NULL,
  `name` varchar(255) NOT NULL,
  `start_date` varchar(45) DEFAULT NULL,
  `end_date` varchar(45) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blue_print`
--

LOCK TABLES `blue_print` WRITE;
/*!40000 ALTER TABLE `blue_print` DISABLE KEYS */;
INSERT INTO `blue_print` VALUES (1,'1','Home','2018-08-01 ','2019-02-28',0),(2,'1.1','Foundation','2018-08-01 ','2019-09-04',1),(3,'1.1.1','Digging soil','2018-08-01 ','2019-08-10',1),(4,'1.1.2','Piling','2018-08-11 ','2019-09-04',1),(5,'1.2','Floor','2018-09-06','2019-11-04',NULL),(6,'1.2.1','Tiling','2018-09-06','2019-11-04 ',5),(7,'1.3','\nWalls\n','2018-11-06','2019-01-14',NULL),(8,'1.4','Roof','2019-01-15 ','2019-02-28',NULL),(9,'1.5','\nBoundary wall\n','2018-08-01','2018-09-02',NULL);
/*!40000 ALTER TABLE `blue_print` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-21 12:49:50
