-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2022 at 01:13 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newfinsys`
--

-- --------------------------------------------------------

--
-- Table structure for table `app1_accounts`
--

CREATE TABLE `app1_accounts` (
  `accountsid` int(11) NOT NULL,
  `acctype` varchar(100) NOT NULL,
  `detype` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `gst` varchar(100) DEFAULT NULL,
  `deftaxcode` varchar(100) NOT NULL,
  `balance` double DEFAULT NULL,
  `asof` date NOT NULL,
  `balfordisp` double DEFAULT NULL,
  `cid_id` int(11) NOT NULL,
  `productid_id` int(11) NOT NULL,
  `proid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_accounts`
--

INSERT INTO `app1_accounts` (`accountsid`, `acctype`, `detype`, `name`, `description`, `gst`, `deftaxcode`, `balance`, `asof`, `balfordisp`, `cid_id`, `productid_id`, `proid_id`) VALUES
(1, '2', 'Inventory', 'Inventory', 'fgdd', 'dfgfd', 'fdgf', 22594, '2022-09-14', 0, 6, 2, 2),
(2, '2', 'Inventory', 'Inventory', 'dfsssdf', 'dsfds', 'sdfdsf', 22594, '2022-09-14', 0, 6, 2, 2),
(3, '2', 'Inventory', 'Inventory', 'ghjgj', 'hgjh', 'hgjhgj', 22594, '2022-09-14', 0, 6, 2, 2),
(4, '2', 'Inventory', 'Inventory', 'hgfhg', 'bvfhg', 'hgfhgf', 22594, '2022-09-14', 0, 6, 2, 2),
(5, '2', 'Inventory', 'Inventory', 'ghffhljkjlkljkjklljkljk', 'kjljkl', 'jkljklkkkkkkkkkkkkkkkkkkkkkkkkkk', 22594, '2022-09-16', 0, 6, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `app1_accounts1`
--

CREATE TABLE `app1_accounts1` (
  `accounts1id` int(11) NOT NULL,
  `acctype` varchar(100) NOT NULL,
  `detype` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `gst` varchar(100) DEFAULT NULL,
  `deftaxcode` varchar(100) NOT NULL,
  `balance` double DEFAULT NULL,
  `asof` date DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_accounts1`
--

