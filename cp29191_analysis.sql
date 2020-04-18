-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Апр 18 2020 г., 18:45
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
-- Структура таблицы `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `id_student` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `record_book` int(11) NOT NULL,
  PRIMARY KEY (`id_student`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`id_student`, `name`, `record_book`) VALUES
(1, 'Иванов Иван Иванович', 123442),
(2, 'Петров Дмитрий Константинович', 123432);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
