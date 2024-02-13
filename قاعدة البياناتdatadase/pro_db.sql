-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 01 مارس 2023 الساعة 22:37
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pro_db`
--

-- --------------------------------------------------------

--
-- بنية الجدول `clients`
--

CREATE TABLE IF NOT EXISTS `clients` (
  `cli_address` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cli_phone` int(20) NOT NULL,
  `cli_name` varchar(100) CHARACTER SET utf32 COLLATE utf32_unicode_ci NOT NULL,
  `cli_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`cli_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- إرجاع أو استيراد بيانات الجدول `clients`
--

INSERT INTO `clients` (`cli_address`, `cli_phone`, `cli_name`, `cli_id`) VALUES
('صنعاء', 777666555, 'محمد محمد', 1),
('صنعاء', 775544332, 'علي سعيد', 2),
('صنعاء', 776655443, 'عبدالله علي', 3);

-- --------------------------------------------------------

--
-- بنية الجدول `commodities`
--

CREATE TABLE IF NOT EXISTS `commodities` (
  `com_categorie` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `com_cost` int(20) NOT NULL,
  `com_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `com_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`com_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- إرجاع أو استيراد بيانات الجدول `commodities`
--

INSERT INTO `commodities` (`com_categorie`, `com_cost`, `com_name`, `com_id`) VALUES
('بطانيات', 15000, 'بطانية', 1),
('قطن', 1500, 'مخده', 2);

-- --------------------------------------------------------

--
-- بنية الجدول `employees`
--

CREATE TABLE IF NOT EXISTS `employees` (
  `emp_salary` int(20) NOT NULL,
  `emp_address` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `emp_phone` int(20) NOT NULL,
  `emp_job` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `emp_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `emp_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=7 ;

--
-- إرجاع أو استيراد بيانات الجدول `employees`
--

INSERT INTO `employees` (`emp_salary`, `emp_address`, `emp_phone`, `emp_job`, `emp_name`, `emp_id`) VALUES
(300, 'صنعاء', 777666888, 'مخيط', 'محمد علي', 1),
(300, 'صنعاء', 770099887, 'مخيط', 'علي عبده', 2),
(1000, 'صنعاء', 739863658, 'مدير', 'حسام أحمد سالم', 3),
(1000, 'إب', 776655443, 'مدير', 'عزيز محمد', 4);

-- --------------------------------------------------------

--
-- بنية الجدول `purchase`
--

CREATE TABLE IF NOT EXISTS `purchase` (
  `pur_type` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pur_date_purchase` date NOT NULL,
  `pur_purchase_amount` int(20) NOT NULL,
  `pur_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pur_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pur_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=4 ;

--
-- إرجاع أو استيراد بيانات الجدول `purchase`
--

INSERT INTO `purchase` (`pur_type`, `pur_date_purchase`, `pur_purchase_amount`, `pur_name`, `pur_id`) VALUES
('كاش', '2023-02-25', 300000, 'بطانيات', 1),
('أجل', '2023-02-26', 150000, 'إسفنج', 2);

-- --------------------------------------------------------

--
-- بنية الجدول `sale`
--

CREATE TABLE IF NOT EXISTS `sale` (
  `sale_type` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sale_date_purchase` date NOT NULL,
  `sale_purchase_amount` int(20) NOT NULL,
  `sale_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sale_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sale_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

--
-- إرجاع أو استيراد بيانات الجدول `sale`
--

INSERT INTO `sale` (`sale_type`, `sale_date_purchase`, `sale_purchase_amount`, `sale_name`, `sale_id`) VALUES
('كاش', '2023-02-23', 600000, 'موكت مجلس', 1),
('كاش', '2023-02-23', 100000, 'مفرشه', 2),
('كاش', '2023-02-24', 20000, 'بطانية', 3),
('كاش', '2023-02-26', 10000, 'ستارة', 4);

-- --------------------------------------------------------

--
-- بنية الجدول `suppliers`
--

CREATE TABLE IF NOT EXISTS `suppliers` (
  `sup_address` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sup_phone` int(20) NOT NULL,
  `sup_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sup_id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sup_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- إرجاع أو استيراد بيانات الجدول `suppliers`
--

INSERT INTO `suppliers` (`sup_address`, `sup_phone`, `sup_name`, `sup_id`) VALUES
('صنعاء', 733344554, 'محمد مصلح', 1),
('صنعاء', 777788654, 'عبدالله مسعد', 2);

-- --------------------------------------------------------

--
-- بنية الجدول `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- إرجاع أو استيراد بيانات الجدول `users`
--

INSERT INTO `users` (`user_id`, `user_name`, `password`) VALUES
(1, 'safwan', 'safwan123'),
(2, 'mansor', '123');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
