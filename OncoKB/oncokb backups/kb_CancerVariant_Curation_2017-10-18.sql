# ************************************************************
# Sequel Pro SQL dump
# Version 5224
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: db2.hpc.mssm.edu (MySQL 5.6.14-56-log)
# Database: kb_CancerVariant_Curation
# Generation Time: 2017-10-18 19:45:09 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table OncoKB_variants
# ------------------------------------------------------------

DROP TABLE IF EXISTS `OncoKB_variants`;

CREATE TABLE `OncoKB_variants` (
  `Entrez_Gene_ID` int(11) NOT NULL,
  `Hugo_Symbol` varchar(8) NOT NULL DEFAULT '',
  `Gene_Name` varchar(80) NOT NULL DEFAULT '',
  `Oncogene` char(5) NOT NULL DEFAULT '',
  `Curated_Isoform` varchar(30) NOT NULL DEFAULT '',
  `Curated_Refseq` varchar(30) NOT NULL DEFAULT '',
  `TSG` char(5) NOT NULL DEFAULT '',
  `Consequence_term` varchar(30) NOT NULL DEFAULT '',
  `Genes_Aliases0` varchar(15) DEFAULT '',
  `Genes_Aliases1` varchar(15) DEFAULT '',
  `Genes_Aliases2` varchar(15) DEFAULT '',
  `Genes_Aliases3` varchar(15) DEFAULT '',
  `Genes_Aliases4` varchar(15) DEFAULT '',
  `Genes_Aliases5` varchar(15) DEFAULT '',
  `Genes_Aliases6` varchar(15) DEFAULT '',
  `Genes_Aliases7` varchar(15) DEFAULT '',
  `Genes_Aliases8` varchar(15) DEFAULT '',
  `Genes_Aliases9` varchar(15) DEFAULT '',
  `Genes_Aliases10` varchar(15) DEFAULT '',
  `Genes_Aliases11` varchar(15) DEFAULT '',
  `Genes_Aliases12` varchar(15) DEFAULT '',
  `Genes_Aliases13` varchar(15) DEFAULT '',
  `Genes_Aliases14` varchar(15) DEFAULT '',
  `Genes_Aliases15` varchar(15) DEFAULT '',
  `Genes_Aliases16` varchar(15) DEFAULT '',
  `Genes_Aliases17` varchar(15) DEFAULT '',
  `Genes_Aliases18` varchar(15) DEFAULT '',
  `Genes_Aliases19` varchar(15) DEFAULT '',
  `Genes_Aliases20` varchar(15) DEFAULT '',
  `Genes_Aliases21` varchar(15) DEFAULT '',
  `Consequence_isGenerallyTruncated` varchar(5) NOT NULL DEFAULT '',
  `Alteration` varchar(30) NOT NULL DEFAULT '',
  `Alteration_name` varchar(30) NOT NULL DEFAULT '',
  `ref_Residues` char(2) DEFAULT '',
  `Protein_Start` int(10) DEFAULT NULL,
  `Protein_End` int(10) DEFAULT NULL,
  PRIMARY KEY (`Entrez_Gene_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
