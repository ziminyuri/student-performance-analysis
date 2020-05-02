-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Май 02 2020 г., 15:00
-- Версия сервера: 5.6.39-83.1
-- Версия PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `cp29191_analysis`
--

-- --------------------------------------------------------

--
-- Структура таблицы `discipline`
--

CREATE TABLE IF NOT EXISTS `discipline` (
  `id_discipline` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  PRIMARY KEY (`id_discipline`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `discipline`
--

INSERT INTO `discipline` (`id_discipline`, `name`) VALUES
(1, 'Операционные системы'),
(2, 'Алгоритмы и структуры данных');

-- --------------------------------------------------------

--
-- Структура таблицы `grade`
--

CREATE TABLE IF NOT EXISTS `grade` (
  `id_grade` int(11) NOT NULL AUTO_INCREMENT,
  `value` int(11) NOT NULL,
  `date` date NOT NULL,
  `id_work` int(11) NOT NULL,
  `id_student` int(11) NOT NULL,
  PRIMARY KEY (`id_grade`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `grade`
--

INSERT INTO `grade` (`id_grade`, `value`, `date`, `id_work`, `id_student`) VALUES
(1, 90, '2020-02-14', 1, 1),
(2, 80, '2020-04-01', 2, 2),
(3, 80, '2020-04-07', 3, 1),
(4, 90, '2020-03-13', 3, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `group_table`
--

CREATE TABLE IF NOT EXISTS `group_table` (
  `id_group` int(11) NOT NULL AUTO_INCREMENT,
  `number` char(255) NOT NULL,
  `id_specialty` int(11) NOT NULL,
  PRIMARY KEY (`id_group`),
  KEY `IX_Relationship1` (`id_specialty`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `group_table`
--

INSERT INTO `group_table` (`id_group`, `number`, `id_specialty`) VALUES
(1, '432432234', 1),
(2, '342234', 2),
(3, '423243', 3),
(4, '342324', 4),
(5, '423423', 4),
(6, '342324', 2),
(7, '342432', 2);

-- --------------------------------------------------------

--
-- Структура таблицы `specialty`
--

CREATE TABLE IF NOT EXISTS `specialty` (
  `id_specialty` int(11) NOT NULL AUTO_INCREMENT,
  `code` char(30) NOT NULL,
  `name` char(255) NOT NULL,
  PRIMARY KEY (`id_specialty`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `specialty`
--

INSERT INTO `specialty` (`id_specialty`, `code`, `name`) VALUES
(1, '10.03.01', 'Информационная безопасность'),
(2, '09.03.04', 'Программная инженерия'),
(3, '12.03.01', 'Приборостроение'),
(4, '09.03.02', 'Информационные системы и технологии');

-- --------------------------------------------------------

--
-- Структура таблицы `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `id_student` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `record_book` int(11) NOT NULL,
  `id_group` int(11) NOT NULL,
  PRIMARY KEY (`id_student`),
  KEY `IX_Relationship3` (`id_group`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`id_student`, `name`, `record_book`, `id_group`) VALUES
(1, 'Иванов Иван Иванович', 123442, 1),
(2, 'Петров Дмитрий Константинович', 123432, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` char(255) NOT NULL,
  `password` char(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password`) VALUES
(1, 'molchanova', '739548637fc51ad74e61a46767c456fece496b4e696dfdb9c22f0ac15f9c9f77'),
(2, 'vojvodina', '68bb59b75f87fc4b53d934eee65dff1406ca56c0a1f0ab5b993d8ab83d2045bc');

-- --------------------------------------------------------

--
-- Структура таблицы `work`
--

CREATE TABLE IF NOT EXISTS `work` (
  `id_work` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `id_group` int(11) NOT NULL,
  `id_discipline` int(11) NOT NULL,
  PRIMARY KEY (`id_work`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `work`
--

INSERT INTO `work` (`id_work`, `name`, `id_group`, `id_discipline`) VALUES
(1, 'Лабораторная работа №1', 1, 1),
(2, 'Лабораторная работа №2', 1, 1),
(3, 'Лабораторная работа №3', 1, 1),
(4, 'Лабораторная работа №4', 1, 1),
(5, 'Лабораторная работа №1', 1, 2),
(6, 'Лабораторная работа №2', 1, 2);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
