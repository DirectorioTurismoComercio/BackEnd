-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 27-01-2016 a las 12:11:42
-- Versión del servidor: 5.5.38-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4.5

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `plataforma`
--

--
-- Volcado de datos para la tabla `plataforma_municipio`
--
INSERT INTO `sitios_sitio` (`nombre`, `latitud`, `longitud`) VALUES
('Bogota Bar',4.66828,-74.055457),
('SILENCIO BAR',4.66771508574261,-74.0544954545059),
('SIMONA SHOT',4.66771508574261,-74.0544954545059),
('COLOMBIAN PUB MARLY',4.63759461676702,-74.0639712296873),
('HOTEL V BOGOTA',4.668682,-74.054244),
('MARQUEZ BAR BTA',4.66785712898823,-74.0550116335708),
('FULL 80S 85 PASEO DEL FARO',4.667664,-74.05234),
('MALABAR BOGOTA',4.6375594338091,-74.0638673689284),
('LA CASA DE MATILDE LINA',4.66545235735413,-74.0536352236533),
('NOA NOA DISCO',4.64809554553747,-74.0633909529381),
('MATCH BOX CAFE',4.66808908502512,-74.0551963370065),
('BIZARRO DISCO - BAR',4.5846336091603,-74.1007375490765),
('SANTIAMEN V. I .P',4.58494402566598,-74.100152327227),
('PA BOHEMIOS',4.58367736251751,-74.100516567334),
('NEW STUDIO 53',4.64245383712095,-74.0766330996144),
('AMARANTA CAFE BAR RESTREPO',4.58455096956884,-74.0995206956337),
('GUZMAN NOHORA ALBA',4.58411148580602,-74.0999116084241),
('DISCOTECA BAR EL TEMPLO',4.58461070499538,-74.1000960430523),
('LA SANTA V.I.P.',4.5842376240189,-74.0994871074974),
('VIEJOTECA EL CONDADO',4.58466064766255,-74.1001430598795),
('RINCON PAISA DE ORTIZ',4.58416050236045,-74.1014570927021),
('ESTADIO EL CAMPíN', 4.646012,-74.077330);

--
-- Volcado de datos para la tabla `sitios_sitio`
--
INSERT INTO `plataforma_municipio` (`nombre`, `latitud`, `longitud`) VALUES
('Boita',4.66828,-74.055457),
('Bogotá',4.66771508574261,-74.0544954545059),
('Chía',4.66771508574261,-74.0544954545059),
('Mosquera',4.63759461676702,-74.0639712296873);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