INSERT INTO `app1_accounts1` (`accounts1id`, `acctype`, `detype`, `name`, `description`, `gst`, `deftaxcode`, `balance`, `asof`, `cid_id`) VALUES
(5, 'income', 'fdgf', 'Billable Expense Income', '', NULL, '', 150, '2022-02-11', 6),
(9, 'Income', 'sas', 'Billable Expense Income', '', NULL, '', 150, '2022-08-22', 6),
(10, 'Income', 'sdfds', 'Account Receivable(Debtors)', '', NULL, '', -14310, '2022-08-21', 6),
(11, 'Expenses', 'zzvxcvv', 'ZzxzZx', '', NULL, '', 150, '2022-08-20', 6),
(12, 'Expenses', 'gfh', 'sdfd', '', NULL, '', 150, '2022-08-22', 6),
(13, 'Income', 'fdgfg', 'cxvc', '', NULL, '', 150, '2022-08-22', 6),
(17, 'Income', 'sads', 'Billable Expense Income', '', NULL, '', 150, '2022-03-15', 6),
(19, 'Income', 'dsfds', 'Billable Expense Income', '', NULL, '', 150, '2022-04-03', 6),
(20, 'Income', 'dsff', 'Billable Expense Income', '', NULL, '', 150, '2022-05-06', 6),
(21, 'Income', 'sad', 'Billable Expense Income', '', NULL, '', 150, '2022-06-03', 6),
(22, 'Income', 'sda', 'Billable Expense Income', '', NULL, '', 150, '2022-07-02', 6),
(23, 'Income', 'dsd', 'Billable Expense Income', '', NULL, '', 150, '2022-08-03', 6),
(24, 'Income', 'sdsfd', 'Consulting Income', '', NULL, '', 150, '2022-08-13', 6),
(25, 'Income', 'ds', 'Consulting Income', '', NULL, '', 150, '2022-07-12', 6),
(26, 'Income', 'dsfd', 'Consulting Income', '', NULL, '', 150, '2022-06-15', 6),
(27, 'Income', 'sdf', 'Consulting Income', '', NULL, '', 150, '2022-05-25', 6),
(28, 'Income', 'dsf', 'Consulting Income', '', NULL, '', 150, '2022-05-08', 6),
(30, 'Income', 'dsfd', 'Consulting Income', '', NULL, '', 150, '2022-04-02', 6),
(31, 'Income', 'fdgf', 'Consulting Income', '', NULL, '', 150, '2022-03-05', 6),
(32, 'Income', 'fdh', 'Product Sales', '', NULL, '', 150, '2022-08-09', 6),
(33, 'Income', 'sd', 'Product Sales', '', NULL, '', 150, '2022-07-05', 6),
(34, 'Income', 'dfgf', 'Product Sales', '', NULL, '', 150, '2022-06-22', 6),
(35, 'Income', 'sdfd', 'Product Sales', '', NULL, '', 150, '2022-05-25', 6),
(36, 'Income', 'sdf', 'Product Sales', '', NULL, '', 150, '2022-04-05', 6),
(37, 'Income', 'sdf', 'Product Sales', '', NULL, '', 150, '2022-03-04', 6),
(38, 'Income', 'sfddfd', 'Sales', '', NULL, '', 150, '2022-08-04', 6),
(39, 'Income', 'sfd', 'Sales', '', NULL, '', 150, '2022-07-07', 6),
(40, 'Income', 'sdfd', 'Sales', '', NULL, '', 150, '2022-06-04', 6),
(41, 'Income', 'dsfd', 'Sales', '', NULL, '', 150, '2022-05-04', 6),
(42, 'Income', 'sads', 'Sales', '', NULL, '', 150, '2022-03-04', 6),
(43, 'Income', 'sad', 'Sales', '', NULL, '', 150, '2022-04-08', 6),
(44, 'Income', 'sdf', 'Sales-Hardware', '', NULL, '', 150, '2022-08-04', 6),
(45, 'Income', 'sdfd', 'Sales-Hardware', '', NULL, '', 150, '2022-07-04', 6),
(46, 'Income', 'sdfsda', 'Sales-Hardware', '', NULL, '', 150, '2022-06-22', 6),
(53, 'Income', 'sdfdsf', 'Sales-Hardware', '', NULL, '', 150, '2022-05-04', 6),
(54, 'Income', 'dsfd', 'Sales-Hardware', '', NULL, '', 150, '2022-04-08', 6),
(55, 'Income', 'sdfd', 'Sales-Hardware', '', NULL, '', 150, '2022-03-01', 6),
(56, 'Income', 'dsdf', 'Sales-Software', '', NULL, '', 150, '2022-08-11', 6),
(57, 'Income', 'fdgfd', 'Sales-Software', 'dfsdf', NULL, '', 150, '2022-07-04', 6),
(58, 'Income', 'ewewr', 'Sales-Software', '', NULL, '', 150, '2022-06-12', 6),
(59, 'Income', 'sdf', 'Sales-Software', '', NULL, '', 150, '2022-05-22', 6),
(60, 'Income', 'fghg', 'Sales-Software', '', NULL, '', 150, '2022-04-14', 6),
(61, 'Income', 'xcvc', 'Sales-Software', '', NULL, '', 150, '2022-03-20', 6),
(62, 'Income', 'sdfsd', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-08-14', 6),
(63, 'Income', 'sasad', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-07-15', 6),
(64, 'Income', 'dsf', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-06-21', 6),
(65, 'Income', 'sad', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-05-05', 6),
(66, 'Income', 'sdfd', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-04-14', 6),
(67, 'Income', 'sad', 'Sales-Support and Maintanance', '', NULL, '', 150, '2022-03-20', 6),
(68, 'Income', 'sdf', 'Sales Discounts', '', NULL, '', 150, '2022-08-03', 6),
(69, 'Income', 'fdg', 'Sales Discounts', '', NULL, '', 150, '2022-07-04', 6),
(70, 'Income', 'sadsa', 'Sales Discounts', '', NULL, '', 150, '2022-06-22', 6),
(71, 'Income', 'sdf', 'Sales Discounts', '', NULL, '', 150, '2022-05-22', 6),
(72, 'income', 'sdf', 'Sales Discounts', '', NULL, '', 150, '2022-04-14', 6),
(73, 'Income', 'sdf', 'Sales Discounts', '', NULL, '', 150, '2022-03-20', 6),
(74, 'Income', 'sdfdfs', 'Sales of Product Income', '', NULL, '', 150, '2022-08-03', 6),
(75, 'Income', 'jhgf', 'Sales of Product Income', '', NULL, '', 150, '2022-07-04', 6),
(76, 'Income', 'sad', 'Sales of Product Income', '', NULL, '', 150, '2022-06-22', 6),
(77, 'Income', 'gfd', 'Sales of Product Income', '', NULL, '', 150, '2022-05-22', 6),
(78, 'Income', 'sads', 'Sales of Product Income', '', NULL, '', 150, '2022-04-14', 6),
(79, 'Income', 'gfd', 'Sales of Product Income', '', NULL, '', 150, '2022-03-20', 6),
(80, 'Income', 'sasad', 'Services', '', NULL, '', 150, '2022-08-03', 6),
(81, 'Income', 'jk', 'Services', '', NULL, '', 150, '2022-07-04', 6),
(82, 'Income', 'sddf', 'Services', '', NULL, '', 150, '2022-06-22', 6),
(83, 'Income', 'jhg', 'Services', '', NULL, '', 150, '2022-05-22', 6),
(84, 'Income', 'dsfd', 'Services', '', NULL, '', 150, '2022-04-14', 6),
(85, 'Income', 'sdf', 'Services', '', NULL, '', 150, '2022-03-20', 6),
(86, 'Income', 'sd', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-08-03', 6),
(87, 'Income', 'sa', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-07-04', 6),
(88, 'Income', 'sdf', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-06-22', 6),
(89, 'Income', 'sdf', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-05-22', 6),
(90, 'Income', 'sdf', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-04-14', 6),
(91, 'Income', 'sdfds', 'Unapplied Cash Payment Income', '', NULL, '', 150, '2022-03-20', 6),
(92, 'Income', 'sdf', 'Uncategorised Income', '', NULL, '', 150, '2022-08-03', 6),
(93, 'Income', 'sad', 'Uncategorised Income', '', NULL, '', 150, '2022-07-04', 6),
(94, 'Income', 'sdfsd', 'Uncategorised Income', '', NULL, '', 150, '2022-06-22', 6),
(95, 'Income', 'cxv', 'Uncategorised Income', '', NULL, '', 150, '2022-05-22', 6),
(96, 'Income', 'asdsa', 'Uncategorised Income', '', NULL, '', 150, '2022-04-14', 6),
(97, 'Income', 'sad', 'Uncategorised Income', '', NULL, '', 150, '2022-03-20', 6),
(98, 'Other Income', 'sdf', 'Finance Charge Income', '', NULL, '', 150, '2022-08-03', 6),
(99, 'Other Income', 'df', 'Finance Charge Income', '', NULL, '', 150, '2022-07-04', 6),
(100, 'Other Income', 'df', 'Finance Charge Income', '', NULL, '', 150, '2022-06-22', 6),
(101, 'Other Income', 'ghf', 'Finance Charge Income', '', NULL, '', 150, '2022-05-22', 6),
(102, 'Other Income', 'sdf', 'Finance Charge Income', '', NULL, '', 150, '2022-04-14', 6),
(104, 'Expenses', 'fgddgf', 'Advertising/Promotional', '', NULL, '', 150, '2022-08-03', 6),
(105, 'Expenses', '', 'Advertising/Promotional', '', NULL, '', 150, '2022-07-04', 6),
(106, 'Expenses', '', 'Advertising/Promotional', '', NULL, '', 150, '2022-06-22', 6),
(107, 'Expenses', '', 'Advertising/Promotional', '', NULL, '', 150, '2022-05-22', 6),
(108, 'Expenses', '', 'Advertising/Promotional', '', NULL, '', 150, '2022-04-14', 6),
(110, 'Other Expenses', 'gfhgh', 'Ask My Accountant', '', NULL, '', 150, '2022-08-03', 6),
(111, 'Other Expenses', 'fd', 'Ask My Accountant', '', NULL, '', 150, '2022-07-04', 6),
(112, 'Other Expenses', '', 'Ask My Accountant', '', NULL, '', 150, '2022-06-22', 6),
(113, 'Other Expenses', 'jkk', 'Ask My Accountant', '', NULL, '', 150, '2022-05-22', 6),
(114, 'Other Expenses', 'hgfd', 'Ask My Accountant', '', NULL, '', 150, '2022-04-14', 6),
(115, 'Other Expenses', 'cx', 'Ask My Accountant', '', NULL, '', 150, '2022-03-20', 6),
(116, 'Other Income', '', 'Finance Charge Income', '', NULL, '', 150, '2022-03-04', 6),
(117, 'Other Income', 'sad', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-08-03', 6),
(118, 'Other Income', 'zxvc', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-07-04', 6),
(119, 'Other Income', 'df', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-06-22', 6),
(120, 'Other Income', '', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-05-22', 6),
(121, 'Other Income', 'gfdf', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-04-14', 6),
(122, 'Other Income', 'fds', 'Shipping and Delivery Income', '', NULL, '', 150, '2022-03-20', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_accountype`
--

CREATE TABLE `app1_accountype` (
  `accountypeid` int(11) NOT NULL,
  `accountname` varchar(100) NOT NULL,
  `accountbal` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_accountype`
--

INSERT INTO `app1_accountype` (`accountypeid`, `accountname`, `accountbal`, `cid_id`) VALUES
(1, 'Inventory', '0', 6),
(2, 'Inventory', '0', 6),
(3, 'Inventory', '0', 6),
(4, 'Inventory', '0', 6),
(5, 'Inventory', '0', 6),
(6, 'Inventory', '0', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_addac`
--

CREATE TABLE `app1_addac` (
  `id` bigint(20) NOT NULL,
  `acname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  `dateadded` date NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_addtax1`
--

CREATE TABLE `app1_addtax1` (
  `addtax1id` int(11) NOT NULL,
  `taxname` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_advancepayment`
--

CREATE TABLE `app1_advancepayment` (
  `advancepaymentid` int(11) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `account` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `paymentdate` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `memo` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_advancepayment`
--

INSERT INTO `app1_advancepayment` (`advancepaymentid`, `payee`, `account`, `address`, `amount`, `paymentdate`, `refno`, `memo`, `cid_id`) VALUES
(1, 'SADSADSD', 'jksdfn', 'ASDSDDSSDS\nSADSADSD\n\n\n\n\n\n', '200000', '2022-09-17', '32', 'fgdgfgfdg\n\n\n', 6),
(2, 'sdfds', 'jksdfn', 'dfssdf\nsdfds\nsdfds\ndsfds\nff\n\n\n', '1', '2022-09-15', '12', 'cvcv\n', 6),
(3, 'SADSADSD', 'Cash and cash equivalents', 'ASDSDDSSDS\nSADSADSD\n\n\n\n\n\n', '2000', '2022-09-14', '2032', 'asasSas\n', 6),
(4, 'karun dfdsfsd', '', 'karundfdsfsd\nasd\n\n\n\n\n\nAfghanistan\n', '800', '2022-09-21', '7', 'fdsdfsfd\n', 6),
(5, 'karun dfdsfsd', 'Advance Payment Asset', 'karundfdsfsd\nasd\n\n\n\n\n\nAfghanistan\n', '800', '2022-09-21', '7', 'xzcz\n', 6),
(6, 'karun dfdsfsd', 'Cash and cash equivalents', 'karundfdsfsd\nasd\n\n\n\n\n\nAfghanistan\n', '800', '2022-09-21', '7', 'asddasd\n', 6),
(7, 'karun dfdsfsd', 'Advance Payment Asset', 'karundfdsfsd\nasd\n\n\n\n\n\nAfghanistan\n', '200', '2022-09-23', '7', 'asdsasd\n', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_bankstatement`
--

CREATE TABLE `app1_bankstatement` (
  `bankstatementid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `debit` double DEFAULT NULL,
  `credit` double DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_bankstatement`
--

INSERT INTO `app1_bankstatement` (`bankstatementid`, `name`, `date`, `description`, `debit`, `credit`, `cid_id`) VALUES
(2, '', '', '', 200, 3000, 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_bills`
--

CREATE TABLE `app1_bills` (
  `billid` int(11) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `paymacnt` varchar(100) NOT NULL,
  `paymdate` varchar(100) NOT NULL,
  `paymmethod` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `totamt` varchar(100) NOT NULL,
  `category1` varchar(100) NOT NULL,
  `descrptin1` varchar(100) NOT NULL,
  `catqty1` varchar(100) NOT NULL,
  `catprice1` varchar(100) NOT NULL,
  `cattotal1` varchar(100) NOT NULL,
  `category2` varchar(100) NOT NULL,
  `descrptin2` varchar(100) NOT NULL,
  `catqty2` varchar(100) NOT NULL,
  `catprice2` varchar(100) NOT NULL,
  `cattotal2` varchar(100) NOT NULL,
  `category3` varchar(100) NOT NULL,
  `descrptin3` varchar(100) NOT NULL,
  `catqty3` varchar(100) NOT NULL,
  `catprice3` varchar(100) NOT NULL,
  `cattotal3` varchar(100) NOT NULL,
  `category4` varchar(100) NOT NULL,
  `descrptin4` varchar(100) NOT NULL,
  `catqty4` varchar(100) NOT NULL,
  `catprice4` varchar(100) NOT NULL,
  `cattotal4` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `price2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `product4` varchar(100) NOT NULL,
  `hsn4` varchar(100) NOT NULL,
  `description4` varchar(100) NOT NULL,
  `qty4` varchar(100) NOT NULL,
  `price4` varchar(100) NOT NULL,
  `total4` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `tax4` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `grandtotal` varchar(100) NOT NULL,
  `payornot` varchar(100) DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_bundle`
--

CREATE TABLE `app1_bundle` (
  `bundleid` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `sku` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `product1` varchar(100) DEFAULT NULL,
  `product2` varchar(100) DEFAULT NULL,
  `product3` varchar(100) DEFAULT NULL,
  `product4` varchar(100) DEFAULT NULL,
  `hsn1` varchar(100) DEFAULT NULL,
  `hsn2` varchar(100) DEFAULT NULL,
  `hsn3` varchar(100) DEFAULT NULL,
  `hsn4` varchar(100) DEFAULT NULL,
  `description1` varchar(255) DEFAULT NULL,
  `description2` varchar(255) DEFAULT NULL,
  `description3` varchar(255) DEFAULT NULL,
  `description4` varchar(255) DEFAULT NULL,
  `qty1` int(11) DEFAULT NULL,
  `qty2` int(11) DEFAULT NULL,
  `qty3` int(11) DEFAULT NULL,
  `qty4` int(11) DEFAULT NULL,
  `price1` double DEFAULT NULL,
  `price2` double DEFAULT NULL,
  `price3` double DEFAULT NULL,
  `price4` double DEFAULT NULL,
  `total1` double DEFAULT NULL,
  `total2` double DEFAULT NULL,
  `total3` double DEFAULT NULL,
  `total4` double DEFAULT NULL,
  `tax1` varchar(255) DEFAULT NULL,
  `tax2` varchar(255) DEFAULT NULL,
  `tax3` varchar(255) DEFAULT NULL,
  `tax4` varchar(255) DEFAULT NULL,
  `grandtotal` double DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_bundle`
--

INSERT INTO `app1_bundle` (`bundleid`, `image`, `name`, `sku`, `description`, `product1`, `product2`, `product3`, `product4`, `hsn1`, `hsn2`, `hsn3`, `hsn4`, `description1`, `description2`, `description3`, `description4`, `qty1`, `qty2`, `qty3`, `qty4`, `price1`, `price2`, `price3`, `price4`, `total1`, `total2`, `total3`, `total4`, `tax1`, `tax2`, `tax3`, `tax4`, `grandtotal`, `cid_id`) VALUES
(1, '', 'key', '1221', '1fggfdf', 'key1', 'key2', 'key3', 'key4', '123', '122', '124', '1245', 'sdfdf', 'ddfs', 'sdfd', 'dsf', 1, 1, 1, 1, 200, 200, 200, 200, 400, 400, 400, 400, '28.0% GST (28%)', '28.0% GST (28%)', '28.0% GST (28%)', '28.0% GST (28%)', 20000, 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_cheqs`
--

CREATE TABLE `app1_cheqs` (
  `chequeid` int(11) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `bankacc` varchar(100) NOT NULL,
  `mailaddr` varchar(100) NOT NULL,
  `paydate` varchar(100) NOT NULL,
  `chequeno` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `category1` varchar(100) NOT NULL,
  `descrptin1` varchar(100) NOT NULL,
  `catqty1` varchar(100) NOT NULL,
  `catprice1` varchar(100) NOT NULL,
  `cattotal1` varchar(100) NOT NULL,
  `category2` varchar(100) NOT NULL,
  `descrptin2` varchar(100) NOT NULL,
  `catqty2` varchar(100) NOT NULL,
  `catprice2` varchar(100) NOT NULL,
  `cattotal2` varchar(100) NOT NULL,
  `category3` varchar(100) NOT NULL,
  `descrptin3` varchar(100) NOT NULL,
  `catqty3` varchar(100) NOT NULL,
  `catprice3` varchar(100) NOT NULL,
  `cattotal3` varchar(100) NOT NULL,
  `category4` varchar(100) NOT NULL,
  `descrptin4` varchar(100) NOT NULL,
  `catqty4` varchar(100) NOT NULL,
  `catprice4` varchar(100) NOT NULL,
  `cattotal4` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `price2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `product4` varchar(100) NOT NULL,
  `hsn4` varchar(100) NOT NULL,
  `description4` varchar(100) NOT NULL,
  `qty4` varchar(100) NOT NULL,
  `price4` varchar(100) NOT NULL,
  `total4` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `tax4` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `grandtotal` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_company`
--

CREATE TABLE `app1_company` (
  `cid` int(11) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `caddress` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `cemail` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `cimg` varchar(100) NOT NULL,
  `bname` varchar(100) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `ctype` varchar(100) NOT NULL,
  `abt` varchar(100) NOT NULL,
  `paid` varchar(100) NOT NULL,
  `id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_company`
--

INSERT INTO `app1_company` (`cid`, `cname`, `caddress`, `city`, `state`, `pincode`, `cemail`, `phone`, `cimg`, `bname`, `industry`, `ctype`, `abt`, `paid`, `id_id`) VALUES
(6, 'Clowns', 'Clown Chottanikkara', 'Chottanikkara', 'Kerala', '682312', 'clow@gmail.com', '8848937577', '386infox.png', 'Clowns', 'Cash', 'sdfgfg', 'Yes', 'dfgfdgfd', 26),
(12, 'sadsad', 'sad', 'sad', 'asdd', '2154', 'Saiju@gmail.com', '7854212365', '386infox.png', 'sdfdf', 'Cash', 'sdfds', 'Yes', 'sdffd', 38),
(14, 'sad', 'sadsa', 'sada', 'Defaultsadas', 'Pincodesadsa', 'sadsad@gmail.com', '8848937577', '386infox.png', '', '', '', '', '', 42),
(16, 'Saibu', 'Sai cho', 'cho', 'asdsads', '2154', 'ssas@gmail.com', '2154873256', 'avatar-7.png', 'dsfdsf', 'Accounting Services', 'Public Limited Company', 'Yes', 'Cheque', 44),
(17, 'sadsa', 'sads', 'sdsa', 'Black', '15424', 'sadsa@gmail.com', '7854213265', 'avatar-5.png', '', '', '', '', '', 45),
(20, 'sdf', 'sdf', 'sddf', 'Algeria', '215487', 'sdf@gmail.com', '1254872365', 'avatar-8.png', 'fghgf', 'Consultants, doctors, Lawyers and similar', 'Public Limited Company', 'Yes', 'Credit card/Debit card', 52),
(21, 'sad', 'sads', 'sadsa', 'Algeria', '125487', 'sad@gmail.com', '2145872652', 'avatar-12.png', '', '', '', '', '', 53),
(22, 'sadsad', 'sasad', 'sad', 'Afghanistansadsad', '0215487', 'sadsad@gmail.com', '1254878965', 'avatar-11.png', 'Legal Business Name', 'Information Tecnology', 'Joint-Venture Company', 'Yes', 'Cheque', 54),
(23, 'Clens', 'sdsa', 'cho', 'India', '682032', 'clens@gmail.com', '8848956788', 'avatar-5.png', 'clens', 'Information Tecnology', 'Public Limited Company', 'Yes', 'Cheque', 55);

-- --------------------------------------------------------

--
-- Table structure for table `app1_credit`
--

CREATE TABLE `app1_credit` (
  `creditnoteid` int(11) NOT NULL,
  `customer` varchar(100) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `biladdr` varchar(100) NOT NULL,
  `creditdate` varchar(100) NOT NULL,
  `creditno` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `invnum` varchar(100) NOT NULL,
  `invperiod` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `descrip` varchar(100) NOT NULL,
  `qty` int(11) DEFAULT NULL,
  `price` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `subtot` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `grndtot` int(11) DEFAULT NULL,
  `taxamnt` int(11) DEFAULT NULL,
  `product1` varchar(100) NOT NULL,
  `descrip1` varchar(100) NOT NULL,
  `qty1` int(11) DEFAULT NULL,
  `price1` varchar(100) NOT NULL,
  `tax1` varchar(100) NOT NULL,
  `total1` int(11) DEFAULT NULL,
  `product2` varchar(100) NOT NULL,
  `descrip2` varchar(100) NOT NULL,
  `qty2` int(11) DEFAULT NULL,
  `price2` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `total2` int(11) DEFAULT NULL,
  `product3` varchar(100) NOT NULL,
  `descrip3` varchar(100) NOT NULL,
  `qty3` int(11) DEFAULT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` int(11) DEFAULT NULL,
  `tax3` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_credit`
--

INSERT INTO `app1_credit` (`creditnoteid`, `customer`, `mail`, `biladdr`, `creditdate`, `creditno`, `place`, `invnum`, `invperiod`, `product`, `descrip`, `qty`, `price`, `tax`, `subtot`, `total`, `grndtot`, `taxamnt`, `product1`, `descrip1`, `qty1`, `price1`, `tax1`, `total1`, `product2`, `descrip2`, `qty2`, `price2`, `tax2`, `total2`, `product3`, `descrip3`, `qty3`, `price3`, `total3`, `tax3`, `cid_id`) VALUES
(1, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1001', 'Kerala', '0', '', 'Mouse', 'xcv', 1, '200.0', '28', 200, 200, 0, 0, '', '', 0, '', '0', 0, '', '', 0, '', '0', 0, '', '', 0, '', 0, '0', 6),
(2, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1002', 'Kerala', '0', '', 'Mouse', 'xcv', 1, '200.0', '28', 200, 200, 0, 0, '', '', 0, '', '0', 0, '', '', 0, '', '0', 0, '', '', 0, '', 0, '0', 6),
(3, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1003', 'Andaman and Nicobar Islads', '0', '', 'Mouse', 'xcv', 0, '200.0', '28', 0, 0, 0, 0, '', '', 0, '', '0', 0, '', '', 0, '', '0', 0, '', '', 0, '', 0, '0', 6),
(4, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-01', '1012', 'Madhya Predesh', '1005', '', 'Mouse', '', 1, '200.0', '28', 600, 200, 748, 148, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 0, '200.0', 0, '28', 6),
(5, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-28', '1005', 'Assam', '1005', '', 'Mouse', '', 1, '200.0', '28', 800, 200, 1004, 204, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 1, '200.0', 200, '28', 6),
(6, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-28', '1006', 'Assam', '1005', '', 'Mouse', '', 1, '200.0', '28', 800, 200, 1004, 204, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 1, '200.0', 200, '28', 6),
(7, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-28', '1007', 'Arunachal Predesh', '1005', '', 'Mouse', '', 1, '200.0', '28', 800, 200, 1004, 204, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 1, '200.0', 200, '28', 6),
(8, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-01', '1012', 'Madhya Predesh', '1005', '', 'Mouse', '', 1, '200.0', '28', 600, 200, 748, 148, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 0, '200.0', 0, '28', 6),
(9, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-30', '1009', 'Andaman and Nicobar Islads', '1005', '', 'Mouse', '', 1, '200.0', '28', 600, 200, 748, 148, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 0, '200.0', 0, '28', 6),
(10, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-30', '1010', 'Kerala', '1005', '', 'Mouse', '', 1, '200.0', '28', 600, 200, 748, 148, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 0, '200.0', 0, '28', 6),
(11, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-01', '1012', 'Madhya Predesh', '1005', '', 'Mouse', '', 1, '200.0', '28', 600, 200, 748, 148, 'Mouse', '', 1, '200.0', '18', 200, 'Mouse', '', 1, '200.0', '28', 200, 'Mouse', '', 0, '200.0', 0, '28', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_customer`
--

CREATE TABLE `app1_customer` (
  `customerid` int(11) NOT NULL,
  `title` varchar(10) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gsttype` varchar(100) DEFAULT NULL,
  `gstin` varchar(100) NOT NULL,
  `panno` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `website` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `shipstreet` varchar(100) DEFAULT NULL,
  `shipcity` varchar(100) DEFAULT NULL,
  `shipstate` varchar(100) DEFAULT NULL,
  `shippincode` varchar(100) DEFAULT NULL,
  `shipcountry` varchar(100) DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_customer`
--

INSERT INTO `app1_customer` (`customerid`, `title`, `firstname`, `lastname`, `company`, `location`, `gsttype`, `gstin`, `panno`, `email`, `website`, `mobile`, `street`, `city`, `state`, `pincode`, `country`, `shipstreet`, `shipcity`, `shipstate`, `shippincode`, `shipcountry`, `cid_id`) VALUES
(1, '', 'ASDSD', 'DSSDS', 'SADSADSD', '', NULL, '', NULL, '', '', '', '', '', '', '', '', NULL, NULL, NULL, NULL, NULL, 6),
(2, '', '', '', '', '', NULL, '', NULL, '', '', '', '', '', '', '', '', NULL, NULL, NULL, NULL, NULL, 6),
(3, 'Mr', '', '', '', '', 'Choose...', '29APPCK7465F1Z1', 'APPCK7465F', 'saiju@gmail.com', '', '', 'sda', 'sadsad', 'sdsad', 'asds', 'sad', 'sda', 'sadsad', 'sdsad', 'sadsa', 'das', 6),
(4, 'Mrs', 'zxcxz', 'xzcxzcz', '', '', 'GST registered Regular', '29APPCK7465F1Z1', 'APPCK7465F', '', '', '', 'asds', 'sad', 'sads', '', '', 'asds', 'sad', 'sads', '', '', 6),
(5, 'Mrs', 'ASA', 'ASASAS', '', '', 'Choose...', '29APPCK7465F1Z1', 'APPCK7465F', '', '', '2154879865', 'dsf', 'sd', 'kerala', 'ds', 'ds', 'dsf', 'sd', '', 'ds', 'ds', 6),
(6, 'Mr', 'dfs', 'sdf', 'sdfds', 'sdf', 'Choose...', '29APPCK7465F1Z1', 'APPCK7465F', '', '', '', 'sdfds', 'dsfds', 'ff', '', '', 'sdfds', 'dsfds', 'ff', '', '', 6),
(7, 'Mrs', 'fdgfdgdg', 'fdgfdg', 'fdgg', 'fdgdfg', 'SEZ', '', 'APPCK7465F', 'dfgdgdfg@gmail.com', '', '1254879898', 'asda', 'asdas', 'sdad', 'asdsd', 'sdsdd', 'asda', 'asdas', 'sdad', 'asdsd', 'sdsdd', 6),
(8, 'Mrs', 'ram', 'kum', 'sdsad', 'asdsa', 'GST registered Regular', '29APPCK7465F1Z1', 'APPCK7465F', 'fdg@gmail.com', '', '8848937577', 'sdfd', 'sdfsd', 'fdf', 'df', 'fdfdf', 'sdfd', 'sdfsd', 'fdf', 'df', 'fdfdf', 6),
(9, 'Mrs', 'Amal ', 'Neerath', 'Amals', 'Kochi', 'GST registered Regular', '29APPCK7465F1Z1', 'gfddgfd', 'am@gmail.com', '', '8848937577', 'sdfsdfdfd', 'sdfds', 'sdfsd', '25154', 'dsfsdf', 'sdfsdfdfd', 'sdfds', 'sdfsd', '25154', 'dsfsdf', 6),
(10, 'Mrs', 'Amal ', 'Neerath', 'Amals', 'Kochi', 'GST registered Regular', '29APPCK7465F1Z1', 'gfddgfd', 'am@gmail.com', '', '8848937577', 'sdfsdfdfd', 'sdfds', 'sdfsd', '25154', 'dsfsdf', 'sdfsdfdfd', 'sdfds', 'sdfsd', '25154', 'dsfsdf', 6),
(11, 'Mr', 'Amal', 'Leenath', 'amals', 'Kochi', 'GST registered Regular', '214451154512425145fdgfdg', 'fdgfdgfdgfdgfdgfdgfdgdgfgd', 'fdgfdgdf@gmail.com', '', '8754213265', 'asddsa', 'dasdsd', 'sda', 'dsad', 'dsadads', 'asddsa', 'dasdsd', 'sda', 'dsad', 'dsadads', 6),
(12, 'Mr', 'Arjun ', 'Ameeth', '', '', 'Choose...', '29APPCK7465F1Z1', 'APPCK7465F', '', '', '', '', '', '', '', '', '', '', '', '', '', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_customize`
--

CREATE TABLE `app1_customize` (
  `customizeid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `template` varchar(255) NOT NULL,
  `pcolour` varchar(255) NOT NULL,
  `scolour` varchar(255) NOT NULL,
  `fonts` varchar(255) NOT NULL,
  `lastedited` varchar(255) NOT NULL,
  `selected` varchar(255) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_delayedcharge`
--

CREATE TABLE `app1_delayedcharge` (
  `delayedchargeid` int(11) NOT NULL,
  `customer` varchar(100) NOT NULL,
  `delayedchargedate` varchar(100) NOT NULL,
  `delayedchargeno` varchar(100) NOT NULL,
  `prodorser` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `rate` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `grandtotal` varchar(100) NOT NULL,
  `prodorser1` varchar(100) NOT NULL,
  `description1` varchar(100) NOT NULL,
  `qty1` varchar(100) NOT NULL,
  `rate1` varchar(100) NOT NULL,
  `total1` varchar(100) NOT NULL,
  `tax1` varchar(100) NOT NULL,
  `prodorser2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `rate2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `prodorser3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `rate3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_delayedcharge`
--

INSERT INTO `app1_delayedcharge` (`delayedchargeid`, `customer`, `delayedchargedate`, `delayedchargeno`, `prodorser`, `description`, `qty`, `rate`, `tax`, `total`, `subtotal`, `grandtotal`, `prodorser1`, `description1`, `qty1`, `rate1`, `total1`, `tax1`, `prodorser2`, `description2`, `qty2`, `rate2`, `total2`, `tax2`, `prodorser3`, `description3`, `qty3`, `rate3`, `total3`, `tax3`, `taxamount`, `cid_id`) VALUES
(1, 'zxcxz xzcxzcz', '2022-09-30', '1001', 'Mouse', '', '1', '200', '28', '200', '800.0', '1024.0', 'Mouse', '', '1', '200', '200', '28', 'Mouse', '', '1', '200', '200', '28', 'Mouse', '', '1', '200', '200', '28', '224.0', 6),
(2, 'Amal  Neerath', '2022-09-30', '1002', 'Mouse', '', '1', '200', '28', '200', '200.0', '256.0', '', '', '0', '', '0', '0', '', '', '0', '', '0', '0', '', '', '0', '', '0', '0', '56.0', 6),
(3, 'ram kum', '2022-09-30', '1003', 'Mouse', 'asddssasd', '1', '200', '28', '200', '200.0', '256.0', '', '', '0', '', '0', '0', '', '', '0', '', '0', '0', '', '', '0', '', '0', '0', '56.0', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_employee`
--

CREATE TABLE `app1_employee` (
  `employeeid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `joiningdate` varchar(100) NOT NULL,
  `employeenumber` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `gmail` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `providebankdetails` varchar(20) NOT NULL,
  `bankaccountnumber` varchar(100) NOT NULL,
  `ifsccode` varchar(100) NOT NULL,
  `hrareceived` varchar(20) NOT NULL,
  `totalrentpaid` varchar(100) NOT NULL,
  `livein` varchar(100) NOT NULL,
  `applicabletaxregime` varchar(100) NOT NULL,
  `pannumber` varchar(100) NOT NULL,
  `aadhaarnumber` varchar(100) NOT NULL,
  `universalaccountnumber` varchar(100) NOT NULL,
  `pfaccountnumber` varchar(100) NOT NULL,
  `epsaccountnumber` varchar(100) NOT NULL,
  `praccountnumber` varchar(100) NOT NULL,
  `esinumber` varchar(100) NOT NULL,
  `esidispensaryname` varchar(100) NOT NULL,
  `basic` varchar(100) NOT NULL,
  `da` varchar(100) NOT NULL,
  `othincome1` varchar(100) NOT NULL,
  `othincome2` varchar(100) NOT NULL,
  `othincome3` varchar(100) NOT NULL,
  `othincome4` varchar(100) NOT NULL,
  `othincome5` varchar(100) NOT NULL,
  `othamount1` varchar(100) NOT NULL,
  `othamount2` varchar(100) NOT NULL,
  `othamount3` varchar(100) NOT NULL,
  `othamount4` varchar(100) NOT NULL,
  `othamount5` varchar(100) NOT NULL,
  `provifund` varchar(100) NOT NULL,
  `proftax` varchar(100) NOT NULL,
  `esi` varchar(100) NOT NULL,
  `deduc1` varchar(100) NOT NULL,
  `deduc2` varchar(100) NOT NULL,
  `deduc3` varchar(100) NOT NULL,
  `deduc4` varchar(100) NOT NULL,
  `deducamt1` varchar(100) NOT NULL,
  `deducamt2` varchar(100) NOT NULL,
  `deducamt3` varchar(100) NOT NULL,
  `deducamt4` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_employee`
--

INSERT INTO `app1_employee` (`employeeid`, `name`, `joiningdate`, `employeenumber`, `designation`, `department`, `branch`, `location`, `gender`, `age`, `mobile`, `gmail`, `address`, `providebankdetails`, `bankaccountnumber`, `ifsccode`, `hrareceived`, `totalrentpaid`, `livein`, `applicabletaxregime`, `pannumber`, `aadhaarnumber`, `universalaccountnumber`, `pfaccountnumber`, `epsaccountnumber`, `praccountnumber`, `esinumber`, `esidispensaryname`, `basic`, `da`, `othincome1`, `othincome2`, `othincome3`, `othincome4`, `othincome5`, `othamount1`, `othamount2`, `othamount3`, `othamount4`, `othamount5`, `provifund`, `proftax`, `esi`, `deduc1`, `deduc2`, `deduc3`, `deduc4`, `deducamt1`, `deducamt2`, `deducamt3`, `deducamt4`, `cid_id`) VALUES
(1, '', '9/23/22', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(2, 'sdasads', '9/23/22', '202112', 'Tl', 'it', 'sad', 'asds', 'Male', '20', '8847589645', 'jhdsgfdsjhg@gmail.com', '', 'Yes', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0', '', '', '', '', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(3, 'sdfd', '9/23/22', '21546', 'it', 'it', 'fgh', 'gfhgf', 'Male', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '20000', '0', '', '', '', '', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_estimate`
--

CREATE TABLE `app1_estimate` (
  `estimateid` int(11) NOT NULL,
  `customer` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `billingaddress` varchar(100) NOT NULL,
  `estimatedate` varchar(100) NOT NULL,
  `expirationdate` varchar(100) NOT NULL,
  `estimateno` varchar(100) NOT NULL,
  `placeofsupply` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `rate` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `estimatetotal` varchar(100) NOT NULL,
  `product1` varchar(100) NOT NULL,
  `hsn1` varchar(100) NOT NULL,
  `description1` varchar(100) NOT NULL,
  `qty1` varchar(100) NOT NULL,
  `rate1` varchar(100) NOT NULL,
  `total1` varchar(100) NOT NULL,
  `tax1` varchar(100) NOT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `rate2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `rate3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL,
  `ref_no` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_estimate`
--

INSERT INTO `app1_estimate` (`estimateid`, `customer`, `email`, `billingaddress`, `estimatedate`, `expirationdate`, `estimateno`, `placeofsupply`, `product`, `hsn`, `description`, `qty`, `rate`, `total`, `tax`, `subtotal`, `estimatetotal`, `product1`, `hsn1`, `description1`, `qty1`, `rate1`, `total1`, `tax1`, `product2`, `hsn2`, `description2`, `qty2`, `rate2`, `total2`, `tax2`, `product3`, `hsn3`, `description3`, `qty3`, `rate3`, `total3`, `tax3`, `taxamount`, `cid_id`, `ref_no`, `status`) VALUES
(1, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '2022-09-27', '1001', 'Kerala', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', '400.0', '512.0', 'Mouse', 'fdg2154', '', '1', '200', '0', '28', 'Mouse', 'fdg2154', '', '3', '200', '200', '28', 'Mouse', 'fdg2154', '', '0', '200', '0', '28', '112.0', 6, '', ''),
(2, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '2022-09-27', '1002', 'Kerala', 'key', '1221', '1fggfdf', '1', '20000.0', '20000', '28', '20600.0', '26328.0', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', 'Mouse', 'fdg2154', '', '1', '200', '200', '18', 'Mouse', 'fdg2154', '', '1', '200', '200', '18', '5728.0', 6, '', ''),
(3, 'fdgfdgdg fdgfdg', 'dfgdgdfg@gmail.com', 'fdgfdgdg fdgfdg\nfdgg\nasda\nasdas\nsdad\nasdsd\nsdsdd', '2022-09-27', '2022-09-27', '1003', 'Kerala', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', '800.0', '1004.0', 'Mouse', 'fdg2154', '', '1', '200', '200', '18', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', '204.0', 6, '', ''),
(4, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '2022-09-27', '1004', 'Kerala', 'pen', '2154', '', '1', '2500', '2500', '28', '2500.0', '3200.0', '', '', '', '0', '', '0', '0', '', '', '', '0', '', '0', '0', '', '', '', '0', '', '0', '0', '700.0', 6, '', ''),
(5, 'Amal  Neerath', '', '', '2022-09-30', '2022-09-30', '1005', 'Kochi', 'Mouse', 'fdg2154', '', '1', '200', '200', '18', '800.0', '1004.0', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', 'Mouse', 'fdg2154', '', '1', '200', '200', '28', '204.0', 6, '', ''),
(6, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-30', '2022-09-30', '1006', 'Kerala', 'Mouse', 'fdg2154', 'asddssasd', '1', '200', '200', '28', '200.0', '256.0', '', '', '', '0', '', '0', '0', '', '', '', '0', '', '0', '0', '', '', '', '0', '', '0', '0', '56.0', 6, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `app1_expences`
--

CREATE TABLE `app1_expences` (
  `expencesid` int(11) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `paymdate` varchar(100) NOT NULL,
  `paymmethod` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `totamt` varchar(100) NOT NULL,
  `category1` varchar(100) NOT NULL,
  `descrptin1` varchar(100) NOT NULL,
  `catqty1` varchar(100) NOT NULL,
  `catprice1` varchar(100) NOT NULL,
  `cattotal1` varchar(100) NOT NULL,
  `category2` varchar(100) NOT NULL,
  `descrptin2` varchar(100) NOT NULL,
  `catqty2` varchar(100) NOT NULL,
  `catprice2` varchar(100) NOT NULL,
  `cattotal2` varchar(100) NOT NULL,
  `category3` varchar(100) NOT NULL,
  `descrptin3` varchar(100) NOT NULL,
  `catqty3` varchar(100) NOT NULL,
  `catprice3` varchar(100) NOT NULL,
  `cattotal3` varchar(100) NOT NULL,
  `category4` varchar(100) NOT NULL,
  `descrptin4` varchar(100) NOT NULL,
  `catqty4` varchar(100) NOT NULL,
  `catprice4` varchar(100) NOT NULL,
  `cattotal4` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `price2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `product4` varchar(100) NOT NULL,
  `hsn4` varchar(100) NOT NULL,
  `description4` varchar(100) NOT NULL,
  `qty4` varchar(100) NOT NULL,
  `price4` varchar(100) NOT NULL,
  `total4` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `tax4` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `grandtotal` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_expences`
--

INSERT INTO `app1_expences` (`expencesid`, `payee`, `paymdate`, `paymmethod`, `refno`, `totamt`, `category1`, `descrptin1`, `catqty1`, `catprice1`, `cattotal1`, `category2`, `descrptin2`, `catqty2`, `catprice2`, `cattotal2`, `category3`, `descrptin3`, `catqty3`, `catprice3`, `cattotal3`, `category4`, `descrptin4`, `catqty4`, `catprice4`, `cattotal4`, `product`, `hsn`, `description`, `qty`, `price`, `total`, `product2`, `hsn2`, `description2`, `qty2`, `price2`, `total2`, `product3`, `hsn3`, `description3`, `qty3`, `price3`, `total3`, `product4`, `hsn4`, `description4`, `qty4`, `price4`, `total4`, `subtotal`, `tax`, `tax2`, `tax3`, `tax4`, `taxamount`, `grandtotal`, `cid_id`) VALUES
(4, 'ASA ASASAS', '2022-09-22', 'Debit cards', '', '', 'lkl', 'dfsd', '1', '200', '200', 'lkl', 'dsfd', '2', '200', '400', 'ZzxzZx', 'fd', '3', '300', '900', 'lkl', 'fdfd', '4', '400', '1600', 'Mouse', 'fdg2154', 'sd\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'sdfd\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'sdf\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'sdf\n', '1', '100', '200.0', '3900.0', '18.0% GST(18%)', '18.0% GST(18%)', '18.0% GST(18%)', '28.0% GST(28%)', '164.0', '0.0', 6),
(6, 'zxcxz xzcxzcz', '2022-09-20', 'Debit cards', '', '', 'Consulting Income', 'asdhagsdhj', '1', '200', '200', 'Consulting Income', 'dfssf', '1', '100', '100', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'fdgf\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'fdg\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'fdgfd\n\n', '2', '200.0', '400.0', 'Mouse', 'fdg2154', 'fdgfd\n\n', '1', '200.0', '200.0', '1300.0', '28.0% GST(28%)', '18.0% GST(18%)', '28.0% GST(28%)', 'Choose', '148.0', '-1048.0', 6),
(7, 'karun dfdsfsd', '2022-09-21', 'Cheque', '', '', 'Uncategorised Income', 'sfd', '1', '100', '100', 'Sales', 'sdfd', '1', '200', '200', 'Consulting Income', 'sdfsd', '1', '300', '300', 'Sales-Hardware', 'fdfsdf', '1', '400', '400', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdas\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', '1800.0', '28.0% GST(28%)', '18.0% GST(18%)', '28.0% GST(28%)', '28.0% GST(28%)', '204.0', '1804.0', 6),
(8, 'fdgfdgdg fdgfdg', '2022-09-15', 'Cheque', '', '', 'lkl', 'asdsa', '1', '100', '100', 'Billable Expense Income', 'sadsa', '1', '200', '200', 'lkl', 'dsd', '1', '200', '200', 'Billable Expense Income', 'asdasd', '1', '200', '200', 'key', '1221', '1fggfdf\n', '1', '20000.0', '20000.0', 'Mouse', 'fdg2154', 'sadsd\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'sadas\n', '1', '200.0', '200.0', 'key', '1221', '1fggfdf\n', '1', '200', '200', '21100.0', '28.0% GST(28%)', '28.0% GST(28%)', '28.0% GST(28%)', '28.0% GST(28%)', '5768.0', '-26068.0', 6),
(9, 'dfs sdf', '2022-09-23', 'Cheque', '', '', 'Billable Expense Income', 'fdgf', '1', '200', '200', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'cxvvcc\n', '1', '200.0', '200.0', '', '', '\n', '0', '0', '', '', '', '\n', '0', '0', '', '', '', '\n', '0', '0', '', '400.0', '28.0% GST(28%)', 'Choose', 'Choose', 'Choose', '56.0', '456.0', 6),
(10, 'ram kum', '2022-09-23', 'Cash', '', '', 'Billable Expense Income', 'erwewrw', '1', '200', '200', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'sad\n', '1', '201', '201.0', '', '', '\n', '0', '0', '', '', '', '\n', '0', '0', '', '', '', '\n', '0', '0', '', '401.0', '28.0% GST(28%)', 'Choose', 'Choose', 'Choose', '56.28', '-200.0', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_expenseaccount`
--

CREATE TABLE `app1_expenseaccount` (
  `expenseid` int(11) NOT NULL,
  `account` varchar(100) NOT NULL,
  `begbal` varchar(100) NOT NULL,
  `endbal` varchar(100) NOT NULL,
  `enddate` varchar(100) DEFAULT NULL,
  `dat` varchar(100) DEFAULT NULL,
  `serchar` varchar(100) NOT NULL,
  `expacc` varchar(100) DEFAULT NULL,
  `type1` varchar(100) DEFAULT NULL,
  `memo1` varchar(100) DEFAULT NULL,
  `cid_id` int(11) NOT NULL,
  `expaccountypid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_incomeaccount`
--

CREATE TABLE `app1_incomeaccount` (
  `incomeid` int(11) NOT NULL,
  `dat1` varchar(100) DEFAULT NULL,
  `intear` varchar(100) NOT NULL,
  `incacc` varchar(100) DEFAULT NULL,
  `type2` varchar(100) DEFAULT NULL,
  `memo2` varchar(100) DEFAULT NULL,
  `cid_id` int(11) NOT NULL,
  `expenceincomeid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_inventory`
--

CREATE TABLE `app1_inventory` (
  `inventoryid` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `sku` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `initialqty` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `stockalrt` varchar(100) NOT NULL,
  `invacnt` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `salesprice` varchar(10) NOT NULL,
  `incomeacnt` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `purchaseinfo` varchar(100) NOT NULL,
  `cost` varchar(100) NOT NULL,
  `expacnt` varchar(100) NOT NULL,
  `purtax` varchar(100) NOT NULL,
  `revcharge` varchar(100) NOT NULL,
  `presupplier` varchar(100) NOT NULL,
  `cxq` double DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_inventory`
--

INSERT INTO `app1_inventory` (`inventoryid`, `image`, `name`, `sku`, `hsn`, `unit`, `category`, `initialqty`, `date`, `stockalrt`, `invacnt`, `description`, `salesprice`, `incomeacnt`, `tax`, `purchaseinfo`, `cost`, `expacnt`, `purtax`, `revcharge`, `presupplier`, `cxq`, `cid_id`) VALUES
(1, '', 'pen', '12121', '2154', '200', '', '100', '', '', '', 'gfdgffdgdfg', '2500', '', '2', '', '200', '', '', '', '', NULL, 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_invoice`
--

CREATE TABLE `app1_invoice` (
  `invoiceid` int(11) NOT NULL,
  `customername` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `invoiceno` int(11) NOT NULL,
  `terms` varchar(100) NOT NULL,
  `invoicedate` varchar(100) NOT NULL,
  `duedate` varchar(100) NOT NULL,
  `bname` varchar(255) NOT NULL,
  `placosupply` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` int(11) DEFAULT NULL,
  `price` varchar(100) NOT NULL,
  `total` int(11) DEFAULT NULL,
  `tax` varchar(100) NOT NULL,
  `subtotal` int(11) DEFAULT NULL,
  `grandtotal` int(11) DEFAULT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` int(11) DEFAULT NULL,
  `price2` varchar(100) NOT NULL,
  `total2` int(11) DEFAULT NULL,
  `tax2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` int(11) DEFAULT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` int(11) DEFAULT NULL,
  `tax3` varchar(100) NOT NULL,
  `product4` varchar(100) NOT NULL,
  `hsn4` varchar(100) NOT NULL,
  `description4` varchar(100) NOT NULL,
  `qty4` int(11) DEFAULT NULL,
  `price4` varchar(100) NOT NULL,
  `total4` int(11) DEFAULT NULL,
  `tax4` varchar(100) NOT NULL,
  `amtrecvd` int(11) DEFAULT NULL,
  `taxamount` int(11) DEFAULT NULL,
  `baldue` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_invoice`
--

INSERT INTO `app1_invoice` (`invoiceid`, `customername`, `email`, `invoiceno`, `terms`, `invoicedate`, `duedate`, `bname`, `placosupply`, `product`, `hsn`, `description`, `qty`, `price`, `total`, `tax`, `subtotal`, `grandtotal`, `product2`, `hsn2`, `description2`, `qty2`, `price2`, `total2`, `tax2`, `product3`, `hsn3`, `description3`, `qty3`, `price3`, `total3`, `tax3`, `product4`, `hsn4`, `description4`, `qty4`, `price4`, `total4`, `tax4`, `amtrecvd`, `taxamount`, `baldue`, `cid_id`) VALUES
(6, 'Silpa N S', 'silpa@gmail.com', 6, 'NET 60', '2022-08-31', '2022-10-30', 'Silpa N S\nIBM\nz street\nBanglore\nKarnataka\n680717\nIndia', 'Kerala', 'Inv_1', '1001', 'des', 1, '78.12', 78, '28.0% GST (28%)', 123, 150, 'Non_1', '1002', 'des1', 1, '44.64', 45, '12.0% GST (12%)', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 0, 27, '149.99', 16),
(8, 'Vishnu D', 'vishnu@gmail.com', 8, 'Due on Receipt', '2022-09-02', '2022-09-02', 'Vishnu D\nAmazon\nXYZ Street\nBanglore\nKarnataka\n680400\nIndia', 'Kerala', 'Inv_1', '1001', 'des', 1, '78.12', 78, '28.0% GST (28%)', 324, 400, 'Non_1', '1002', 'des1', 1, '44.64', 45, '12.0% GST (12%)', 'Inv_1', '1001', 'des', 1, '78.12', 78, '28.0% GST (28%)', 'Bun_1', 'N41554', 'des1', 0, '0', 0, 'Choose', 0, 76, '400.22', 16),
(10, 'Sonia Johny', 'sonia@gmail.com', 10, 'NET 15', '2022-09-02', '2022-09-17', 'Sonia Johny\nAspire\nStreet1\nKochi\nKerala\n680303\nIndia', 'Kerala', 'Inv_1', '1001', 'des', 1, '78.12', 78, '28.0% GST (28%)', 201, 250, 'Non_1', '1002', 'des1', 1, '44.64', 45, '12.0% GST (12%)', 'Inv_1', '1001', 'des', 1, '78.12', 78, '28.0% GST (28%)', '', '', '', 0, '0', 0, 'Choose', 0, 49, '249.98', 16),
(12, 'ASA ASASAS', 'sdfsd@gamil.com', 0, 'Due on Receipt', '2022-09-23', '2022-09-16', 'ASA ASASAS\n\ndsf\nsd\nkerala\nds\nds', 'Kerala', 'Mouse', 'fdg2154', 'xcv', 1, '200.0', 200, '28.0%\n GST(28%)', 200, 0, '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 2140, 0, '0.0', 6),
(13, 'dfs sdf', 'sdad@gmail.com', 0, 'NET 15', '2022-09-26', '2022-09-26', 'dfs sdf\nsdfds\nsdfds\ndsfds\nff\n\n', 'Kerala', 'Mouse', 'fdg2154', 'sadas', 1, '200.0', 200, '28.0% GST (28%)', 200, 256, '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 2140, 56, '0.0', 6),
(14, 'dfs sdf', 'dfsfds@gmail.com', 0, 'NET 15', '2022-09-26', '2022-09-26', 'dfs sdf\nsdfds\nsdfds\ndsfds\nff\n\n', 'Kerala', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 200, 256, '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 2140, 56, '0.0', 6),
(15, 'ASA ASASAS', '', 0, 'NET 15', '2022-09-26', '2022-10-11', 'ASA ASASAS\n\ndsf\nsd\nkerala\nds\nds', 'Kerala', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 400, 456, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0%\n GST(28%)', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 2140, 56, '0.0', 6),
(16, '', '', 0, '', '2022-09-26', '2022-09-26', '', 'Kerala', 'key', '1221', '1fggfdf', 2, '2500.0', 5000, 'Choose', 5600, 5748, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '18.0% GST (18%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 2140, 148, '0.0', 6),
(17, 'ram kum', 'fdg@gmail.com', 1005, 'NET 15', '2022-09-26', '2022-10-11', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', 'Kerala', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 800, 1004, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '18.0% GST (18%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 1644, 204, '0.0', 6),
(20, 'fdgfdgdg fdgfdg', 'dfgdgdfg@gmail.com', 0, 'NET 15', '2022-09-27', '2022-10-12', 'fdgfdgdg fdgfdg\nfdgg\nasda\nasdas\nsdad\nasdsd\nsdsdd', 'Kerala', 'pen', '2154', '', 1, '2500.0', 2500, '28.0% GST (28%)', 3100, 3948, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '18.0% GST (18%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 2140, 848, '0.0', 6),
(21, 'dfs sdf', 'sdsa@gmail.com', 0, 'NET 30', '2022-09-27', '2022-09-02', 'dfs sdf\nsdfds\nsdfds\ndsfds\nff\n\n', 'Kerala', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 800, 1024, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 2140, 224, '0.0', 6),
(23, 'Amal  Neerath', 'am@gmail.com', 0, 'NET 60', '2022-09-30', '2022-11-29', 'Amal  Neerath\nAmals\nsdfsdfdfd\nsdfds\nsdfsd\n25154\ndsfsdf', 'Kerala', 'pen', '2154', '', 1, '2500.0', 2500, '28.0% GST (28%)', 3100, 3968, 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', '', 1, '200.0', 200, '28.0% GST (28%)', 2140, 868, '0.0', 6),
(24, 'ram kum', 'fdg@gmail.com', 0, 'NET 30', '2022-09-30', '2022-10-30', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', 'Kerala', 'Mouse', 'fdg2154', 'asddssasd', 1, '200.0', 200, '28.0% GST (28%)', 600, 768, 'Mouse', 'fdg2154', 'asddssasd', 1, '200.0', 200, '28.0% GST (28%)', 'Mouse', 'fdg2154', 'asddssasd', 1, '200.0', 200, '28.0% GST (28%)', '', '', '', 0, '0', 0, 'Choose', 2140, 168, '0.0', 6),
(25, 'Amal Leenath', 'am@gmail.com', 0, 'NET 15', '2022-09-30', '2022-10-15', 'Amal  Neerath\nAmals\nsdfsdfdfd\nsdfds\nsdfsd\n25154\ndsfsdf', 'Kerala', 'Mouse', 'fdg2154', 'asddssasd', 1, '200.0', 200, '28.0% GST (28%)', 200, 256, '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 2140, 56, '0.0', 6),
(26, 'ram kum', 'fdg@gmail.com', 0, 'NET 30', '2022-10-01', '2022-10-31', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', 'Kerala', 'pen', '2154', 'gfdgffdgdfg', 2, '2500.0', 5000, '28.0% GST (28%)', 5000, 6400, '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', '', '', '', 0, '0', 0, 'Choose', 545, 1400, '5855.0', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_noninventory`
--

CREATE TABLE `app1_noninventory` (
  `noninventoryid` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `sku` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `descr` varchar(100) NOT NULL,
  `saleprice` varchar(100) NOT NULL,
  `income` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `purchasedescr` varchar(100) NOT NULL,
  `cost` varchar(100) NOT NULL,
  `expenseaccount` varchar(100) NOT NULL,
  `purchasetax` varchar(100) NOT NULL,
  `revcharge` varchar(100) NOT NULL,
  `presupplier` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_noninventory`
--

INSERT INTO `app1_noninventory` (`noninventoryid`, `image`, `name`, `sku`, `hsn`, `unit`, `category`, `descr`, `saleprice`, `income`, `tax`, `purchasedescr`, `cost`, `expenseaccount`, `purchasetax`, `revcharge`, `presupplier`, `qty`, `cid_id`) VALUES
(1, '', 'Mouse', '1254', 'fdg2154', '2', '', 'asddssasd', '200', '200', '2', '', '100', '', '', '', '', '108', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_paydowncreditcard`
--

CREATE TABLE `app1_paydowncreditcard` (
  `paycreditcardid` int(11) NOT NULL,
  `ccno` varchar(100) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `dateofpayment` varchar(100) NOT NULL,
  `discription` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_payment`
--

CREATE TABLE `app1_payment` (
  `paymentid` int(11) NOT NULL,
  `customer` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `findinvoice` varchar(100) DEFAULT NULL,
  `paymdate` varchar(100) NOT NULL,
  `pmethod` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `depto` varchar(100) NOT NULL,
  `amtreceived` varchar(100) NOT NULL,
  `descrip` varchar(100) NOT NULL,
  `duedate` varchar(10) NOT NULL,
  `orgamt` varchar(100) NOT NULL,
  `openbal` varchar(100) NOT NULL,
  `payment` varchar(100) NOT NULL,
  `amtapply` varchar(100) NOT NULL,
  `amtcredit` varchar(100) NOT NULL,
  `descrip1` varchar(100) NOT NULL,
  `duedate1` varchar(10) NOT NULL,
  `orgamt1` varchar(100) NOT NULL,
  `openbal1` varchar(100) NOT NULL,
  `payment1` varchar(100) NOT NULL,
  `descrip2` varchar(100) NOT NULL,
  `duedate2` varchar(10) NOT NULL,
  `orgamt2` varchar(100) NOT NULL,
  `openbal2` varchar(100) NOT NULL,
  `payment2` varchar(100) NOT NULL,
  `descrip3` varchar(100) NOT NULL,
  `duedate3` varchar(10) NOT NULL,
  `orgamt3` varchar(100) NOT NULL,
  `openbal3` varchar(100) NOT NULL,
  `payment3` varchar(100) NOT NULL,
  `descrip4` varchar(100) NOT NULL,
  `duedate4` varchar(10) NOT NULL,
  `orgamt4` varchar(100) NOT NULL,
  `openbal4` varchar(100) NOT NULL,
  `payment4` varchar(100) NOT NULL,
  `descrip5` varchar(100) NOT NULL,
  `duedate5` varchar(10) NOT NULL,
  `orgamt5` varchar(100) NOT NULL,
  `openbal5` varchar(100) NOT NULL,
  `payment5` varchar(100) NOT NULL,
  `descrip6` varchar(100) NOT NULL,
  `duedate6` varchar(10) NOT NULL,
  `orgamt6` varchar(100) NOT NULL,
  `openbal6` varchar(100) NOT NULL,
  `payment6` varchar(100) NOT NULL,
  `descrip7` varchar(100) NOT NULL,
  `duedate7` varchar(10) NOT NULL,
  `orgamt7` varchar(100) NOT NULL,
  `openbal7` varchar(100) NOT NULL,
  `payment7` varchar(100) NOT NULL,
  `descrip8` varchar(100) NOT NULL,
  `duedate8` varchar(10) NOT NULL,
  `orgamt8` varchar(100) NOT NULL,
  `openbal8` varchar(100) NOT NULL,
  `payment8` varchar(100) NOT NULL,
  `descrip9` varchar(100) NOT NULL,
  `duedate9` varchar(10) NOT NULL,
  `orgamt9` varchar(100) NOT NULL,
  `openbal9` varchar(100) NOT NULL,
  `payment9` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_payment`
--

INSERT INTO `app1_payment` (`paymentid`, `customer`, `email`, `findinvoice`, `paymdate`, `pmethod`, `refno`, `depto`, `amtreceived`, `descrip`, `duedate`, `orgamt`, `openbal`, `payment`, `amtapply`, `amtcredit`, `descrip1`, `duedate1`, `orgamt1`, `openbal1`, `payment1`, `descrip2`, `duedate2`, `orgamt2`, `openbal2`, `payment2`, `descrip3`, `duedate3`, `orgamt3`, `openbal3`, `payment3`, `descrip4`, `duedate4`, `orgamt4`, `openbal4`, `payment4`, `descrip5`, `duedate5`, `orgamt5`, `openbal5`, `payment5`, `descrip6`, `duedate6`, `orgamt6`, `openbal6`, `payment6`, `descrip7`, `duedate7`, `orgamt7`, `openbal7`, `payment7`, `descrip8`, `duedate8`, `orgamt8`, `openbal8`, `payment8`, `descrip9`, `duedate9`, `orgamt9`, `openbal9`, `payment9`, `cid_id`) VALUES
(3, 'SAD', 'SADSA', NULL, '2022-08-13', 'Cash', '1003', '', '', '', '', '', '', '5000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(4, 'xcv', 'xcvcx', 'xcvc', '2022-08-14', 'Cash', '1004', '', '', '', '', '', '', '1200', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(5, 'sad', 'sad', 'sads', '2022-08-16', 'Cash', '1005', '', '', '', '', '', '', '1400', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(7, 'dsfd', 'sdfds', 'sdfd', '2022-1-08-17', 'Cash', '1006', '', '', '', '', '', '', '1568', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 6),
(8, 'ASA ASASAS', 'dsffd@gmail.com', '12', '2022-09-26', 'Credit Card', '1015.0', 'Inventory', '100', '0 2022-09-23', '2022-09-16', '0', '200', '100', '100.0', '20', '0 2022-09-23', '2022-09-16', '0', '', '', '100.0', '20', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(9, 'ASA ASASAS', 'dfdsf', '12', '2022-09-26', 'Cheque', '1008.0', 'Inventory', '20', '0 2022-09-23', '2022-09-16', '0', '100.0', '20', '20.0', '10', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(10, 'ram kum', 'fdg@gmail.com', '17', '2022-09-26', 'Cash', '1015.0', 'Inventory', '200', '0 2022-09-26', '2022-10-11', '1004', '1004.0', '200', '200.0', '200', '0 2022-09-26', '2022-10-11', '1004', '', '', '804.0', '100', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(11, 'ram kum', 'fdg@gmail.com', '17', '2022-09-27', '', '1010.0', 'Inventory', '100', '0 2022-09-26', '2022-10-11', '1004', '804.0', '100', '100.0', '0.0', '0 2022-09-26', '2022-10-26', '9356', '9356.0', '0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(12, 'fdgfdgdg fdgfdg', 'dfgdgdfg@gmail.com', '20', '2022-09-27', 'Cheque', '1011.0', 'Inventory', '100', '0 2022-09-27', '2022-10-12', '3948', '3948.0', '100', '100.0', '100', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(13, 'dfs sdf', '', '21', '2022-09-30', 'Credit Card', '1015.0', 'Inventory', '200', 'sadsadsad', '2022-09-31', '39546', '3848.0', '0', '200.0', '0.0', 'undefined', 'undefined', 'undefined', '3848.0', '0', 'undefined', 'undefined', 'undefined', '1024.0', '0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(14, 'Amal  Neerath', '', '22', '2022-09-22', 'Credit Card', '1015.0', 'Inventory', '32', 'dgf', '2022-09-31', '3000', '', '', '32.0', '32', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(15, 'Amal Leenath', 'fdgfdgdf@gmail.com', '23', '2022-09-30', 'Cheque', '1016.0', 'Inventory', '100', '0 2022-09-28', '2022-10-28', '3032', '80.0', '80.0', '100.0', '80', '0 2022-09-30', '2022-11-29', '3968', '3968.0', '20.0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(16, 'ram kum', 'fdg@gmail.com', '17', '2022-09-30', '', '1017.0', 'Inventory', '100', '1005 2022-09-26', '2022-10-11', '1004', '1024.0', '100', '100.0', '100', '0 2022-09-30', '2022-10-30', '768', '768.0', '0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(17, 'ram kum', 'fdg@gmail.com', '1005', '2022-09-30', 'Credit Card', '1018.0', 'Inventory', '120', '1005 2022-09-26', '2022-10-11', '1004', '924.0', '120', '120.0', '23', '0 2022-09-30', '2022-10-30', '768', '768.0', '0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(18, 'ram kum', 'fdg@gmail.com', '1005', '2022-09-30', '', '1019.0', 'Inventory', '1212', '1005 2022-09-26', '2022-10-11', '1004', '804.0', '804.0', '1212.0', '122', '0 2022-09-30', '2022-10-30', '768', '768.0', '408.0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(19, 'ram kum', 'fdg@gmail.com', '1005', '2022-09-30', '', '1020.0', 'Inventory', '200', '1005 2022-09-26', '2022-10-11', '1004', '0.0', '0.0', '200.0', '100', '0 2022-09-30', '2022-10-30', '768', '360.0', '200.0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6),
(20, 'Amal  Neerath', '', '0', '2022-10-01', '', '1021.0', 'Inventory', '300', '0 2022-09-30', '2022-11-29', '3968', '160.0', '160.0', '160.0', '140.0', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 'undefined', 'undefined', 'undefined', '', '', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_payslip`
--

CREATE TABLE `app1_payslip` (
  `payslipid` int(11) NOT NULL,
  `empname` varchar(100) NOT NULL,
  `employeenumber` varchar(100) NOT NULL,
  `desig` varchar(100) NOT NULL,
  `fper` varchar(100) NOT NULL,
  `tper` varchar(100) NOT NULL,
  `paydate` varchar(100) NOT NULL,
  `basic` varchar(100) NOT NULL,
  `da` varchar(100) NOT NULL,
  `ear1` varchar(100) NOT NULL,
  `earr1` varchar(100) NOT NULL,
  `ear2` varchar(100) NOT NULL,
  `earr2` varchar(100) NOT NULL,
  `ear3` varchar(100) NOT NULL,
  `earr3` varchar(100) NOT NULL,
  `ear4` varchar(100) NOT NULL,
  `earr4` varchar(100) NOT NULL,
  `ear5` varchar(100) NOT NULL,
  `earr5` varchar(100) NOT NULL,
  `ear6` varchar(100) NOT NULL,
  `earr6` varchar(100) NOT NULL,
  `ear7` varchar(100) NOT NULL,
  `earr7` varchar(100) NOT NULL,
  `provi` varchar(100) NOT NULL,
  `prof` varchar(100) NOT NULL,
  `esi` varchar(100) NOT NULL,
  `ded1` varchar(100) NOT NULL,
  `dedu1` varchar(100) NOT NULL,
  `ded2` varchar(100) NOT NULL,
  `dedu2` varchar(100) NOT NULL,
  `ded3` varchar(100) NOT NULL,
  `dedu3` varchar(100) NOT NULL,
  `ded4` varchar(100) NOT NULL,
  `dedu4` varchar(100) NOT NULL,
  `ded5` varchar(100) NOT NULL,
  `dedu5` varchar(100) NOT NULL,
  `ded6` varchar(100) NOT NULL,
  `dedu6` varchar(100) NOT NULL,
  `gros` varchar(100) NOT NULL,
  `tded` varchar(100) NOT NULL,
  `netsal` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_production`
--

CREATE TABLE `app1_production` (
  `id` bigint(20) NOT NULL,
  `productname` varchar(255) NOT NULL,
  `sku` varchar(255) NOT NULL,
  `hsn` varchar(255) NOT NULL,
  `quantity` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `manufacturing_date` varchar(255) NOT NULL,
  `expiry_date` varchar(255) NOT NULL,
  `pname1` varchar(255) NOT NULL,
  `sku1` varchar(255) NOT NULL,
  `quantity1` varchar(255) NOT NULL,
  `rate1` varchar(255) NOT NULL,
  `amount1` varchar(255) NOT NULL,
  `pname2` varchar(255) NOT NULL,
  `sku2` varchar(255) NOT NULL,
  `quantity2` varchar(255) NOT NULL,
  `rate2` varchar(255) NOT NULL,
  `amount2` varchar(255) NOT NULL,
  `pname3` varchar(255) NOT NULL,
  `sku3` varchar(255) NOT NULL,
  `quantity3` varchar(255) NOT NULL,
  `rate3` varchar(255) NOT NULL,
  `amount3` varchar(255) NOT NULL,
  `pname4` varchar(255) NOT NULL,
  `sku4` varchar(255) NOT NULL,
  `quantity4` varchar(255) NOT NULL,
  `rate4` varchar(255) NOT NULL,
  `amount4` varchar(255) NOT NULL,
  `pname5` varchar(255) NOT NULL,
  `sku5` varchar(255) NOT NULL,
  `quantity5` varchar(255) NOT NULL,
  `rate5` varchar(255) NOT NULL,
  `amount5` varchar(255) NOT NULL,
  `pname6` varchar(255) NOT NULL,
  `sku6` varchar(255) NOT NULL,
  `quantity6` varchar(255) NOT NULL,
  `rate6` varchar(255) NOT NULL,
  `amount6` varchar(255) NOT NULL,
  `pname7` varchar(255) NOT NULL,
  `sku7` varchar(255) NOT NULL,
  `quantity7` varchar(255) NOT NULL,
  `rate7` varchar(255) NOT NULL,
  `amount7` varchar(255) NOT NULL,
  `pname8` varchar(255) NOT NULL,
  `sku8` varchar(255) NOT NULL,
  `quantity8` varchar(255) NOT NULL,
  `rate8` varchar(255) NOT NULL,
  `amount8` varchar(255) NOT NULL,
  `pname9` varchar(255) NOT NULL,
  `sku9` varchar(255) NOT NULL,
  `quantity9` varchar(255) NOT NULL,
  `rate9` varchar(255) NOT NULL,
  `amount9` varchar(255) NOT NULL,
  `pname10` varchar(255) NOT NULL,
  `sku10` varchar(255) NOT NULL,
  `quantity10` varchar(255) NOT NULL,
  `rate10` varchar(255) NOT NULL,
  `amount10` varchar(255) NOT NULL,
  `pname11` text NOT NULL,
  `sku11` text NOT NULL,
  `quantity11` text NOT NULL,
  `rate11` text NOT NULL,
  `amount11` text NOT NULL,
  `pname12` text NOT NULL,
  `sku12` text NOT NULL,
  `quantity12` text NOT NULL,
  `rate12` text NOT NULL,
  `amount12` text NOT NULL,
  `pname13` text NOT NULL,
  `sku13` text NOT NULL,
  `quantity13` text NOT NULL,
  `rate13` text NOT NULL,
  `amount13` text NOT NULL,
  `pname14` text NOT NULL,
  `sku14` text NOT NULL,
  `quantity14` text NOT NULL,
  `rate14` text NOT NULL,
  `amount14` text NOT NULL,
  `pname15` text NOT NULL,
  `sku15` text NOT NULL,
  `quantity15` text NOT NULL,
  `rate15` text NOT NULL,
  `amount15` text NOT NULL,
  `co_pname1` text NOT NULL,
  `co_sku1` text NOT NULL,
  `co_qty1` text NOT NULL,
  `co_rate1` text NOT NULL,
  `co_amount1` text NOT NULL,
  `co_pname2` text NOT NULL,
  `co_sku2` text NOT NULL,
  `co_qty2` text NOT NULL,
  `co_rate2` text NOT NULL,
  `co_amount2` text NOT NULL,
  `co_pname3` text NOT NULL,
  `co_sku3` text NOT NULL,
  `co_qty3` text NOT NULL,
  `co_rate3` text NOT NULL,
  `co_amount3` text NOT NULL,
  `co_pname4` text NOT NULL,
  `co_sku4` text NOT NULL,
  `co_qty4` text NOT NULL,
  `co_rate4` text NOT NULL,
  `co_amount4` text NOT NULL,
  `co_pname5` text NOT NULL,
  `co_sku5` text NOT NULL,
  `co_qty5` text NOT NULL,
  `co_rate5` text NOT NULL,
  `co_amount5` text NOT NULL,
  `co_pname6` text NOT NULL,
  `co_sku6` text NOT NULL,
  `co_qty6` text NOT NULL,
  `co_rate6` text NOT NULL,
  `co_amount6` text NOT NULL,
  `co_pname7` text NOT NULL,
  `co_sku7` text NOT NULL,
  `co_qty7` text NOT NULL,
  `co_rate7` text NOT NULL,
  `co_amount7` text NOT NULL,
  `co_pname8` text NOT NULL,
  `co_sku8` text NOT NULL,
  `co_qty8` text NOT NULL,
  `co_rate8` text NOT NULL,
  `co_amount8` text NOT NULL,
  `co_pname9` text NOT NULL,
  `co_sku9` text NOT NULL,
  `co_qty9` text NOT NULL,
  `co_rate9` text NOT NULL,
  `co_amount9` text NOT NULL,
  `co_pname10` text NOT NULL,
  `co_sku10` text NOT NULL,
  `co_qty10` text NOT NULL,
  `co_rate10` text NOT NULL,
  `co_amount10` text NOT NULL,
  `co_pname11` text NOT NULL,
  `co_sku11` text NOT NULL,
  `co_qty11` text NOT NULL,
  `co_rate11` text NOT NULL,
  `co_amount11` text NOT NULL,
  `co_pname12` text NOT NULL,
  `co_sku12` text NOT NULL,
  `co_qty12` text NOT NULL,
  `co_rate12` text NOT NULL,
  `co_amount12` text NOT NULL,
  `co_pname13` text NOT NULL,
  `co_sku13` text NOT NULL,
  `co_qty13` text NOT NULL,
  `co_rate13` text NOT NULL,
  `co_amount13` text NOT NULL,
  `co_pname14` text NOT NULL,
  `co_sku14` text NOT NULL,
  `co_qty14` text NOT NULL,
  `co_rate14` text NOT NULL,
  `co_amount14` text NOT NULL,
  `co_pname15` text NOT NULL,
  `co_sku15` text NOT NULL,
  `co_qty15` text NOT NULL,
  `co_rate15` text NOT NULL,
  `co_amount15` text NOT NULL,
  `wg_adi_cost1` text NOT NULL,
  `wg_perc1` text NOT NULL,
  `wg_amount1` text NOT NULL,
  `wg_adi_cost2` text NOT NULL,
  `wg_perc2` text NOT NULL,
  `wg_amount2` text NOT NULL,
  `wg_adi_cost3` text NOT NULL,
  `wg_perc3` text NOT NULL,
  `wg_amount3` text NOT NULL,
  `wg_adi_cost4` text NOT NULL,
  `wg_perc4` text NOT NULL,
  `wg_amount4` text NOT NULL,
  `wg_adi_cost5` text NOT NULL,
  `wg_perc5` text NOT NULL,
  `wg_amount5` text NOT NULL,
  `tot_add_cost` text NOT NULL,
  `eff_cost` text NOT NULL,
  `tt_qty` varchar(255) NOT NULL,
  `tt_tot` varchar(255) NOT NULL,
  `co_tt_qty` varchar(255) NOT NULL,
  `co_tt_tot` varchar(255) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_production`
--

INSERT INTO `app1_production` (`id`, `productname`, `sku`, `hsn`, `quantity`, `price`, `manufacturing_date`, `expiry_date`, `pname1`, `sku1`, `quantity1`, `rate1`, `amount1`, `pname2`, `sku2`, `quantity2`, `rate2`, `amount2`, `pname3`, `sku3`, `quantity3`, `rate3`, `amount3`, `pname4`, `sku4`, `quantity4`, `rate4`, `amount4`, `pname5`, `sku5`, `quantity5`, `rate5`, `amount5`, `pname6`, `sku6`, `quantity6`, `rate6`, `amount6`, `pname7`, `sku7`, `quantity7`, `rate7`, `amount7`, `pname8`, `sku8`, `quantity8`, `rate8`, `amount8`, `pname9`, `sku9`, `quantity9`, `rate9`, `amount9`, `pname10`, `sku10`, `quantity10`, `rate10`, `amount10`, `pname11`, `sku11`, `quantity11`, `rate11`, `amount11`, `pname12`, `sku12`, `quantity12`, `rate12`, `amount12`, `pname13`, `sku13`, `quantity13`, `rate13`, `amount13`, `pname14`, `sku14`, `quantity14`, `rate14`, `amount14`, `pname15`, `sku15`, `quantity15`, `rate15`, `amount15`, `co_pname1`, `co_sku1`, `co_qty1`, `co_rate1`, `co_amount1`, `co_pname2`, `co_sku2`, `co_qty2`, `co_rate2`, `co_amount2`, `co_pname3`, `co_sku3`, `co_qty3`, `co_rate3`, `co_amount3`, `co_pname4`, `co_sku4`, `co_qty4`, `co_rate4`, `co_amount4`, `co_pname5`, `co_sku5`, `co_qty5`, `co_rate5`, `co_amount5`, `co_pname6`, `co_sku6`, `co_qty6`, `co_rate6`, `co_amount6`, `co_pname7`, `co_sku7`, `co_qty7`, `co_rate7`, `co_amount7`, `co_pname8`, `co_sku8`, `co_qty8`, `co_rate8`, `co_amount8`, `co_pname9`, `co_sku9`, `co_qty9`, `co_rate9`, `co_amount9`, `co_pname10`, `co_sku10`, `co_qty10`, `co_rate10`, `co_amount10`, `co_pname11`, `co_sku11`, `co_qty11`, `co_rate11`, `co_amount11`, `co_pname12`, `co_sku12`, `co_qty12`, `co_rate12`, `co_amount12`, `co_pname13`, `co_sku13`, `co_qty13`, `co_rate13`, `co_amount13`, `co_pname14`, `co_sku14`, `co_qty14`, `co_rate14`, `co_amount14`, `co_pname15`, `co_sku15`, `co_qty15`, `co_rate15`, `co_amount15`, `wg_adi_cost1`, `wg_perc1`, `wg_amount1`, `wg_adi_cost2`, `wg_perc2`, `wg_amount2`, `wg_adi_cost3`, `wg_perc3`, `wg_amount3`, `wg_adi_cost4`, `wg_perc4`, `wg_amount4`, `wg_adi_cost5`, `wg_perc5`, `wg_amount5`, `tot_add_cost`, `eff_cost`, `tt_qty`, `tt_tot`, `co_tt_qty`, `co_tt_tot`, `cid_id`) VALUES
(24, 'dfgfh', '125', '258', '2', '$3622.5', '2022-09-03', '2022-09-03', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'dfds', '1', '63.0', 'vc', '2', '126.0', 'cxv', '3', '189.0', 'cvx', '4', '252.0', 'cvxd', '5', '315.0', '$945.0', '$7245.0', '', '', '', '', 6),
(27, 'hp brand', '1254', '54455', '2', '$4158.0', '2022-09-03', '2022-09-03', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'wd', '2', '132.0', 'sda', '1', '66.0', 'zxc', '6', '396.0', 'zx', '8', '528.0', 'vcb', '9', '594.0', '$1716.0', '$8316.0', '', '', '', '', 6),
(28, 'ph', '455', '455', '5', '$1263.6', '2022-09-03', '2022-09-03', 'laptop', '154', '2', '$500.0', '1000.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '200.0', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'mi mobile', '1235', '1', '$200.0', '200.0', 'laptop', '154', '1', '$500.0', '500.0', 'fd', '2', '98.0', 'fdgf', '3', '147.0', 'zx', '4', '196.0', 'zx', '5', '245.0', 'z', '6', '294.0', '$1418.0', '$6318.0', '2', '$1000.0', '15', '$3900.0', 6),
(31, 'phs', '1245', '5858', '5', '$96.0', '2022-09-05', '2022-09-05', 'mi mobile', '1235', '1', '$200.0', '200.0', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', 'mi mobile', '1235', '1', '$200.0', '200.0', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', '', '', '1', '', '', 'dfs', '2', '8.0', 'dsf', '3', '12.0', 'dsf', '4', '16.0', 'dsf', '5', '20.0', 'ds', '6', '24.0', '$80.0', '$480.0', '1', '$200.0', '1', '$200.0', 6),
(32, 'bnhj', '1254', '6578', '5', '$181.6', '2022-09-05', '2022-09-05', 'mi mobile', '1235', '1', '$200.0', '200.0', 'vivo y11', '15478', '0', '$$1200', '', 'laptop', '154', '1', '$$500', '500.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'mi mobile', '1235', '1', '$200.0', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'vcbvb', '2', '18.0', '', '', '0.0', '', '', '0.0', '', '', '0.0', '', '', '0.0', '$8.0', '$908.0', '2', '$700.0', '1', '$200.0', 6),
(34, 'dsfd', '12456', '555', '2', '$204.0', '2022-09-05', '2022-09-05', 'mi mobile', '1235', '1', '$200.0', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'mi mobile', '1235', '1', '$200.0', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'fdgfd', '2', '8.0', '', '', '', '', '', '', '', '', '', '', '', '', '$8.0', '$408.0', '1', '$200.0', '1', '$200.0', 6),
(35, 'sdf', '1457', '888', '5', '$81.6', '2022-09-05', '2022-09-05', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'sdfd', '2', '8.0', '', '', '', '', '', '', '', '', '', '', '', '', '$8.0', '$408.0', '1', '$200.0', '1', '$200.0', 6),
(38, 'sdfd', 'dsfd', 'dsfds', '2', '$206.0', '2022-09-05', '2022-09-05', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'ghfg', '3', '12.0', '', '', '', '', '', '', '', '', '', '', '', '', '$12.0', '$412.0', '1', '$200.0', '1', '$200.0', 6),
(39, 'Asus', '121619', '2587', '2', '$212.0', '2022-09-06', '2022-09-06', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'wgty', '6', '24.0', '', '', '', '', '', '', '', '', '', '', '', '', '$24.0', '$424.0', '1', '$200.0', '1', '$200.0', 6),
(40, 'zeb', '12456', '2', '2', '$559.0', '2022-09-01', '2022-09-06', 'mi mobile', '1235', '1', '$200', '200.0', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'laptop', '154', '1', '$500', '500.0', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'wg', '2', '22.0', '', '', '0.0', '', '', '0.0', '', '', '0.0', '', '', '0.0', '$18.0', '$1118.0', '2', '$400.0', '2', '$700.0', 6),
(41, 'rens', 'as2154', 'N42015', '3', '$247.33333333333334', '2022-09-23', '2022-09-23', 'mi mobile', '1235', '1', '$200', '200.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'laptop', '154', '1', '$500', '500.0', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'wages', '6', '42.0', '', '', '', '', '', '', '', '', '', '', '', '', '$42.0', '$742.0', '1', '$200.0', '1', '$500.0', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_recon1`
--

CREATE TABLE `app1_recon1` (
  `recon1id` int(11) NOT NULL,
  `accounttype` varchar(100) NOT NULL,
  `beginningbalance` varchar(100) NOT NULL,
  `endingbalance` varchar(100) NOT NULL,
  `endingdate` varchar(100) NOT NULL,
  `edat` varchar(100) DEFAULT NULL,
  `serchar` varchar(100) NOT NULL,
  `expacc` varchar(100) NOT NULL,
  `idat1` varchar(100) DEFAULT NULL,
  `intear` varchar(100) NOT NULL,
  `incacc` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_recordpay`
--

CREATE TABLE `app1_recordpay` (
  `recordpayid` int(11) NOT NULL,
  `textname` varchar(100) NOT NULL,
  `paymentdate` varchar(100) NOT NULL,
  `recordamount` varchar(100) NOT NULL,
  `recordmemo` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_salesrecpts`
--

CREATE TABLE `app1_salesrecpts` (
  `salesrecptsid` int(11) NOT NULL,
  `salename` varchar(100) NOT NULL,
  `saleemail` varchar(254) NOT NULL,
  `saleaddress` varchar(150) NOT NULL,
  `saledate` varchar(10) NOT NULL,
  `saleno` varchar(20) NOT NULL,
  `salesplace` varchar(100) NOT NULL,
  `salepay` varchar(10) NOT NULL,
  `salerefno` varchar(10) NOT NULL,
  `saledeposit` varchar(150) NOT NULL,
  `salepro` varchar(100) NOT NULL,
  `salehsn` varchar(100) NOT NULL,
  `saledescription` varchar(100) NOT NULL,
  `saleqty` varchar(100) NOT NULL,
  `saleprice` varchar(100) NOT NULL,
  `saaletotal` varchar(100) NOT NULL,
  `salesubtotal` varchar(100) NOT NULL,
  `tax` int(11) DEFAULT NULL,
  `saletaxamount` varchar(100) NOT NULL,
  `salegrandtotal` varchar(100) NOT NULL,
  `category2` varchar(100) NOT NULL,
  `categoryhsn2` varchar(100) NOT NULL,
  `descrptin2` varchar(100) NOT NULL,
  `catqty2` varchar(100) NOT NULL,
  `catprice2` varchar(100) NOT NULL,
  `cattotal2` varchar(100) NOT NULL,
  `tax1` int(11) DEFAULT NULL,
  `category3` varchar(100) NOT NULL,
  `categoryhsn3` varchar(100) NOT NULL,
  `descrptin3` varchar(100) NOT NULL,
  `catqty3` varchar(100) NOT NULL,
  `catprice3` varchar(100) NOT NULL,
  `cattotal3` varchar(100) NOT NULL,
  `tax2` int(11) DEFAULT NULL,
  `category4` varchar(100) NOT NULL,
  `categoryhsn4` varchar(100) NOT NULL,
  `descrptin4` varchar(100) NOT NULL,
  `catqty4` varchar(100) NOT NULL,
  `catprice4` varchar(100) NOT NULL,
  `cattotal4` varchar(100) NOT NULL,
  `tax3` int(11) DEFAULT NULL,
  `offline` varchar(100) DEFAULT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_salesrecpts`
--

INSERT INTO `app1_salesrecpts` (`salesrecptsid`, `salename`, `saleemail`, `saleaddress`, `saledate`, `saleno`, `salesplace`, `salepay`, `salerefno`, `saledeposit`, `salepro`, `salehsn`, `saledescription`, `saleqty`, `saleprice`, `saaletotal`, `salesubtotal`, `tax`, `saletaxamount`, `salegrandtotal`, `category2`, `categoryhsn2`, `descrptin2`, `catqty2`, `catprice2`, `cattotal2`, `tax1`, `category3`, `categoryhsn3`, `descrptin3`, `catqty3`, `catprice3`, `cattotal3`, `tax2`, `category4`, `categoryhsn4`, `descrptin4`, `catqty4`, `catprice4`, `cattotal4`, `tax3`, `offline`, `cid_id`) VALUES
(1, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1001', 'Kerala', 'Cheque', '17', 'Inventory', 'pen', '2154', '', '2', '2500', '5000.0', '7500.0', 2, '150.0', '7650.0', 'pen', '2154', '', '2', '2500', '2500.0', 2, '', '', '', '0', '', '0', 0, '', '', '', '0', '', '0', 0, NULL, 6),
(3, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1003', 'Kerala', 'Cash', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(4, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1004', 'Kerala', 'Cheque', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(5, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1005', 'Kerala', 'Cheque', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(6, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1006', 'Kerala', 'Cheque', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(7, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-27', '1007', 'Kerala', 'Cheque', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(8, 'fdgfdgdg fdgfdg', 'dfgdgdfg@gmail.com', 'fdgfdgdg fdgfdg\nfdgg\nasda\nasdas\nsdad\nasdsd\nsdsdd', '2022-09-27', '1008', 'Kerala', 'Cash', '20', 'Inventory', 'pen', '2154', '', '1', '2500.0', '2500', '3100', 28, '848', '3948', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(9, 'fdgfdgdg fdgfdg', 'dfgdgdfg@gmail.com', 'fdgfdgdg fdgfdg\nfdgg\nasda\nasdas\nsdad\nasdsd\nsdsdd', '2022-09-27', '1009', 'Kerala', 'Cheque', '20', 'Inventory', 'pen', '2154', '', '1', '2500.0', '2500', '3100', 28, '848', '3948', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(10, 'Amal  Neerath', 'fdgfdgdf@gmail.com', 'Amal Leenath\namals\nasddsa\ndasdsd\nsda\ndsad\ndsadads', '2022-09-30', '1010', 'Kerala', 'Credit Car', '23', 'Inventory', 'pen', '2154', '', '1', '2500.0', '2500', '3100', 28, '868', '3968', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6),
(11, 'ram kum', 'fdg@gmail.com', 'ram kum\nsdsad\nsdfd\nsdfsd\nfdf\ndf\nfdfdf', '2022-09-30', '1011', 'Kerala', 'Cheque', '17', 'Inventory', 'Mouse', 'fdg2154', '', '1', '200.0', '200', '800', 28, '204', '1004', 'Mouse', 'fdg2154', '', '1', '200.0', '200', 18, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, 'Mouse', 'fdg2154', '', '1', '200.0', '200', 28, NULL, 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_service`
--

CREATE TABLE `app1_service` (
  `serviceid` int(11) NOT NULL,
  `img` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `sku` varchar(100) NOT NULL,
  `sac` varchar(100) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `categ` varchar(100) NOT NULL,
  `descr` varchar(100) NOT NULL,
  `saleprice` varchar(100) NOT NULL,
  `income` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `abatement` varchar(100) NOT NULL,
  `sertype` varchar(100) NOT NULL,
  `purchasedescr` varchar(100) NOT NULL,
  `cost` varchar(100) NOT NULL,
  `expenseaccount` varchar(100) NOT NULL,
  `purchasetax` varchar(100) NOT NULL,
  `revcharge` varchar(100) NOT NULL,
  `presupplier` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_sign`
--

CREATE TABLE `app1_sign` (
  `sid` int(11) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `conformpassword` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app1_suplrcredit`
--

CREATE TABLE `app1_suplrcredit` (
  `suppliercreditid` int(11) NOT NULL,
  `supplier` varchar(100) NOT NULL,
  `mailaddr` varchar(100) NOT NULL,
  `paymdate` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `ccatego` varchar(100) NOT NULL,
  `cdescrip` varchar(100) NOT NULL,
  `cqty` varchar(100) NOT NULL,
  `cprice` varchar(100) NOT NULL,
  `ctotal` varchar(100) NOT NULL,
  `ccatego2` varchar(100) NOT NULL,
  `cdescrip2` varchar(100) NOT NULL,
  `cqty2` varchar(100) NOT NULL,
  `cprice2` varchar(100) NOT NULL,
  `ctotal2` varchar(100) NOT NULL,
  `ccatego3` varchar(100) NOT NULL,
  `cdescrip3` varchar(100) NOT NULL,
  `cqty3` varchar(100) NOT NULL,
  `cprice3` varchar(100) NOT NULL,
  `ctotal3` varchar(100) NOT NULL,
  `ccatego4` varchar(100) NOT NULL,
  `cdescrip4` varchar(100) NOT NULL,
  `cqty4` varchar(100) NOT NULL,
  `cprice4` varchar(100) NOT NULL,
  `ctotal4` varchar(100) NOT NULL,
  `product` varchar(100) NOT NULL,
  `hsn` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `qty` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `product2` varchar(100) NOT NULL,
  `hsn2` varchar(100) NOT NULL,
  `description2` varchar(100) NOT NULL,
  `qty2` varchar(100) NOT NULL,
  `price2` varchar(100) NOT NULL,
  `total2` varchar(100) NOT NULL,
  `product3` varchar(100) NOT NULL,
  `hsn3` varchar(100) NOT NULL,
  `description3` varchar(100) NOT NULL,
  `qty3` varchar(100) NOT NULL,
  `price3` varchar(100) NOT NULL,
  `total3` varchar(100) NOT NULL,
  `product4` varchar(100) NOT NULL,
  `hsn4` varchar(100) NOT NULL,
  `description4` varchar(100) NOT NULL,
  `qty4` varchar(100) NOT NULL,
  `price4` varchar(100) NOT NULL,
  `total4` varchar(100) NOT NULL,
  `subtotal` varchar(100) NOT NULL,
  `tax` varchar(100) NOT NULL,
  `tax2` varchar(100) NOT NULL,
  `tax3` varchar(100) NOT NULL,
  `tax4` varchar(100) NOT NULL,
  `taxamount` varchar(100) NOT NULL,
  `grandtotal` varchar(100) NOT NULL,
  `creditamount` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_suplrcredit`
--

INSERT INTO `app1_suplrcredit` (`suppliercreditid`, `supplier`, `mailaddr`, `paymdate`, `refno`, `ccatego`, `cdescrip`, `cqty`, `cprice`, `ctotal`, `ccatego2`, `cdescrip2`, `cqty2`, `cprice2`, `ctotal2`, `ccatego3`, `cdescrip3`, `cqty3`, `cprice3`, `ctotal3`, `ccatego4`, `cdescrip4`, `cqty4`, `cprice4`, `ctotal4`, `product`, `hsn`, `description`, `qty`, `price`, `total`, `product2`, `hsn2`, `description2`, `qty2`, `price2`, `total2`, `product3`, `hsn3`, `description3`, `qty3`, `price3`, `total3`, `product4`, `hsn4`, `description4`, `qty4`, `price4`, `total4`, `subtotal`, `tax`, `tax2`, `tax3`, `tax4`, `taxamount`, `grandtotal`, `creditamount`, `cid_id`) VALUES
(1, 'ASA ASASAS', 'dfdsfsf\n\n\n', '2022-09-19', '', 'ZzxzZx', 'fdg', '3', '500', '1500', 'Billable Expense Income', 'gfd', '1', '200', '200', 'Billable Expense Income', 'dfgd', '1', '200', '200', 'Billable Expense Income', 'fdgfdgf', '3', '700', '2100', 'Mouse', 'fdg2154', 'sdfsdf\n\n\n', '1', '100', '200.0', 'key', '1221', '1fggfdf\n\n\n', '1', '100', '100.0', 'Mouse', 'fdg2154', 'cxvcv\n\n\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'cv\n\n\n', '1', '100', '200.0', '4700.0', '28.0% GST(28%)', '18.0% GST(18%)', '12.0% GST(12%)', '18.0% GST(18%)', '152.0', '4852.0', '', 6),
(2, 'zxcxz xzcxzcz', 'sdfsdfsfd\n', '2022-09-07', '', 'lkl', 'fgd', '1', '50', '50', 'Billable Expense Income', 'fgdf', '1', '50', '50', 'Billable Expense Income', 'fdg', '1', '20', '20', 'Billable Expense Income', 'fgdfd', '1', '20', '20', 'Mouse', 'fdg2154', 'dsfd\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'sdfsd\n', '200.0', '1', '200.0', 'Mouse', 'fdg2154', 'fd\n', '200.0', '1', '200.0', 'Mouse', 'fdg2154', 'sad\n', '200.0', '1', '200.0', '940.0', '28.0% GST(28%)', '28.0% GST(28%)', '28.0% GST(28%)', '28.0% GST(28%)', '224.0', '1164.0', '', 6),
(3, 'ASA ASASAS', 'dfdsfsf\n\n\n', '2022-09-19', '', 'ZzxzZx', 'fdg', '3', '500', '1500', 'Billable Expense Income', 'gfd', '1', '200', '200', 'Billable Expense Income', 'dfgd', '1', '200', '200', 'Billable Expense Income', 'fdgfdgf', '3', '700', '2100', 'Mouse', 'fdg2154', 'sdfsdf\n\n\n', '1', '100', '200.0', 'key', '1221', '1fggfdf\n\n\n', '1', '100', '100.0', 'Mouse', 'fdg2154', 'cxvcv\n\n\n', '1', '100', '200.0', 'Mouse', 'fdg2154', 'cv\n\n\n', '1', '100', '200.0', '4700.0', '28.0% GST(28%)', '18.0% GST(18%)', '12.0% GST(12%)', '18.0% GST(18%)', '152.0', '4852.0', '', 6),
(4, 'karun dfdsfsd', 'karundfdsfsd\nasd\n8848937577\n\n\n\n\n\nAfghanistan\n', '2022-09-21', '', 'Uncategorised Income', 'sfd', '1', '100', '100', 'Sales', 'sdfd', '1', '200', '200', 'Consulting Income', 'sdfsd', '1', '300', '300', 'Sales-Hardware', 'fdfsdf', '1', '400', '400', 'Mouse', 'fdg2154', 'asdsa\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdas\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n', '0', '200.0', '0.0', '1600.0', '28.0% GST(28%)', '18.0% GST(18%)', '28.0% GST(28%)', '28.0% GST(28%)', '204.0', '1804.0', '', 6),
(5, 'karun dfdsfsd', 'karundfdsfsd\nasd\n8848937577\n\n\n\n\n\nAfghanistan\n', '2022-09-21', '', 'Uncategorised Income', 'sfd', '1', '100', '100', 'Sales', 'sdfd', '1', '200', '200', 'Consulting Income', 'sdfsd', '1', '300', '300', 'Sales-Hardware', 'fdfsdf', '1', '400', '400', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdas\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'asdsa\n\n\n', '1', '200.0', '200.0', '1800.0', '28.0% GST(28%)', '18.0% GST(18%)', '28.0% GST(28%)', '28.0% GST(28%)', '204.0', '1804.0', '', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_supplier`
--

CREATE TABLE `app1_supplier` (
  `supplierid` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `website` varchar(100) NOT NULL,
  `billingrate` varchar(100) NOT NULL,
  `terms` varchar(100) NOT NULL,
  `addterms` varchar(100) NOT NULL,
  `openingbalance` varchar(100) NOT NULL,
  `accountno` varchar(100) NOT NULL,
  `gsttype` varchar(100) NOT NULL,
  `gstin` varchar(100) NOT NULL,
  `taxregistrationno` varchar(100) NOT NULL,
  `effectivedate` varchar(100) NOT NULL,
  `defaultexpenceaccount` varchar(100) NOT NULL,
  `tds` varchar(200) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `notes` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_supplier`
--

INSERT INTO `app1_supplier` (`supplierid`, `title`, `firstname`, `lastname`, `company`, `mobile`, `email`, `website`, `billingrate`, `terms`, `addterms`, `openingbalance`, `accountno`, `gsttype`, `gstin`, `taxregistrationno`, `effectivedate`, `defaultexpenceaccount`, `tds`, `street`, `city`, `state`, `pincode`, `country`, `notes`, `cid_id`) VALUES
(3, 'Mr', 'hgjhgjhg', 'dsdfs', 'Vamans', 'fdfsf', 'dsfd', 'dfsf', 'dfdfdf', ' Due on Receipt', 'sdfsf', '1000', 'dfdf', 'GST registered- Regular', '124587', '215487', '2022-08-22', 'Business Licenses and Permits', 'Yes', 'zxcxz\n', 'xcxcxc', 'xcxcz', 'zxczxcxc', 'Anguilla', 'zxcxzcc\n', 6),
(5, 'Mr', 'karun', 'dfdsfsd', 'asd', '8848937577', 'sadasd@gmail.com', '', '1', 'NET15', 'fdg', '1000', '', 'Choose...', '', '', '2022-09-22', 'Choose Account', 'Choose', '\n', '', '', '', 'Afghanistan', '\n', 6),
(6, 'Mr', 'dsfd', 'dsfds', 'dsfds', '8848935788', 'fdfdfsd@gmail.com', '', '1', 'NET15', '', '1000', 'fdgfdgfdg', 'GST registered- Composition', 'fdgfdg', 'dfgfdg', '2022-09-20', 'Advertising /Promotional', 'Yes', 'dfgfd\n', 'gfdgfdg', 'dfgf', 'gfdgfd', 'Afghanistan', 'dfgdgd\n', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_timeact`
--

CREATE TABLE `app1_timeact` (
  `timeactid` int(11) NOT NULL,
  `timdate` varchar(10) NOT NULL,
  `timename` varchar(20) NOT NULL,
  `timecust` varchar(20) NOT NULL,
  `timecheck` varchar(10) NOT NULL,
  `timebill` varchar(20) NOT NULL,
  `timecheckk` varchar(10) NOT NULL,
  `timestart` varchar(6) NOT NULL,
  `timeend` varchar(6) NOT NULL,
  `tyme` varchar(6) NOT NULL,
  `timedes` varchar(50) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_timeact`
--

INSERT INTO `app1_timeact` (`timeactid`, `timdate`, `timename`, `timecust`, `timecheck`, `timebill`, `timecheckk`, `timestart`, `timeend`, `tyme`, `timedes`, `cid_id`) VALUES
(1, '2022-09-17', 'Ram Charn', 'fdgg', 'Yes', '0', 'Yes', '12.03', '1204', '12.25', 'dfgfgfd\n\n\n', 6),
(2, '2022-09-17', 'Ram Charn', 'fdgg', 'Yes', '0', 'Yes', '12.03', '1204', '12.25', 'dfgfgfd\n\n\n', 6),
(3, '2022-09-14', 'anbmuds', 'sdfds', 'Yes', '1', 'Yes', '12.02', '12.06', '12.22', 'ewrerewrew\n', 6),
(4, '2022-09-23', 'Ajas', 'fdgg', 'Yes', '120', 'Yes', '12.00', '2.00', '14:00', 'tretr\n', 6);

-- --------------------------------------------------------

--
-- Table structure for table `app1_timeactsale`
--

CREATE TABLE `app1_timeactsale` (
  `timeactsaleid` int(11) NOT NULL,
  `timdatesale` varchar(10) NOT NULL,
  `timenamesale` varchar(20) NOT NULL,
  `timecustsale` varchar(20) NOT NULL,
  `timechecksale` varchar(10) NOT NULL,
  `timebillsale` varchar(20) NOT NULL,
  `timecheckksale` varchar(10) NOT NULL,
  `timestartsale` varchar(6) NOT NULL,
  `timeendsale` varchar(6) NOT NULL,
  `tymesale` varchar(6) NOT NULL,
  `timedessale` varchar(50) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_timeactsale`
--

INSERT INTO `app1_timeactsale` (`timeactsaleid`, `timdatesale`, `timenamesale`, `timecustsale`, `timechecksale`, `timebillsale`, `timecheckksale`, `timestartsale`, `timeendsale`, `tymesale`, `timedessale`, `cid_id`) VALUES
(2, '2022-09-27', 'hgjhgjhg dsdfs', 'ASDSD DSSDS', 'Yes', '1', 'Yes', '01:03', '01:01', '00:00', 'ddffg', 6),
(3, '2022-09-30', 'karun dfdsfsd', 'ram kum', 'Yes', 'sdfsgsfd', 'Yes', '01:01', '01:01', '02:02', 'sadsafdgsah', 6);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add accountype', 7, 'add_accountype'),
(26, 'Can change accountype', 7, 'change_accountype'),
(27, 'Can delete accountype', 7, 'delete_accountype'),
(28, 'Can view accountype', 7, 'view_accountype'),
(29, 'Can add addac', 8, 'add_addac'),
(30, 'Can change addac', 8, 'change_addac'),
(31, 'Can delete addac', 8, 'delete_addac'),
(32, 'Can view addac', 8, 'view_addac'),
(33, 'Can add company', 9, 'add_company'),
(34, 'Can change company', 9, 'change_company'),
(35, 'Can delete company', 9, 'delete_company'),
(36, 'Can view company', 9, 'view_company'),
(37, 'Can add expenseaccount', 10, 'add_expenseaccount'),
(38, 'Can change expenseaccount', 10, 'change_expenseaccount'),
(39, 'Can delete expenseaccount', 10, 'delete_expenseaccount'),
(40, 'Can view expenseaccount', 10, 'view_expenseaccount'),
(41, 'Can add item model', 11, 'add_itemmodel'),
(42, 'Can change item model', 11, 'change_itemmodel'),
(43, 'Can delete item model', 11, 'delete_itemmodel'),
(44, 'Can view item model', 11, 'view_itemmodel'),
(45, 'Can add product model', 12, 'add_productmodel'),
(46, 'Can change product model', 12, 'change_productmodel'),
(47, 'Can delete product model', 12, 'delete_productmodel'),
(48, 'Can view product model', 12, 'view_productmodel'),
(49, 'Can add sign', 13, 'add_sign'),
(50, 'Can change sign', 13, 'change_sign'),
(51, 'Can delete sign', 13, 'delete_sign'),
(52, 'Can view sign', 13, 'view_sign'),
(53, 'Can add timeactsale', 14, 'add_timeactsale'),
(54, 'Can change timeactsale', 14, 'change_timeactsale'),
(55, 'Can delete timeactsale', 14, 'delete_timeactsale'),
(56, 'Can view timeactsale', 14, 'view_timeactsale'),
(57, 'Can add timeact', 15, 'add_timeact'),
(58, 'Can change timeact', 15, 'change_timeact'),
(59, 'Can delete timeact', 15, 'delete_timeact'),
(60, 'Can view timeact', 15, 'view_timeact'),
(61, 'Can add supplier', 16, 'add_supplier'),
(62, 'Can change supplier', 16, 'change_supplier'),
(63, 'Can delete supplier', 16, 'delete_supplier'),
(64, 'Can view supplier', 16, 'view_supplier'),
(65, 'Can add suplrcredit', 17, 'add_suplrcredit'),
(66, 'Can change suplrcredit', 17, 'change_suplrcredit'),
(67, 'Can delete suplrcredit', 17, 'delete_suplrcredit'),
(68, 'Can view suplrcredit', 17, 'view_suplrcredit'),
(69, 'Can add service', 18, 'add_service'),
(70, 'Can change service', 18, 'change_service'),
(71, 'Can delete service', 18, 'delete_service'),
(72, 'Can view service', 18, 'view_service'),
(73, 'Can add salesrecpts', 19, 'add_salesrecpts'),
(74, 'Can change salesrecpts', 19, 'change_salesrecpts'),
(75, 'Can delete salesrecpts', 19, 'delete_salesrecpts'),
(76, 'Can view salesrecpts', 19, 'view_salesrecpts'),
(77, 'Can add recordpay', 20, 'add_recordpay'),
(78, 'Can change recordpay', 20, 'change_recordpay'),
(79, 'Can delete recordpay', 20, 'delete_recordpay'),
(80, 'Can view recordpay', 20, 'view_recordpay'),
(81, 'Can add recon1', 21, 'add_recon1'),
(82, 'Can change recon1', 21, 'change_recon1'),
(83, 'Can delete recon1', 21, 'delete_recon1'),
(84, 'Can view recon1', 21, 'view_recon1'),
(85, 'Can add payslip', 22, 'add_payslip'),
(86, 'Can change payslip', 22, 'change_payslip'),
(87, 'Can delete payslip', 22, 'delete_payslip'),
(88, 'Can view payslip', 22, 'view_payslip'),
(89, 'Can add payment', 23, 'add_payment'),
(90, 'Can change payment', 23, 'change_payment'),
(91, 'Can delete payment', 23, 'delete_payment'),
(92, 'Can view payment', 23, 'view_payment'),
(93, 'Can add paydowncreditcard', 24, 'add_paydowncreditcard'),
(94, 'Can change paydowncreditcard', 24, 'change_paydowncreditcard'),
(95, 'Can delete paydowncreditcard', 24, 'delete_paydowncreditcard'),
(96, 'Can view paydowncreditcard', 24, 'view_paydowncreditcard'),
(97, 'Can add noninventory', 25, 'add_noninventory'),
(98, 'Can change noninventory', 25, 'change_noninventory'),
(99, 'Can delete noninventory', 25, 'delete_noninventory'),
(100, 'Can view noninventory', 25, 'view_noninventory'),
(101, 'Can add invoice', 26, 'add_invoice'),
(102, 'Can change invoice', 26, 'change_invoice'),
(103, 'Can delete invoice', 26, 'delete_invoice'),
(104, 'Can view invoice', 26, 'view_invoice'),
(105, 'Can add inventory', 27, 'add_inventory'),
(106, 'Can change inventory', 27, 'change_inventory'),
(107, 'Can delete inventory', 27, 'delete_inventory'),
(108, 'Can view inventory', 27, 'view_inventory'),
(109, 'Can add incomeaccount', 28, 'add_incomeaccount'),
(110, 'Can change incomeaccount', 28, 'change_incomeaccount'),
(111, 'Can delete incomeaccount', 28, 'delete_incomeaccount'),
(112, 'Can view incomeaccount', 28, 'view_incomeaccount'),
(113, 'Can add expences', 29, 'add_expences'),
(114, 'Can change expences', 29, 'change_expences'),
(115, 'Can delete expences', 29, 'delete_expences'),
(116, 'Can view expences', 29, 'view_expences'),
(117, 'Can add estimate', 30, 'add_estimate'),
(118, 'Can change estimate', 30, 'change_estimate'),
(119, 'Can delete estimate', 30, 'delete_estimate'),
(120, 'Can view estimate', 30, 'view_estimate'),
(121, 'Can add employee', 31, 'add_employee'),
(122, 'Can change employee', 31, 'change_employee'),
(123, 'Can delete employee', 31, 'delete_employee'),
(124, 'Can view employee', 31, 'view_employee'),
(125, 'Can add delayedcharge', 32, 'add_delayedcharge'),
(126, 'Can change delayedcharge', 32, 'change_delayedcharge'),
(127, 'Can delete delayedcharge', 32, 'delete_delayedcharge'),
(128, 'Can view delayedcharge', 32, 'view_delayedcharge'),
(129, 'Can add customize', 33, 'add_customize'),
(130, 'Can change customize', 33, 'change_customize'),
(131, 'Can delete customize', 33, 'delete_customize'),
(132, 'Can view customize', 33, 'view_customize'),
(133, 'Can add customer', 34, 'add_customer'),
(134, 'Can change customer', 34, 'change_customer'),
(135, 'Can delete customer', 34, 'delete_customer'),
(136, 'Can view customer', 34, 'view_customer'),
(137, 'Can add credit', 35, 'add_credit'),
(138, 'Can change credit', 35, 'change_credit'),
(139, 'Can delete credit', 35, 'delete_credit'),
(140, 'Can view credit', 35, 'view_credit'),
(141, 'Can add cheqs', 36, 'add_cheqs'),
(142, 'Can change cheqs', 36, 'change_cheqs'),
(143, 'Can delete cheqs', 36, 'delete_cheqs'),
(144, 'Can view cheqs', 36, 'view_cheqs'),
(145, 'Can add bundle', 37, 'add_bundle'),
(146, 'Can change bundle', 37, 'change_bundle'),
(147, 'Can delete bundle', 37, 'delete_bundle'),
(148, 'Can view bundle', 37, 'view_bundle'),
(149, 'Can add bills', 38, 'add_bills'),
(150, 'Can change bills', 38, 'change_bills'),
(151, 'Can delete bills', 38, 'delete_bills'),
(152, 'Can view bills', 38, 'view_bills'),
(153, 'Can add bankstatement', 39, 'add_bankstatement'),
(154, 'Can change bankstatement', 39, 'change_bankstatement'),
(155, 'Can delete bankstatement', 39, 'delete_bankstatement'),
(156, 'Can view bankstatement', 39, 'view_bankstatement'),
(157, 'Can add advancepayment', 40, 'add_advancepayment'),
(158, 'Can change advancepayment', 40, 'change_advancepayment'),
(159, 'Can delete advancepayment', 40, 'delete_advancepayment'),
(160, 'Can view advancepayment', 40, 'view_advancepayment'),
(161, 'Can add addtax1', 41, 'add_addtax1'),
(162, 'Can change addtax1', 41, 'change_addtax1'),
(163, 'Can delete addtax1', 41, 'delete_addtax1'),
(164, 'Can view addtax1', 41, 'view_addtax1'),
(165, 'Can add accounts1', 42, 'add_accounts1'),
(166, 'Can change accounts1', 42, 'change_accounts1'),
(167, 'Can delete accounts1', 42, 'delete_accounts1'),
(168, 'Can view accounts1', 42, 'view_accounts1'),
(169, 'Can add accounts', 43, 'add_accounts'),
(170, 'Can change accounts', 43, 'change_accounts'),
(171, 'Can delete accounts', 43, 'delete_accounts'),
(172, 'Can view accounts', 43, 'view_accounts'),
(173, 'Can add production', 44, 'add_production'),
(174, 'Can change production', 44, 'change_production'),
(175, 'Can delete production', 44, 'delete_production'),
(176, 'Can view production', 44, 'view_production');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(26, '123', NULL, 0, 'saiju2000', 'Saiju', 'Sunny', 'saiju@gmail.com', 0, 0, '2022-08-02 17:55:25.793236'),
(38, 'Saijus@123', NULL, 0, 'Saijus2000', 'sinu', 'zxc', 'zxcxz@gmail.com', 0, 0, '2022-08-03 16:26:03.508345'),
(41, 'Ammu@123', NULL, 0, 'ammu', 'Ammuis', 'sag', 'sadsa@gmail.com', 0, 0, '2022-08-04 14:06:58.637537'),
(42, 'ASD@12345', NULL, 0, 'asdassadsa', 'retre', 'retr', 'reter@gmail.com', 0, 0, '2022-08-04 14:20:06.470062'),
(44, 'Saibu@147', NULL, 0, 'saibu20002', 'Saibuss', 'Sunny', 'saibu@gmail.com', 0, 0, '2022-08-04 13:09:37.571853'),
(45, 'Lissy@123', NULL, 0, 'lissy2000', 'Lissy', 'Sunny', 'lissy@gmail.com', 0, 0, '2022-08-08 15:35:02.542016'),
(49, 'Sunny@123', NULL, 0, 'sunny2000', 'Sunny', 'Tc', 'sunny@gmail.Com', 0, 0, '2022-08-08 15:44:12.913222'),
(52, 'Sunny@123', NULL, 0, 'sunny22', 'Sunny', 'Tc', 'sunny@gmail.com', 0, 0, '2022-08-08 15:47:05.076095'),
(53, 'Vincu@123', NULL, 0, 'vincu2000', 'vincy', 'jiby', 'vin@gmail.com', 0, 0, '2022-08-08 15:51:29.537948'),
(54, 'Sdfd@123', NULL, 0, 'sdfd2000', 'sd', 'sdfd', 'sdfd@gmail.com', 0, 0, '2022-08-08 15:53:16.653727'),
(55, 'Lissy@123', NULL, 0, 'lissy@123', 'Lissy', 'Nv', 'lissi@gmail.com', 0, 0, '2022-09-23 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(43, 'app1', 'accounts'),
(42, 'app1', 'accounts1'),
(7, 'app1', 'accountype'),
(8, 'app1', 'addac'),
(41, 'app1', 'addtax1'),
(40, 'app1', 'advancepayment'),
(39, 'app1', 'bankstatement'),
(38, 'app1', 'bills'),
(37, 'app1', 'bundle'),
(36, 'app1', 'cheqs'),
(9, 'app1', 'company'),
(35, 'app1', 'credit'),
(34, 'app1', 'customer'),
(33, 'app1', 'customize'),
(32, 'app1', 'delayedcharge'),
(31, 'app1', 'employee'),
(30, 'app1', 'estimate'),
(29, 'app1', 'expences'),
(10, 'app1', 'expenseaccount'),
(28, 'app1', 'incomeaccount'),
(27, 'app1', 'inventory'),
(26, 'app1', 'invoice'),
(11, 'app1', 'itemmodel'),
(25, 'app1', 'noninventory'),
(24, 'app1', 'paydowncreditcard'),
(23, 'app1', 'payment'),
(22, 'app1', 'payslip'),
(44, 'app1', 'production'),
(12, 'app1', 'productmodel'),
(21, 'app1', 'recon1'),
(20, 'app1', 'recordpay'),
(19, 'app1', 'salesrecpts'),
(18, 'app1', 'service'),
(13, 'app1', 'sign'),
(17, 'app1', 'suplrcredit'),
(16, 'app1', 'supplier'),
(15, 'app1', 'timeact'),
(14, 'app1', 'timeactsale'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-08-02 07:53:08.750165'),
(2, 'auth', '0001_initial', '2022-08-02 07:53:22.456555'),
(3, 'admin', '0001_initial', '2022-08-02 07:53:25.243189'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-08-02 07:53:25.340940'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-08-02 07:53:25.400907'),
(6, 'app1', '0001_initial', '2022-08-02 07:54:15.722084'),
(7, 'app1', '0002_production', '2022-08-02 07:54:16.271469'),
(8, 'contenttypes', '0002_remove_content_type_name', '2022-08-02 07:54:17.416420'),
(9, 'auth', '0002_alter_permission_name_max_length', '2022-08-02 07:54:18.643758'),
(10, 'auth', '0003_alter_user_email_max_length', '2022-08-02 07:54:18.790300'),
(11, 'auth', '0004_alter_user_username_opts', '2022-08-02 07:54:18.863182'),
(12, 'auth', '0005_alter_user_last_login_null', '2022-08-02 07:54:20.112349'),
(13, 'auth', '0006_require_contenttypes_0002', '2022-08-02 07:54:20.186782'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2022-08-02 07:54:20.254743'),
(15, 'auth', '0008_alter_user_username_max_length', '2022-08-02 07:54:20.440635'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2022-08-02 07:54:20.550572'),
(17, 'auth', '0010_alter_group_name_max_length', '2022-08-02 07:54:20.803123'),
(18, 'auth', '0011_update_proxy_permissions', '2022-08-02 07:54:20.976790'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2022-08-02 07:54:21.111978'),
(20, 'sessions', '0001_initial', '2022-08-02 07:54:21.506066');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `itemstable`
--

CREATE TABLE `itemstable` (
  `Itemid` int(11) NOT NULL,
  `Itemname` varchar(100) NOT NULL,
  `Pid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `payee` varchar(255) DEFAULT NULL,
  `ref` varchar(255) DEFAULT NULL,
  `paymdate` date DEFAULT NULL,
  `payment_account` varchar(255) DEFAULT NULL,
  `payment_method` varchar(255) DEFAULT NULL,
  `ccatego` varchar(255) DEFAULT NULL,
  `cdescrip` varchar(255) DEFAULT NULL,
  `cqty` varchar(255) DEFAULT NULL,
  `cprice` varchar(255) DEFAULT NULL,
  `ctotal` varchar(255) DEFAULT NULL,
  `ccatego2` varchar(255) DEFAULT NULL,
  `cdescrip2` varchar(255) DEFAULT NULL,
  `cqty2` varchar(255) DEFAULT NULL,
  `cprice2` varchar(255) DEFAULT NULL,
  `ctotal2` varchar(255) DEFAULT NULL,
  `ccatego3` varchar(255) DEFAULT NULL,
  `cdescrip3` varchar(255) DEFAULT NULL,
  `cqty3` varchar(255) DEFAULT NULL,
  `cprice3` varchar(255) DEFAULT NULL,
  `ctotal3` varchar(255) DEFAULT NULL,
  `ccatego4` varchar(255) DEFAULT NULL,
  `cdescrip4` varchar(255) DEFAULT NULL,
  `cqty4` varchar(255) DEFAULT NULL,
  `cprice4` varchar(255) DEFAULT NULL,
  `ctotal4` varchar(255) DEFAULT NULL,
  `product` varchar(255) DEFAULT NULL,
  `hsn` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `qty` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `total` varchar(255) DEFAULT NULL,
  `product2` varchar(255) DEFAULT NULL,
  `hsn2` varchar(255) DEFAULT NULL,
  `description2` varchar(255) DEFAULT NULL,
  `qty2` varchar(255) DEFAULT NULL,
  `price2` varchar(255) DEFAULT NULL,
  `total2` varchar(255) DEFAULT NULL,
  `product3` varchar(255) DEFAULT NULL,
  `hsn3` varchar(255) DEFAULT NULL,
  `description3` varchar(255) DEFAULT NULL,
  `qty3` varchar(255) DEFAULT NULL,
  `price3` varchar(255) DEFAULT NULL,
  `total3` varchar(255) DEFAULT NULL,
  `product4` varchar(255) DEFAULT NULL,
  `hsn4` varchar(255) DEFAULT NULL,
  `description4` varchar(255) DEFAULT NULL,
  `qty4` varchar(255) DEFAULT NULL,
  `price4` varchar(255) DEFAULT NULL,
  `total4` varchar(255) DEFAULT NULL,
  `tax` varchar(255) DEFAULT NULL,
  `tax2` varchar(255) DEFAULT NULL,
  `tax3` varchar(255) DEFAULT NULL,
  `tax4` varchar(255) DEFAULT NULL,
  `subtotal` varchar(255) DEFAULT NULL,
  `taxamount` varchar(255) DEFAULT NULL,
  `grandtotal` varchar(255) DEFAULT NULL,
  `cid_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `payee`, `ref`, `paymdate`, `payment_account`, `payment_method`, `ccatego`, `cdescrip`, `cqty`, `cprice`, `ctotal`, `ccatego2`, `cdescrip2`, `cqty2`, `cprice2`, `ctotal2`, `ccatego3`, `cdescrip3`, `cqty3`, `cprice3`, `ctotal3`, `ccatego4`, `cdescrip4`, `cqty4`, `cprice4`, `ctotal4`, `product`, `hsn`, `description`, `qty`, `price`, `total`, `product2`, `hsn2`, `description2`, `qty2`, `price2`, `total2`, `product3`, `hsn3`, `description3`, `qty3`, `price3`, `total3`, `product4`, `hsn4`, `description4`, `qty4`, `price4`, `total4`, `tax`, `tax2`, `tax3`, `tax4`, `subtotal`, `taxamount`, `grandtotal`, `cid_id`) VALUES
(7, 'zxcxz xzcxzcz', '6', '2022-09-21', '', 'Debit cards', 'Consulting Income', 'asdhagsdhj', '1', '200', '200', 'Consulting Income', 'dfssf', '1', '100', '100', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'fdgf\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'fdg\n\n\n', '1', '200.0', '200.0', 'Mouse', 'fdg2154', 'fdgfd\n\n\n', '2', '200.0', '400.0', 'Mouse', 'fdg2154', 'fdgfd\n\n\n', '1', '200.0', '200.0', '28.0% GST(28%)', '18.0% GST(18%)', '28.0% GST(28%)', 'Choose', '1300.0', '148.0', '400', 6),
(10, 'ram kum', '10', '2022-09-23', 'Inventory', 'Cash', 'Billable Expense Income', 'erwewrw', '1', '200', '200', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'sad\n\n', '1', '201', '201.0', 'Mouse', 'fdg2154', '\n', '1', '200.0', '200.0', '', '', '\n\n', '0', '0', '', '', '', '\n\n', '0', '0', '', '28.0% GST(28%)', '28.0% GST(28%)', 'Choose', 'Choose', '601.0', '112.28', '713.28', 6),
(11, 'ram kum', '10', '2022-09-23', '', 'Cash', 'Billable Expense Income', 'erwewrw', '1', '200', '200', '', '', '0', '', '', '', '', '0', '', '', '', '', '0', '', '', 'Mouse', 'fdg2154', 'sad\n\n', '1', '201', '201.0', '', '', '\n\n', '0', '0', '', '', '', '\n\n', '0', '0', '', '', '', '\n\n', '0', '0', '', '28.0% GST(28%)', 'Choose', 'Choose', 'Choose', '401.0', '56.28', '56', 6);

-- --------------------------------------------------------

--
-- Table structure for table `producttable`
--

CREATE TABLE `producttable` (
  `Pid` int(11) NOT NULL,
  `Pname` varchar(100) NOT NULL,
  `sku` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `producttable`
--

INSERT INTO `producttable` (`Pid`, `Pname`, `sku`, `price`, `cid_id`) VALUES
(1, 'mi mobile', '1235', '200', 6),
(2, 'laptop', '154', '500', 6),
(3, 'vivo y11', '15478', '1200', 6),
(4, 'tv', '147', '500', 6),
(5, 'Ac', '1489', '250', 6),
(35, 'sdf', '1457', '81.6', 6),
(36, 'sdfssd', '78', '81.2', 6),
(37, 'vagi', '1254', '1260.0', 6),
(38, 'hp brand', '21', '2000', 6),
(40, 'zeb', '12456', '559.0', 6),
(41, 'rens', 'as2154', '247.33333333333334', 6),
(42, 'zeb', '12456', '357.0', 6),
(43, 'ph', '2354', '200', 6),
(44, 'rens', 'as2154', '247.33333333333334', 6),
(45, 'hp brand', 'xzcc', '200', 6),
(46, 'hp brand', '1254', '45000', 6);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app1_accounts`
--
ALTER TABLE `app1_accounts`
  ADD PRIMARY KEY (`accountsid`),
  ADD KEY `app1_accounts_cid_id_ca072561_fk_app1_company_cid` (`cid_id`),
  ADD KEY `app1_accounts_productid_id_ff25de48_fk_producttable_Pid` (`productid_id`),
  ADD KEY `app1_accounts_proid_id_d0d77a6d_fk_app1_accountype_accountypeid` (`proid_id`);

--
-- Indexes for table `app1_accounts1`
--
ALTER TABLE `app1_accounts1`
  ADD PRIMARY KEY (`accounts1id`),
  ADD KEY `app1_accounts1_cid_id_073c043d_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_accountype`
--
ALTER TABLE `app1_accountype`
  ADD PRIMARY KEY (`accountypeid`),
  ADD KEY `app1_accountype_cid_id_b591dd7d_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_addac`
--
ALTER TABLE `app1_addac`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app1_addtax1`
--
ALTER TABLE `app1_addtax1`
  ADD PRIMARY KEY (`addtax1id`),
  ADD KEY `app1_addtax1_cid_id_90eebb52_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_advancepayment`
--
ALTER TABLE `app1_advancepayment`
  ADD PRIMARY KEY (`advancepaymentid`),
  ADD KEY `app1_advancepayment_cid_id_796af5b3_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_bankstatement`
--
ALTER TABLE `app1_bankstatement`
  ADD PRIMARY KEY (`bankstatementid`),
  ADD KEY `app1_bankstatement_cid_id_00a3fc3b_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_bills`
--
ALTER TABLE `app1_bills`
  ADD PRIMARY KEY (`billid`),
  ADD KEY `app1_bills_cid_id_d648c3f6_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_bundle`
--
ALTER TABLE `app1_bundle`
  ADD PRIMARY KEY (`bundleid`),
  ADD KEY `app1_bundle_cid_id_82c2ec98_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_cheqs`
--
ALTER TABLE `app1_cheqs`
  ADD PRIMARY KEY (`chequeid`),
  ADD KEY `app1_cheqs_cid_id_ff8a2ca6_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_company`
--
ALTER TABLE `app1_company`
  ADD PRIMARY KEY (`cid`),
  ADD KEY `app1_company_id_id_84084c19_fk_auth_user_id` (`id_id`);

--
-- Indexes for table `app1_credit`
--
ALTER TABLE `app1_credit`
  ADD PRIMARY KEY (`creditnoteid`),
  ADD KEY `app1_credit_cid_id_40b75237_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_customer`
--
ALTER TABLE `app1_customer`
  ADD PRIMARY KEY (`customerid`),
  ADD KEY `app1_customer_cid_id_607bad1d_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_customize`
--
ALTER TABLE `app1_customize`
  ADD PRIMARY KEY (`customizeid`),
  ADD KEY `app1_customize_cid_id_059fe662_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_delayedcharge`
--
ALTER TABLE `app1_delayedcharge`
  ADD PRIMARY KEY (`delayedchargeid`),
  ADD KEY `app1_delayedcharge_cid_id_b9dff420_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_employee`
--
ALTER TABLE `app1_employee`
  ADD PRIMARY KEY (`employeeid`),
  ADD KEY `app1_employee_cid_id_62659cb7_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_estimate`
--
ALTER TABLE `app1_estimate`
  ADD PRIMARY KEY (`estimateid`),
  ADD KEY `app1_estimate_cid_id_983a0fc3_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_expences`
--
ALTER TABLE `app1_expences`
  ADD PRIMARY KEY (`expencesid`),
  ADD KEY `app1_expences_cid_id_2cd98c8f_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_expenseaccount`
--
ALTER TABLE `app1_expenseaccount`
  ADD PRIMARY KEY (`expenseid`),
  ADD KEY `app1_expenseaccount_cid_id_df816740_fk_app1_company_cid` (`cid_id`),
  ADD KEY `app1_expenseaccount_expaccountypid_id_67312bdf_fk_app1_acco` (`expaccountypid_id`);

--
-- Indexes for table `app1_incomeaccount`
--
ALTER TABLE `app1_incomeaccount`
  ADD PRIMARY KEY (`incomeid`),
  ADD KEY `app1_incomeaccount_cid_id_094b46f8_fk_app1_company_cid` (`cid_id`),
  ADD KEY `app1_incomeaccount_expenceincomeid_id_f4304840_fk_app1_expe` (`expenceincomeid_id`);

--
-- Indexes for table `app1_inventory`
--
ALTER TABLE `app1_inventory`
  ADD PRIMARY KEY (`inventoryid`),
  ADD KEY `app1_inventory_cid_id_f2e81863_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_invoice`
--
ALTER TABLE `app1_invoice`
  ADD PRIMARY KEY (`invoiceid`),
  ADD KEY `app1_invoice_cid_id_a9c8e9b5_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_noninventory`
--
ALTER TABLE `app1_noninventory`
  ADD PRIMARY KEY (`noninventoryid`),
  ADD KEY `app1_noninventory_cid_id_d0447e15_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_paydowncreditcard`
--
ALTER TABLE `app1_paydowncreditcard`
  ADD PRIMARY KEY (`paycreditcardid`),
  ADD KEY `app1_paydowncreditcard_cid_id_148fd035_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_payment`
--
ALTER TABLE `app1_payment`
  ADD PRIMARY KEY (`paymentid`),
  ADD KEY `app1_payment_cid_id_a954b426_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_payslip`
--
ALTER TABLE `app1_payslip`
  ADD PRIMARY KEY (`payslipid`),
  ADD KEY `app1_payslip_cid_id_3f97b6d6_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_production`
--
ALTER TABLE `app1_production`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cid_id` (`cid_id`);

--
-- Indexes for table `app1_recon1`
--
ALTER TABLE `app1_recon1`
  ADD PRIMARY KEY (`recon1id`),
  ADD KEY `app1_recon1_cid_id_958c7d0e_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_recordpay`
--
ALTER TABLE `app1_recordpay`
  ADD PRIMARY KEY (`recordpayid`),
  ADD KEY `app1_recordpay_cid_id_f3d93b71_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_salesrecpts`
--
ALTER TABLE `app1_salesrecpts`
  ADD PRIMARY KEY (`salesrecptsid`),
  ADD KEY `app1_salesrecpts_cid_id_7834f425_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_service`
--
ALTER TABLE `app1_service`
  ADD PRIMARY KEY (`serviceid`),
  ADD KEY `app1_service_cid_id_e19684ee_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_sign`
--
ALTER TABLE `app1_sign`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `app1_suplrcredit`
--
ALTER TABLE `app1_suplrcredit`
  ADD PRIMARY KEY (`suppliercreditid`),
  ADD KEY `app1_suplrcredit_cid_id_943a7180_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_supplier`
--
ALTER TABLE `app1_supplier`
  ADD PRIMARY KEY (`supplierid`),
  ADD KEY `app1_supplier_cid_id_53a00add_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_timeact`
--
ALTER TABLE `app1_timeact`
  ADD PRIMARY KEY (`timeactid`),
  ADD KEY `app1_timeact_cid_id_2709432a_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `app1_timeactsale`
--
ALTER TABLE `app1_timeactsale`
  ADD PRIMARY KEY (`timeactsaleid`),
  ADD KEY `app1_timeactsale_cid_id_0dcbffb2_fk_app1_company_cid` (`cid_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `itemstable`
--
ALTER TABLE `itemstable`
  ADD PRIMARY KEY (`Itemid`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cid_id` (`cid_id`);

--
-- Indexes for table `producttable`
--
ALTER TABLE `producttable`
  ADD PRIMARY KEY (`Pid`),
  ADD KEY `cid_id` (`cid_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app1_accounts`
--
ALTER TABLE `app1_accounts`
  MODIFY `accountsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `app1_accounts1`
--
ALTER TABLE `app1_accounts1`
  MODIFY `accounts1id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123;

--
-- AUTO_INCREMENT for table `app1_accountype`
--
ALTER TABLE `app1_accountype`
  MODIFY `accountypeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `app1_addac`
--
ALTER TABLE `app1_addac`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_addtax1`
--
ALTER TABLE `app1_addtax1`
  MODIFY `addtax1id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_advancepayment`
--
ALTER TABLE `app1_advancepayment`
  MODIFY `advancepaymentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `app1_bankstatement`
--
ALTER TABLE `app1_bankstatement`
  MODIFY `bankstatementid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app1_bills`
--
ALTER TABLE `app1_bills`
  MODIFY `billid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_bundle`
--
ALTER TABLE `app1_bundle`
  MODIFY `bundleid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app1_cheqs`
--
ALTER TABLE `app1_cheqs`
  MODIFY `chequeid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_company`
--
ALTER TABLE `app1_company`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `app1_credit`
--
ALTER TABLE `app1_credit`
  MODIFY `creditnoteid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `app1_customer`
--
ALTER TABLE `app1_customer`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `app1_customize`
--
ALTER TABLE `app1_customize`
  MODIFY `customizeid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_delayedcharge`
--
ALTER TABLE `app1_delayedcharge`
  MODIFY `delayedchargeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `app1_employee`
--
ALTER TABLE `app1_employee`
  MODIFY `employeeid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `app1_estimate`
--
ALTER TABLE `app1_estimate`
  MODIFY `estimateid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `app1_expences`
--
ALTER TABLE `app1_expences`
  MODIFY `expencesid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `app1_expenseaccount`
--
ALTER TABLE `app1_expenseaccount`
  MODIFY `expenseid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_incomeaccount`
--
ALTER TABLE `app1_incomeaccount`
  MODIFY `incomeid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_inventory`
--
ALTER TABLE `app1_inventory`
  MODIFY `inventoryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app1_invoice`
--
ALTER TABLE `app1_invoice`
  MODIFY `invoiceid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `app1_noninventory`
--
ALTER TABLE `app1_noninventory`
  MODIFY `noninventoryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app1_paydowncreditcard`
--
ALTER TABLE `app1_paydowncreditcard`
  MODIFY `paycreditcardid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_payment`
--
ALTER TABLE `app1_payment`
  MODIFY `paymentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `app1_payslip`
--
ALTER TABLE `app1_payslip`
  MODIFY `payslipid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_production`
--
ALTER TABLE `app1_production`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `app1_recon1`
--
ALTER TABLE `app1_recon1`
  MODIFY `recon1id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_recordpay`
--
ALTER TABLE `app1_recordpay`
  MODIFY `recordpayid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_salesrecpts`
--
ALTER TABLE `app1_salesrecpts`
  MODIFY `salesrecptsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `app1_service`
--
ALTER TABLE `app1_service`
  MODIFY `serviceid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_sign`
--
ALTER TABLE `app1_sign`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app1_suplrcredit`
--
ALTER TABLE `app1_suplrcredit`
  MODIFY `suppliercreditid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `app1_supplier`
--
ALTER TABLE `app1_supplier`
  MODIFY `supplierid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `app1_timeact`
--
ALTER TABLE `app1_timeact`
  MODIFY `timeactid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `app1_timeactsale`
--
ALTER TABLE `app1_timeactsale`
  MODIFY `timeactsaleid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=177;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `producttable`
--
ALTER TABLE `producttable`
  MODIFY `Pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app1_accounts`
--
ALTER TABLE `app1_accounts`
  ADD CONSTRAINT `app1_accounts_cid_id_ca072561_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`),
  ADD CONSTRAINT `app1_accounts_productid_id_ff25de48_fk_producttable_Pid` FOREIGN KEY (`productid_id`) REFERENCES `producttable` (`Pid`),
  ADD CONSTRAINT `app1_accounts_proid_id_d0d77a6d_fk_app1_accountype_accountypeid` FOREIGN KEY (`proid_id`) REFERENCES `app1_accountype` (`accountypeid`);

--
-- Constraints for table `app1_accounts1`
--
ALTER TABLE `app1_accounts1`
  ADD CONSTRAINT `app1_accounts1_cid_id_073c043d_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_accountype`
--
ALTER TABLE `app1_accountype`
  ADD CONSTRAINT `app1_accountype_cid_id_b591dd7d_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_addtax1`
--
ALTER TABLE `app1_addtax1`
  ADD CONSTRAINT `app1_addtax1_cid_id_90eebb52_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_advancepayment`
--
ALTER TABLE `app1_advancepayment`
  ADD CONSTRAINT `app1_advancepayment_cid_id_796af5b3_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_bankstatement`
--
ALTER TABLE `app1_bankstatement`
  ADD CONSTRAINT `app1_bankstatement_cid_id_00a3fc3b_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_bills`
--
ALTER TABLE `app1_bills`
  ADD CONSTRAINT `app1_bills_cid_id_d648c3f6_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_bundle`
--
ALTER TABLE `app1_bundle`
  ADD CONSTRAINT `app1_bundle_cid_id_82c2ec98_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_cheqs`
--
ALTER TABLE `app1_cheqs`
  ADD CONSTRAINT `app1_cheqs_cid_id_ff8a2ca6_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_company`
--
ALTER TABLE `app1_company`
  ADD CONSTRAINT `app1_company_id_id_84084c19_fk_auth_user_id` FOREIGN KEY (`id_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app1_credit`
--
ALTER TABLE `app1_credit`
  ADD CONSTRAINT `app1_credit_cid_id_40b75237_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_customer`
--
ALTER TABLE `app1_customer`
  ADD CONSTRAINT `app1_customer_cid_id_607bad1d_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_customize`
--
ALTER TABLE `app1_customize`
  ADD CONSTRAINT `app1_customize_cid_id_059fe662_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_delayedcharge`
--
ALTER TABLE `app1_delayedcharge`
  ADD CONSTRAINT `app1_delayedcharge_cid_id_b9dff420_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_employee`
--
ALTER TABLE `app1_employee`
  ADD CONSTRAINT `app1_employee_cid_id_62659cb7_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_estimate`
--
ALTER TABLE `app1_estimate`
  ADD CONSTRAINT `app1_estimate_cid_id_983a0fc3_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_expences`
--
ALTER TABLE `app1_expences`
  ADD CONSTRAINT `app1_expences_cid_id_2cd98c8f_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_expenseaccount`
--
ALTER TABLE `app1_expenseaccount`
  ADD CONSTRAINT `app1_expenseaccount_cid_id_df816740_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`),
  ADD CONSTRAINT `app1_expenseaccount_expaccountypid_id_67312bdf_fk_app1_acco` FOREIGN KEY (`expaccountypid_id`) REFERENCES `app1_accountype` (`accountypeid`);

--
-- Constraints for table `app1_incomeaccount`
--
ALTER TABLE `app1_incomeaccount`
  ADD CONSTRAINT `app1_incomeaccount_cid_id_094b46f8_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`),
  ADD CONSTRAINT `app1_incomeaccount_expenceincomeid_id_f4304840_fk_app1_expe` FOREIGN KEY (`expenceincomeid_id`) REFERENCES `app1_expenseaccount` (`expenseid`);

--
-- Constraints for table `app1_inventory`
--
ALTER TABLE `app1_inventory`
  ADD CONSTRAINT `app1_inventory_cid_id_f2e81863_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_invoice`
--
ALTER TABLE `app1_invoice`
  ADD CONSTRAINT `app1_invoice_cid_id_a9c8e9b5_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_noninventory`
--
ALTER TABLE `app1_noninventory`
  ADD CONSTRAINT `app1_noninventory_cid_id_d0447e15_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_paydowncreditcard`
--
ALTER TABLE `app1_paydowncreditcard`
  ADD CONSTRAINT `app1_paydowncreditcard_cid_id_148fd035_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_payment`
--
ALTER TABLE `app1_payment`
  ADD CONSTRAINT `app1_payment_cid_id_a954b426_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_payslip`
--
ALTER TABLE `app1_payslip`
  ADD CONSTRAINT `app1_payslip_cid_id_3f97b6d6_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_production`
--
ALTER TABLE `app1_production`
  ADD CONSTRAINT `app1_production_ibfk_1` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_recon1`
--
ALTER TABLE `app1_recon1`
  ADD CONSTRAINT `app1_recon1_cid_id_958c7d0e_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_recordpay`
--
ALTER TABLE `app1_recordpay`
  ADD CONSTRAINT `app1_recordpay_cid_id_f3d93b71_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_salesrecpts`
--
ALTER TABLE `app1_salesrecpts`
  ADD CONSTRAINT `app1_salesrecpts_cid_id_7834f425_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_service`
--
ALTER TABLE `app1_service`
  ADD CONSTRAINT `app1_service_cid_id_e19684ee_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_suplrcredit`
--
ALTER TABLE `app1_suplrcredit`
  ADD CONSTRAINT `app1_suplrcredit_cid_id_943a7180_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_supplier`
--
ALTER TABLE `app1_supplier`
  ADD CONSTRAINT `app1_supplier_cid_id_53a00add_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_timeact`
--
ALTER TABLE `app1_timeact`
  ADD CONSTRAINT `app1_timeact_cid_id_2709432a_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `app1_timeactsale`
--
ALTER TABLE `app1_timeactsale`
  ADD CONSTRAINT `app1_timeactsale_cid_id_0dcbffb2_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);

--
-- Constraints for table `producttable`
--
ALTER TABLE `producttable`
  ADD CONSTRAINT `producttable_ibfk_1` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
