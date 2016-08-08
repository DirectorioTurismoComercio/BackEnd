-- phpMyAdmin SQL Dump
-- version 4.3.8
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 27-01-2016 a las 11:33:47
-- Versión del servidor: 5.5.42-37.1
-- Versión de PHP: 5.4.23

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `camjoha_turismo`
--

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$15000$S2AMAeYI7tnG$WBmh7OIyDfpVS1Dtk2c0n+wlJ9JPhGZnIZaWXcoxnZk=', '2015-03-26 15:04:36', 1, 'camilo', '', '', '', 1, 1, '2015-03-26 15:04:36'),
(2, 'pbkdf2_sha256$20000$Lfk1pJunMPvf$MftHpUOhme+X0emeWCtA2t+CzxSa41yH1+NVFmHUGd0=', NULL, 0, 'perez@hotmail.com', '', '', 'perez@hotmail.com', 0, 1, '2015-10-16 17:36:30'),
(3, 'pbkdf2_sha256$20000$54IirRXdfLxd$WoTmybLlngBLKg9O9lldgYAFT3ApAx933SJqRhhnamg=', NULL, 0, 'luispacholopez@gmail.com', '', '', 'luispacholopez@gmail.com', 0, 1, '2015-10-19 14:55:54'),
(4, 'pbkdf2_sha256$20000$X0r2duuiB8ZU$AEWw+RwRi5SReaPN0eOlbEsnnhAN+jfNXEAFNHg/chU=', NULL, 0, 'perez@jmail.com', '', '', 'perez@jmail.com', 0, 1, '2015-11-12 16:21:32'),
(5, 'pbkdf2_sha256$20000$wEW87qqqiKoi$vwrHYJk46tz8a3fK0hcutNhADES8x84Rbzbp3su7OwA=', NULL, 0, 'gutierrez@jmail.com', '', '', 'gutierrez@jmail.com', 0, 1, '2015-11-12 16:29:25'),
(6, 'pbkdf2_sha256$20000$Orh3cG1bt0Mw$R1eykvtDn3mbfnvJrJojUgM77WNkjZ2rbIScRxtwXTU=', NULL, 0, 'andres@mail.com', '', '', 'andres@mail.com', 0, 1, '2015-11-20 02:18:37'),
(7, 'pbkdf2_sha256$20000$EOBVJ6aEbv8p$+itc9MkryKf58aBqbU9laCbhJ+qz0uamFM8xAK8BoJ4=', NULL, 0, 'donato@mail.com', '', '', 'donato@mail.com', 0, 1, '2015-11-20 14:55:52'),
(8, 'pbkdf2_sha256$20000$h1tWH04oyRJt$Zb6k8qHQGNDSoARdnVAvpjAcqi6jxFN1619Ab8Jmmuk=', NULL, 0, 'alatorre16@aol.com', '', '', 'alatorre16@aol.com', 0, 1, '2015-11-20 15:09:45'),
(9, 'pbkdf2_sha256$20000$iFAPuuYJF6SD$u/QubZbErpFb1WxgC1sTebJpZGzS42tfdqnC8QOiMjY=', NULL, 0, 'luis@mail.com', '', '', 'luis@mail.com', 0, 1, '2015-11-20 16:12:49'),
(10, 'pbkdf2_sha256$20000$mFN1MoJz8Shz$IuU3qT2N+c1+u7Q3lLFUYp4d8HDT/oHafUEfj+8OB+k=', NULL, 0, 'npparrao@unal.edu.co', '', '', 'npparrao@unal.edu.co', 0, 1, '2015-11-30 15:47:18'),
(11, 'pbkdf2_sha256$20000$j5rn6Q2AQchF$nzhjlLNlFVXX3PBYf4o43pKAwfaAY4HyBoksUVwZbVw=', NULL, 0, 'nuevo@mail.com', '', '', 'nuevo@mail.com', 0, 1, '2015-12-04 16:28:47'),
(12, 'pbkdf2_sha256$20000$qaC8uT5DVf9k$Uus77pV3oWpfqfZrmziMtTxNS1u/66VWquNLTqBU4Fw=', NULL, 0, 'turismo@mail.com', '', '', 'turismo@mail.com', 0, 1, '2015-12-04 16:32:34'),
(13, 'pbkdf2_sha256$20000$oJLDkvg3Z9Hi$XWee4HBUIPnIHr0cYylCyPWAleTbMp0FaFZ1foJT/3g=', NULL, 0, 'aaa@aaa.com', '', '', 'aaa@aaa.com', 0, 1, '2015-12-04 16:41:57'),
(14, 'pbkdf2_sha256$20000$xsytXpaiFqk5$/u8Dx5N68o2z52XE7cruabwGNGwTH7lE0WFRcFqbEGw=', NULL, 0, 'comercio@mail.com', '', '', 'comercio@mail.com', 0, 1, '2015-12-04 16:48:06'),
(15, 'pbkdf2_sha256$20000$nLmEFRUHrgoE$PaIpQwNLAm+YRwgWGqbB1WHzIQJHHWjVTEvEKg58mUI=', NULL, 0, 'ofrezco@mail.com', '', '', 'ofrezco@mail.com', 0, 1, '2015-12-04 16:49:39'),
(16, 'pbkdf2_sha256$20000$O1q5866KSXRW$LqszQJYRmHWTt4+TjJLLAV3uirYdnF8w8vhHoxfu9uI=', NULL, 0, 'pruebac@mail.com', '', '', 'pruebac@mail.com', 0, 1, '2015-12-07 12:14:45'),
(17, 'pbkdf2_sha256$20000$Z5zDZWdawMnB$dhG2U/6aT1vJu6guVN+5UMa2/B+fO97aiDY9cdCSHS8=', NULL, 0, 'empresario@mail.com', '', '', 'empresario@mail.com', 0, 1, '2015-12-07 13:23:02'),
(18, 'pbkdf2_sha256$20000$z2O98F52NkrQ$WY3zD4SAzBslaEUHCPW48Nz6037x+2ZjfpKL67AlVW4=', NULL, 0, 'programador@mail.com', '', '', 'programador@mail.com', 0, 1, '2015-12-07 13:24:08'),
(19, 'pbkdf2_sha256$20000$NPXafnIjR0lD$l0Wb+ir6Xp5Np2rqwiSXDCwQfEgyZksCALao6H1Dc6Q=', NULL, 0, 'jacinto@mail.com', '', '', 'jacinto@mail.com', 0, 1, '2015-12-07 15:07:03'),
(20, 'pbkdf2_sha256$20000$SkFeRroT2cnN$ju4ipYyLOMWppJLU78ygPJzaMWGflwNbXOjeBqsqQJI=', NULL, 0, 'martinmejia2112@gmail.com', '', '', 'martinmejia2112@gmail.com', 0, 1, '2015-12-11 14:20:28'),
(21, 'pbkdf2_sha256$20000$R228mksGQYnL$IKlONQXcpb9OkwgZ4Q/wR37m19hnJ46IUFQjjTrsQgE=', NULL, 0, 'mauricio@longboardcolombia.com', '', '', 'mauricio@longboardcolombia.com', 0, 1, '2015-12-11 16:36:51'),
(22, 'pbkdf2_sha256$20000$TISmsEw6cdfL$PpZalAFnJrweTQ4jfXBvJL9EvO+EjJ0rRXbKwDLGYDQ=', NULL, 0, 'temp@gmail.com', '', '', 'temp@gmail.com', 0, 1, '2015-12-14 15:29:46'),
(23, 'pbkdf2_sha256$20000$wDAmU72VzAdY$w6oAP90BwoQBvhn9EZJI0JAEPd2gHEMWtXnRuT/14vI=', NULL, 0, 'julia@mail.com', '', '', 'julia@mail.com', 0, 1, '2015-12-14 15:32:39'),
(24, 'pbkdf2_sha256$20000$atE02OrxF4Ex$fBUIkVUc/oBVfwgSLHN1tio2WrTzltfdlGB8S+hkED0=', NULL, 0, 'mauriciocamacho@gmail.com', '', '', 'mauriciocamacho@gmail.com', 0, 1, '2015-12-17 17:19:49'),
(25, 'pbkdf2_sha256$20000$YoiHNDaliUHS$B8o1AibG3btdTTUh5VqN/iYvH1DcM2YRHzF7viYbgi8=', NULL, 0, 'usuariouno@usuario.com', '', '', 'usuariouno@usuario.com', 0, 1, '2016-01-20 20:00:06'),
(26, 'pbkdf2_sha256$20000$yU8Xr30zgFRp$jOsdEU6phx0TbNczLtu4JLnzOQdz1rSeLFak4ZrCmDc=', NULL, 0, 'empresariouno@empresario.com', '', '', 'empresariouno@empresario.com', 0, 1, '2016-01-20 20:04:01'),
(27, 'pbkdf2_sha256$20000$WI0q7qj1E3P1$J5B3xi3bxW8jfVjffZdJJ855pymXX4a9UuJnvRlE66I=', NULL, 0, 'agenciauno@agencia.com', '', '', 'agenciauno@agencia.com', 0, 1, '2016-01-20 20:08:52'),
(28, 'pbkdf2_sha256$20000$7rLcMXN4f3gW$GjRWsgqD2GxcMx1dnP9pfnhyERZrHNTwnOvc+FgkGcQ=', NULL, 0, 'misantropee@gmail.com', '', '', 'misantropee@gmail.com', 0, 1, '2016-01-21 16:47:45'),
(29, 'pbkdf2_sha256$20000$g7Op24E3VTMK$+zorFyC/UXc4FMHowg7bg4jgA5+byD26kTmrFNg1yRM=', NULL, 0, 'disenadoruno@disenador.com', '', '', 'disenadoruno@disenador.com', 0, 1, '2016-01-21 17:59:03'),
(30, 'pbkdf2_sha256$20000$jrcGkz4qUilJ$AsxOcbZqOHclTTwix5of5H4Kn2WMDSy+TjGCDEEn8z4=', NULL, 0, 'turismouno@turismo.com', '', '', 'turismouno@turismo.com', 0, 1, '2016-01-21 18:11:10'),
(31, 'pbkdf2_sha256$20000$BpJujsZZGIPo$Eoz0S6UTqzRmU1iYUKYdWHpd5bePCAQC65W1InowEm4=', NULL, 0, 'dayana@alejo.com', '', '', 'dayana@alejo.com', 0, 1, '2016-01-21 18:14:39'),
(32, 'pbkdf2_sha256$20000$GWa8u0LBvqVX$Pv/OMj6MTeEYwAmTaD9sejHyoMtMTkP6BsrqXmg+Xyo=', NULL, 0, 'hotelero@hotelero.com', '', '', 'hotelero@hotelero.com', 0, 1, '2016-01-21 18:51:25'),
(33, 'pbkdf2_sha256$20000$zGNfvJ1v1BnJ$u8Gqq/X1faGEAEGnMVW922khbq357gkKvIbJjQER6Es=', NULL, 0, 'artesano@artesano.com', '', '', 'artesano@artesano.com', 0, 1, '2016-01-21 19:39:15'),
(34, 'pbkdf2_sha256$20000$xG6izKOQBtUh$yeLDKoJRaAAWWfgRTZsnBgNOpFLNp52GaXVNy4lK0+I=', NULL, 0, 'artesanouno@artesano.com', '', '', 'artesanouno@artesano.com', 0, 1, '2016-01-22 18:30:12'),
(35, 'pbkdf2_sha256$20000$6LPseejfU81F$rUgyWsDxuzmntl1BJVXI7eHN91sQjZCiRCzeJDsx+WM=', NULL, 0, 'comercianteuno@comerciante.com', '', '', 'comercianteuno@comerciante.com', 0, 1, '2016-01-22 21:33:55'),
(36, 'pbkdf2_sha256$20000$ROwu5xnUyZXs$HuJX2kNCAU//O/rpjef7/rfdHcH7B7ktNITsUhgklmY=', NULL, 0, 'empresariodos@empresario.com', '', '', 'empresariodos@empresario.com', 0, 1, '2016-01-25 02:34:29'),
(37, 'pbkdf2_sha256$20000$XMgSE08heUxR$HHeNbVQAIhAPnJzY1J5kZKd0L1Mf0GLqEweC1UK9EG8=', NULL, 0, 'joaquin@jmail.com', '', '', 'joaquin@jmail.com', 0, 1, '2016-01-25 04:09:59'),
(38, 'pbkdf2_sha256$20000$JO2wVgia5FYc$wLO+rXaODoMQmCaHQMCV2g58PisWTvTmcah8683GtpU=', NULL, 0, 'disenadordos@disenador.com', '', '', 'disenadordos@disenador.com', 0, 1, '2016-01-25 19:00:43'),
(39, 'pbkdf2_sha256$20000$tzdEGMrc7tQr$Wab5OG20VUHiAgvsxPBOPtjgilcpd0v2h/1OwuGL0ME=', NULL, 0, 'dayanalejo@d.com', '', '', 'dayanalejo@d.com', 0, 1, '2016-01-25 19:38:00'),
(40, 'pbkdf2_sha256$20000$2BHs3uCJWqoQ$VwAApGlsVjMKhcQagFhLDgv5AJ0DCDHjlB8ne9VMnFE=', NULL, 0, 'Oeromeroc@Unal.edu.co', '', '', 'Oeromeroc@Unal.edu.co', 0, 1, '2016-01-25 21:06:10');

--
-- Volcado de datos para la tabla `plataforma_conversacion`
--

INSERT INTO `plataforma_conversacion` (`id`, `busqueda_id`, `respuesta_id`) VALUES
(1, 159, 157),
(2, 161, 160),
(3, 162, 157),
(4, 163, 157),
(5, 165, 156),
(6, 166, 161),
(7, 169, 156),
(8, 172, 171),
(9, 173, 172),
(10, 174, 157),
(11, 175, 166),
(12, 177, 176),
(13, 178, 166),
(14, 179, 157),
(15, 180, 157),
(16, 181, 166),
(17, 181, 157),
(18, 182, 158),
(19, 183, 163),
(20, 184, 161),
(21, 185, 184),
(22, 185, 160),
(23, 185, 185),
(24, 185, 166),
(25, 186, 166),
(26, 186, 186),
(27, 186, 185),
(28, 185, 157),
(29, 188, 176),
(30, 188, 170),
(31, 188, 160),
(32, 190, 156),
(33, 192, 176),
(34, 193, 168),
(35, 193, 161);

--
-- Volcado de datos para la tabla `plataforma_mensaje`
--

INSERT INTO `plataforma_mensaje` (`id`, `mensaje`, `fecha`, `destinatario_id`, `usuario_busqueda_id`, `usuario_respuesta_id`, `visto`, `conversacion_id`) VALUES
(1, 'Luis Francisco López Segura', '2015-11-20 02:12:34', 27, 25, 27, 0, 1),
(2, 'Luis F Lópz', '2015-11-20 02:26:40', 28, 25, 28, 0, 2),
(3, 'Andres galindo', '2015-11-20 02:45:11', 25, 25, 28, 0, 2),
(4, 'Respuesta a mensaje', '2015-11-20 03:05:16', 28, 25, 28, 0, 2),
(5, 'Sigo respondiendo', '2015-11-20 03:05:28', 28, 25, 28, 0, 2),
(6, 'Muchas Gracias', '2015-11-20 03:05:37', 25, 25, 28, 0, 2),
(7, 'Pacho Lopez', '2015-11-20 03:28:00', 28, 25, 28, 0, 2),
(8, 'Luis kuis luis luis', '2015-11-20 14:06:11', 28, 25, 28, 0, 2),
(9, 'Nueva Conexión con las personas', '2015-11-20 15:02:06', 27, 29, 27, 0, 3),
(10, 'hola', '2015-11-23 02:26:04', 28, 25, 28, 0, 2),
(11, 'hola', '2015-11-23 02:26:05', 28, 25, 28, 0, 2),
(12, 'hola', '2015-11-23 02:26:06', 28, 25, 28, 0, 2),
(13, 'hola', '2015-11-23 02:26:07', 28, 25, 28, 0, 2),
(14, 'hola', '2015-11-23 02:26:07', 28, 25, 28, 0, 2),
(15, 'hola', '2015-11-23 02:26:07', 28, 25, 28, 0, 2),
(16, 'hola', '2015-11-23 02:26:08', 28, 25, 28, 0, 2),
(17, 'hola', '2015-11-23 02:26:09', 28, 25, 28, 0, 2),
(18, 'hola', '2015-11-23 02:26:10', 28, 25, 28, 0, 2),
(19, 'hola', '2015-11-23 02:26:40', 28, 25, 28, 0, 2),
(20, 'Buenas tardes, estoy interesado en una página web para mi negocio, estoy ubicado en Girardot y me gustaría que hablaramos en persona', '2015-11-23 02:32:14', 27, 25, 27, 0, 1),
(21, 'Sí, claro. Dígame como le podemos ayudar. Hacemos páginas web desde 350 mil pesos y ofrecemos todos los servicios como hosting y correos electrónicos', '2015-11-23 02:37:13', 25, 25, 27, 0, 1),
(22, 'Nuevo', '2015-11-30 16:02:53', 27, 27, 27, 0, 4),
(23, 'Nuevo', '2015-11-30 16:02:54', 27, 27, 27, 0, 4),
(24, 'Nuevo', '2015-11-30 16:02:59', 27, 27, 27, 0, 4),
(25, 'Luis francisco', '2015-12-02 02:18:16', 28, 25, 28, 0, 2),
(26, 'Adres', '2015-12-02 02:20:35', 25, 25, 28, 0, 2),
(27, 'Prueba Nueva', '2015-12-02 02:32:42', 28, 25, 28, 0, 2),
(28, 'Muchas gracias...', '2015-12-02 03:05:45', 27, 25, 27, 0, 1),
(29, 'Mucho gusto mi nombre es Andres', '2015-12-02 03:12:44', 25, 28, 25, 0, 6),
(30, 'Luis Francisco López', '2015-12-02 03:34:00', 27, 25, 27, 0, 7),
(31, 'gadsdsfasdfasdf', '2015-12-04 16:54:53', 36, 37, 36, 0, 8),
(32, 'nhdyervervfjdyjyjsrjrtjyjyttyjtyjtyjtjtyjytjdgfbgbs', '2015-12-04 16:55:13', 36, 37, 36, 0, 8),
(33, 'hw', '2015-12-04 16:55:20', 36, 37, 36, 0, 8),
(34, 'dsddasagadfas', '2015-12-04 16:57:01', 37, 37, 36, 0, 8),
(35, 'fgfdsfgsd', '2015-12-04 16:57:16', 37, 37, 36, 0, 8),
(36, 'adasfasfas', '2015-12-04 16:57:59', 36, 37, 36, 0, 8),
(37, 'Escribo un mensaje al usuario', '2015-12-06 05:04:29', 37, 25, 37, 0, 9),
(38, 'adldasfadñfjasñdfsadj', '2015-12-06 05:13:42', 27, 25, 27, 0, 7),
(39, 'Pancks', '2015-12-07 12:30:07', 28, 38, 28, 0, 11),
(40, 'Mucho gusto me gustaría contactarilo', '2015-12-07 13:35:16', 40, 39, 40, 0, 12),
(41, 'Hola que tal soy Francisco cuentame como te puedo ayudar', '2015-12-07 13:37:10', 39, 39, 40, 0, 12),
(42, 'Necesito poder poner la información de mi negocio en mi página web pero la tengo desactualizada', '2015-12-07 13:38:30', 40, 39, 40, 0, 12),
(43, 'Hola buenos días, mi nombre es Jacinto estoy interesado en Servidores para mi negocio', '2015-12-07 15:25:25', 28, 41, 28, 0, 13),
(44, 'Buenas', '2015-12-07 15:29:05', 27, 25, 27, 0, 1),
(45, 'Buenas tardes, estoy interesado en alguno de los productos que ofrece, quisiera saber si nos podemos ver para cotizar la instalación y todo el sistema en funcionamentos, quedo atento, gracias!', '2015-12-11 14:28:26', 27, 42, 27, 0, 14),
(46, 'Buenos dias estoy interesado en equipos para mi tienda, quiero saber precios y disponibilidad', '2015-12-11 16:42:26', 27, 43, 27, 0, 15),
(47, 'Buen día, quisiera cotizar el servicio de página web para mi comercio', '2015-12-14 15:40:37', 27, 42, 27, 0, 17),
(48, 'ghfh', '2016-01-20 20:02:17', 25, 47, 25, 0, 18),
(49, 'sdf', '2016-01-21 18:06:28', 27, 51, 27, 0, 19),
(50, 'asdasd', '2016-01-22 18:34:15', 25, 47, 25, 0, 20),
(51, 'mensaje para usuario', '2016-01-22 19:01:55', 47, 48, 47, 0, 21),
(52, 'afafdsf', '2016-01-22 19:02:56', 48, 48, 47, 0, 21),
(53, 'ss', '2016-01-22 19:03:56', 47, 48, 47, 0, 21),
(54, 'rrr', '2016-01-22 19:04:30', 48, 48, 47, 0, 21),
(55, 'rrr', '2016-01-22 19:04:31', 48, 48, 47, 0, 21),
(56, 'asdasd', '2016-01-22 19:06:45', 25, 47, 25, 0, 18),
(57, 'Mensaje del empresario', '2016-01-22 19:20:25', 28, 48, 28, 0, 22),
(58, 'Mensaje del empresario', '2016-01-22 19:20:29', 28, 48, 28, 0, 22),
(59, 'yutuy', '2016-01-22 19:27:30', 48, 48, 28, 0, 22),
(60, 'asdasdasdasd', '2016-01-22 19:29:38', 48, 48, 47, 0, 21),
(61, 'MENSAJE DEL ARTESANO', '2016-01-22 19:29:55', 48, 48, 47, 0, 21),
(62, 'esto es para andres', '2016-01-22 21:43:15', 28, 57, 28, 0, 25),
(63, 'adsasd', '2016-01-22 21:45:49', 57, 57, 57, 0, 26),
(64, 'Hola', '2016-01-25 02:33:15', 27, 48, 27, 0, 28),
(65, 'otro usuario', '2016-01-25 02:34:53', 48, 48, 27, 0, 28),
(66, 'BUSQUEDA DE PROGRAMADOR OFRECE', '2016-01-25 03:15:02', 40, 58, 40, 0, 29),
(67, 'fffff', '2016-01-25 18:57:36', 27, 48, 27, 0, 32),
(68, 'das', '2016-01-25 20:27:46', 25, 53, 25, 0, 35);

--
-- Volcado de datos para la tabla `plataforma_problemasolucion`
--

INSERT INTO `plataforma_problemasolucion` (`id`, `titulo`, `descripcion`, `fecha`, `usuario_id`, `tipo`, `respuestas_cuestionario`) VALUES
(156, 'Equipos, servidores computadores', 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 27, 'S', '{6: (73, 1), 15: [(93, 1), (60, 2), (61, 3), (62, 4)]}'),
(157, 'Ofrezco venta en línea', 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 27, 'S', '{5: (21, 4), 4: (94, (4.87277777777778, -74.1444444444444)), 21: (92, 3), 6: (124, 7), 23: [(106, 1), (108, 2), (110, 3)]}'),
(158, 'Búsqueda Página Web', 'Presupuesto 500 mil y 1 Millón de pesos', '2015-11-19 20:25:17', 25, 'P', '{1: (44, 7), 3: (8, 3), 4: (10, (4.80944444444444, -74.0980555555556)), 14: (57, 1)}'),
(159, 'Mantenimiento de redes', 'Girardot', '2015-11-20 02:05:17', 25, 'P', '{1: (40, 3), 10: (43, 6), 3: (8, 3), 4: (98, (4.29861111111111, -74.8047222222222)), 13: [(56, 3)]}'),
(160, 'Ofrezco Servicios Diseño', 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 28, 'S', '{17: (76, 4), 18: (80, 1), 4: (98, (4.29861111111111, -74.8047222222222)), 5: (19, 2), 6: (75, 3)}'),
(161, 'Equipos Prueba', 'Conexiones', '2015-11-20 02:25:36', 25, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (7, 2), 4: (12, (4.85888888888889, -74.0586111111111))}'),
(162, 'Búsqueda de Equipos', 'Busco Servidores en COTA', '2015-11-20 15:01:15', 29, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (6, 1), 4: (10, (4.80944444444444, -74.0980555555556))}'),
(163, 'T', 'D', '2015-11-30 16:02:24', 27, 'P', '{8: [(25, 3)], 1: (38, 1), 3: (8, 3), 4: (11, (4.70583333333333, -74.2302777777778))}'),
(164, 'Nueva Búsqueda', 'Descripción Nuevas', '2015-12-02 03:06:26', 25, 'P', '{8: [(23, 1), (26, 4)], 1: (38, 1), 3: (6, 1), 4: (10, (4.80944444444444, -74.0980555555556))}'),
(165, 'Busq. 3', 'adasfadsfdfgfgsd', '2015-12-02 03:10:30', 25, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (6, 1), 4: (10, (4.80944444444444, -74.0980555555556))}'),
(166, 'Andres Busca', 'Cota/Programas Facturación', '2015-12-02 03:12:26', 28, 'S', '{16: [(70, 3)], 4: (10, (4.80944444444444, -74.0980555555556)), 5: (19, 2), 6: (74, 2)}'),
(167, 'bbbb', 'bbbbb', '2015-12-02 03:25:39', 25, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (6, 1)}'),
(168, 'Luis Lopez', 'Describe', '2015-12-02 03:29:56', 25, 'P', '{1: (39, 2), 3: (7, 2), 9: [(35, 3)]}'),
(169, 'Nueva sin guardar', 'Debe crear el proceso desde 0', '2015-12-02 03:33:48', 25, 'P', '{8: [(24, 2)], 1: (38, 1), 4: (11, (4.70583333333333, -74.2302777777778))}'),
(170, 'Nueva', 'Nueva', '2015-12-04 16:30:42', 33, 'S', '{17: (76, 4), 18: (80, 1), 4: (11, (4.70583333333333, -74.2302777777778)), 5: (120, 5), 6: (75, 3)}'),
(171, 'Nueva Comercio', '1 1 1 ', '2015-12-04 16:48:48', 36, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (6, 1), 4: (10, (4.80944444444444, -74.0980555555556))}'),
(172, 'Busq. 3', '222', '2015-12-04 16:54:48', 37, 'S', '{4: (10, (4.80944444444444, -74.0980555555556)), 5: (18, 1), 6: (73, 1), 15: [(93, 1)]}'),
(173, 'Pacho', 'Lopez', '2015-12-06 05:04:15', 25, 'P', '{8: [(23, 1), (25, 3)], 1: (38, 1), 3: (7, 2), 4: (12, (4.85888888888889, -74.0586111111111))}'),
(174, 'dfasdf', 'sfsdf', '2015-12-06 05:28:04', 25, 'P', '{8: [(23, 1), (25, 3)], 1: (38, 1), 3: (9, 4), 4: (11, (4.70583333333333, -74.2302777777778))}'),
(175, 'Jddjs', 'Bxjenbtv', '2015-12-07 12:29:52', 38, 'P', '{1: (44, 7), 3: (6, 1), 4: (98, (4.29861111111111, -74.8047222222222)), 14: (57, 1)}'),
(176, 'Programador Ofrece', 'Servicios de Capacitación en manejo de programas', '2015-12-07 13:28:01', 40, 'S', '{1: (40, 3), 10: (42, 5), 3: (8, 3), 12: [(51, 1)], 4: (96, (4.92611111111111, -74.1730555555556))}'),
(177, 'Empresario Busca', 'Servicios de Capacitación', '2015-12-07 13:34:43', 39, 'P', '{1: (40, 3), 10: (42, 5), 3: (8, 3), 12: [(51, 1)], 4: (96, (4.92611111111111, -74.1730555555556))}'),
(178, 'Búsqueda Comercio', 'Estoy buscando servidores ', '2015-12-07 15:24:30', 41, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (119, 5), 4: (96, (4.92611111111111, -74.1730555555556))}'),
(179, 'Búsqueda equipos para oficina', 'Esta búsqueda está enfocada a los equipos de oficina que necesitamos para nuestra nueva sede en Cajicá', '2015-12-11 14:24:30', 42, 'P', '{8: [(25, 3), (26, 4)], 1: (38, 1), 3: (8, 3), 4: (95, (4.91861111111111, -74.0280555555556))}'),
(180, 'Equipos para la tienda en la cra 10', 'Punto de pago y tablets para los vendedores', '2015-12-11 16:40:21', 43, 'P', '{1: (44, 7), 3: (8, 3), 4: (96, (4.92611111111111, -74.1730555555556)), 14: (57, 1)}'),
(181, 'Pagina Web para mi comercio', 'Cotización de página web sencilla', '2015-12-14 15:37:07', 42, 'P', '{1: (44, 7), 3: (8, 3), 4: (98, (4.29861111111111, -74.8047222222222)), 14: (57, 1)}'),
(182, 'guardarbusqueda', 'D guardarbusqueda', '2016-01-20 20:01:04', 47, 'S', '{4: (11, (4.70583333333333, -74.2302777777778)), 21: (90, 1), 6: (124, 7), 5: (20, 3)}'),
(183, 'df', 'sdf', '2016-01-21 18:06:24', 51, 'S', '{4: (11, (4.70583333333333, -74.2302777777778))}'),
(184, 'eeeee', 'eeeee', '2016-01-22 18:34:09', 47, 'S', '{4: (11, (4.70583333333333, -74.2302777777778)), 5: (19, 2)}'),
(185, 'guardar busqueda empresario', 'guardar busqueda empresario', '2016-01-22 19:01:42', 48, 'P', '{1: (44, 7), 3: (7, 2), 4: (11, (4.70583333333333, -74.2302777777778)), 14: (57, 1)}'),
(186, 'INTENET PARA MI EMPRESA', 'INTENET PARA MI EMPRESA COMERCIANTE', '2016-01-22 21:41:37', 57, 'P', '{1: (44, 7), 3: (7, 2), 4: (11, (4.70583333333333, -74.2302777777778)), 14: (57, 1)}'),
(187, 'Busqueda de empresario', 'Empresario', '2016-01-25 02:45:57', 58, 'P', '{1: (39, 2), 3: (7, 2), 4: (11, (4.70583333333333, -74.2302777777778)), 9: [(36, 4)]}'),
(188, 'BUSQUEDA DE PROGRAMADOR OFRECE', 'BUSQUEDA DE PROGRAMADOR OFRECEBUSQUEDA DE PROGRAMADOR OFRECE', '2016-01-25 03:14:51', 58, 'P', '{4: (12, (4.85888888888889, -74.0586111111111))}'),
(189, 'usuario no registrado', 'dddddd', '2016-01-25 18:51:01', 48, 'P', '{8: [(23, 1)], 1: (38, 1), 4: (11, (4.70583333333333, -74.2302777777778))}'),
(190, 'Necesito servidores', 'Equipos servidores computadores', '2016-01-25 18:57:28', 48, 'P', '{8: [(23, 1)], 1: (38, 1), 3: (7, 2), 4: (11, (4.70583333333333, -74.2302777777778))}'),
(191, 'busqueda', 'ssss', '2016-01-25 19:10:37', 60, 'S', '{4: (11, (4.70583333333333, -74.2302777777778)), 5: (19, 2)}'),
(192, 'Busqueda 25', 'Busqueda 25', '2016-01-25 19:52:09', 48, 'P', '{4: (11, (4.70583333333333, -74.2302777777778))}'),
(193, 'sda', 'asd', '2016-01-25 20:23:23', 53, 'S', '{5: (19, 2)}');

--
--

--
-- Volcado de datos para la tabla `plataforma_respuestaproblemasolucion`
--

INSERT INTO `plataforma_respuestaproblemasolucion` (`id`, `busqueda_id`, `respuesta_id`, `descripcion`, `fecha`, `tipo`, `titulo`) VALUES
(1, 158, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(2, 159, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(3, 161, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(4, 162, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(5, 163, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(6, 164, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(7, 165, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(8, 166, 161, 'Conexiones', '2015-11-20 02:25:36', 'P', 'Equipos Prueba'),
(9, 167, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(10, 169, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(11, 172, 171, '1 1 1 ', '2015-12-04 16:48:48', 'P', 'Nueva Comercio'),
(12, 173, 172, '222', '2015-12-04 16:54:48', 'S', 'Busq. 3'),
(13, 169, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(14, 174, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(15, 175, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(16, 177, 176, 'Servicios de Capacitación en manejo de programas', '2015-12-07 13:28:01', 'S', 'Programador Ofrece'),
(17, 178, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(18, 179, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(19, 179, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(20, 180, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(21, 181, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(22, 181, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(23, 181, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(24, 181, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(25, 182, 158, 'Presupuesto 500 mil y 1 Millón de pesos', '2015-11-19 20:25:17', 'P', 'Búsqueda Página Web'),
(26, 183, 163, 'D', '2015-11-30 16:02:24', 'P', 'T'),
(27, 184, 161, 'Conexiones', '2015-11-20 02:25:36', 'P', 'Equipos Prueba'),
(28, 185, 184, 'eeeee', '2016-01-22 18:34:09', 'S', 'eeeee'),
(29, 185, 184, 'eeeee', '2016-01-22 18:34:09', 'S', 'eeeee'),
(30, 185, 184, 'eeeee', '2016-01-22 18:34:09', 'S', 'eeeee'),
(31, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(32, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(33, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(34, 185, 185, 'guardar busqueda empresario', '2016-01-22 19:01:42', 'P', 'guardar busqueda empresario'),
(35, 185, 185, 'guardar busqueda empresario', '2016-01-22 19:01:42', 'P', 'guardar busqueda empresario'),
(36, 185, 182, 'D guardarbusqueda', '2016-01-20 20:01:04', 'S', 'guardarbusqueda'),
(37, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(38, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(39, 185, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(40, 185, 184, 'eeeee', '2016-01-22 18:34:09', 'S', 'eeeee'),
(41, 185, 184, 'eeeee', '2016-01-22 18:34:09', 'S', 'eeeee'),
(42, 185, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(43, 185, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(44, 186, 166, 'Cota/Programas Facturación', '2015-12-02 03:12:26', 'S', 'Andres Busca'),
(45, 186, 186, 'INTENET PARA MI EMPRESA COMERCIANTE', '2016-01-22 21:41:37', 'P', 'INTENET PARA MI EMPRESA'),
(46, 186, 185, 'guardar busqueda empresario', '2016-01-22 19:01:42', 'P', 'guardar busqueda empresario'),
(47, 186, 185, 'guardar busqueda empresario', '2016-01-22 19:01:42', 'P', 'guardar busqueda empresario'),
(48, 185, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(49, 185, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(50, 185, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(51, 185, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(52, 188, 176, 'Servicios de Capacitación en manejo de programas', '2015-12-07 13:28:01', 'S', 'Programador Ofrece'),
(53, 188, 176, 'Servicios de Capacitación en manejo de programas', '2015-12-07 13:28:01', 'S', 'Programador Ofrece'),
(54, 188, 170, 'Nueva', '2015-12-04 16:30:42', 'S', 'Nueva'),
(55, 188, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(56, 188, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(57, 187, 157, 'Asesoría en diferentes herramientas para vender su producto en internet', '2015-11-17 02:44:49', 'S', 'Ofrezco venta en línea'),
(58, 187, 160, 'Diseño de Logos en Girardot ', '2015-11-20 02:20:17', 'S', 'Ofrezco Servicios Diseño'),
(59, 189, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(60, 190, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(61, 190, 156, 'Vendo equipos de cómputo', '2015-11-17 02:34:52', 'S', 'Equipos, servidores computadores'),
(62, 190, 159, 'Girardot', '2015-11-20 02:05:17', 'P', 'Mantenimiento de redes'),
(63, 190, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(64, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(65, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(66, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(67, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(68, 191, 187, 'Empresario', '2016-01-25 02:45:57', 'P', 'Busqueda de empresario'),
(69, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(70, 191, 190, 'Equipos servidores computadores', '2016-01-25 18:57:28', 'P', 'Necesito servidores'),
(71, 192, 176, 'Servicios de Capacitación en manejo de programas', '2015-12-07 13:28:01', 'S', 'Programador Ofrece'),
(72, 192, 182, 'D guardarbusqueda', '2016-01-20 20:01:04', 'S', 'guardarbusqueda'),
(73, 192, 186, 'INTENET PARA MI EMPRESA COMERCIANTE', '2016-01-22 21:41:37', 'P', 'INTENET PARA MI EMPRESA'),
(74, 193, 168, 'Describe', '2015-12-02 03:29:56', 'P', 'Luis Lopez'),
(75, 193, 161, 'Conexiones', '2015-11-20 02:25:36', 'P', 'Equipos Prueba'),
(76, 193, 161, 'Conexiones', '2015-11-20 02:25:36', 'P', 'Equipos Prueba');

--
-- Volcado de datos para la tabla `plataforma_usuario`
--

INSERT INTO `plataforma_usuario` (`id`, `nombres`, `apellido1`, `apellido2`, `numero_documento`, `correo`, `nombre_institucion`, `telefono_institucion`, `ubicacion_institucion`, `direccion_institucion`, `NIT`, `rol_id`, `correo_institucion`, `descripcion`, `user_id`, `municipio_id`) VALUES
(1, 'Juana', 'Ramirez', 'weaver', NULL, 'camilo255423@hotmail.com', NULL, NULL, 'cota', NULL, NULL, 2, NULL, 'ninguna', 1, 11),
(23, 'Camilo', 'Rodriguez', 'Torres', '', 'rodriguez.camilo@gmail.com', '', '', '', '', '', 2, '', 'zz', 1, 11),
(24, 'pepe', 'perez', 'torres', '7777', 'perez@hotmail.com', '', '', 'cali', '', '', 3, '', 'zzz', 2, 11),
(25, 'Luis', 'Lopez', 'Segura', '1015423809', 'luispacholopez@gmail.com', 'LOPEZ', '3132596069', 'Chía', 'calle', '1235', 3, 'luispacholopez@gmail.com', 'descripción', 3, 11),
(26, 'Juan', 'perez', 'torres', NULL, 'perez@jmail.com', NULL, NULL, 'chia', NULL, NULL, 4, NULL, NULL, 4, 11),
(27, 'carlos', 'rodriguez', 'gutierrez', NULL, 'gutierrez@jmail.com', NULL, NULL, 'mosquera', NULL, NULL, 6, NULL, NULL, 5, 11),
(28, 'Andres', 'Villa', 'Villa', NULL, 'andres@mail.com', 'Comercio Don Andres', '1234', 'Chía', 'Calle 2 # 24- 32', NULL, 9, NULL, NULL, 6, 12),
(29, 'Antonio', 'Donato', 'Donato', NULL, 'donato@mail.com', 'Donato''Tic', '1234567', 'Mosquera', 'Calle Carrera -', NULL, 3, NULL, NULL, 7, 11),
(30, 'Alejandro', 'Latorre', 'Latorre', NULL, 'alatorre16@aol.com', 'Programador .JS', '9999999', 'Subachoque', 'Calle 24', NULL, 2, NULL, NULL, 8, 96),
(31, 'Pepe', 'Pepes', 'Pepes', NULL, 'luis@mail.com', 'Comercios', '12314213', 'Mosquera', 'Calle 12', NULL, 3, NULL, NULL, 9, 11),
(32, 'Nhora Paulina', 'Parra Ortiz', 'Parra Ortiz', NULL, 'npparrao@unal.edu.co', 'InTIColombia', '3194728191', 'Mosquera', 'Calle 45', NULL, 5, NULL, NULL, 10, 11),
(33, 'Nuevo', 'Nuevo', 'Nuevo', NULL, 'nuevo@mail.com', 'ComercioNuevo', '1234', 'Mosquera', 'C', NULL, 6, NULL, NULL, 11, 11),
(34, 'Turismo', 'Turismo', 'Turismo', NULL, 'turismo@mail.com', 'Tursimo', '1234', 'Mosquera', 'Calle', NULL, 7, NULL, NULL, 12, 11),
(35, 'aaa', 'aaa', 'aaa', NULL, 'aaa@aaa.com', 'aaa', '123', 'Mosquera', 'aaa', NULL, 7, NULL, NULL, 13, 11),
(36, 'Comercio', 'Busco', 'Busco', NULL, 'comercio@mail.com', 'Comercio Busco', '1234', 'Cota', 'Calle', NULL, 3, NULL, NULL, 14, 10),
(37, 'Comercio', 'Ofrezco', 'Ofrezco', NULL, 'ofrezco@mail.com', 'Ofrezco', '1234', 'Cota', 'Calle', NULL, 9, NULL, NULL, 15, 10),
(38, 'Prueba', 'Comercio safari', 'Comercio safari', NULL, 'pruebac@mail.com', 'Comercio1', '1236', 'Subachoque', 'Ca', NULL, 4, NULL, NULL, 16, 96),
(39, 'Empresario', 'Comercio', 'Comercio', NULL, 'empresario@mail.com', 'Empresario Comercio', '1234', 'Subachoque', 'Calle', NULL, 2, NULL, NULL, 17, 96),
(40, 'Programador', 'Comercio', 'Comercio', NULL, 'programador@mail.com', 'Programador Comercio', '1234', 'Subachoque', 'Calle', NULL, 9, NULL, NULL, 18, 96),
(41, 'Jacinto', 'Perez', 'Perez', NULL, 'jacinto@mail.com', 'Jacinto Comercio', '1234', 'Cajicá', 'Calle 1 2 3', NULL, 4, NULL, NULL, 19, 95),
(42, 'Martin', 'Mejía', 'Mejía', NULL, 'martinmejia2112@gmail.com', 'Mercado de Artesanías Martina', '31113997685', 'Cajicá', 'Cra.10 # 21-19 Local 101', NULL, 3, NULL, NULL, 20, 95),
(43, 'Maurcio', 'Rodriguez', 'Rodriguez', NULL, 'mauricio@longboardcolombia.com', 'Longboard colombia', '3113899588', 'Chía', 'cra 10 67-42', NULL, 3, NULL, NULL, 21, 12),
(44, 'MAURICIO', 'RODRIGUEZ', 'RODRIGUEZ', NULL, 'temp@gmail.com', 'Trixel Design', '+5715303783', 'Chía', 'Cra 10 1145', NULL, 3, NULL, NULL, 22, 12),
(45, 'Julia', 'Fonseca', 'Fonseca', NULL, 'julia@mail.com', 'Restaurante Juli', '3113899', 'Chía', '112 2110', NULL, 14, NULL, NULL, 23, 12),
(46, 'Mauricio', 'Camaho', 'Camaho', NULL, 'mauriciocamacho@gmail.com', 'Mi Comercio', '3113899588', 'Chía', 'Cra 10 # 11-45', NULL, 3, NULL, NULL, 24, 12),
(47, 'usuario', 'uno', 'uno', NULL, 'usuariouno@usuario.com', NULL, '123445', 'Mosquera', NULL, NULL, 9, NULL, NULL, 25, 11),
(48, 'Empresario', 'uno', 'uno', NULL, 'empresariouno@empresario.com', NULL, '123456', 'Mosquera', NULL, NULL, 2, NULL, NULL, 26, 11),
(49, 'agencia', 'uno', 'uno', NULL, 'agenciauno@agencia.com', NULL, '12345678', 'Chía', NULL, NULL, 7, NULL, NULL, 27, 12),
(50, 'Alex', 'Rico', 'Rico', NULL, 'misantropee@gmail.com', 'vivelab', '+573114598595', 'Mosquera', 'Cll 40 # 30 - 20', NULL, 3, NULL, NULL, 28, 11),
(51, 'Diseñador', 'diseñadoruno', 'diseñadoruno', NULL, 'disenadoruno@disenador.com', NULL, '1234567', 'Mosquera', NULL, NULL, 8, NULL, NULL, 29, 11),
(52, 'Agencia de', 'Turismo', 'Turismo', NULL, 'turismouno@turismo.com', NULL, NULL, 'Chía', NULL, NULL, 7, NULL, NULL, 30, 12),
(53, 'Dayana', 'Alejo Ordoñez', 'Alejo Ordoñez', NULL, 'dayana@alejo.com', NULL, '123456', 'Tenjo', NULL, NULL, 9, NULL, NULL, 31, 94),
(54, 'Hotelero', 'hotelerouno', 'hotelerouno', NULL, 'hotelero@hotelero.com', NULL, '123445556', 'Cajicá', NULL, NULL, 13, NULL, NULL, 32, 95),
(55, 'artesano', 'uno', 'uno', NULL, 'artesano@artesano.com', NULL, '123456', 'Tenjo', NULL, NULL, 11, NULL, NULL, 33, 94),
(56, 'Artesano uno', 'artesano apellido', 'artesano apellido', NULL, 'artesanouno@artesano.com', NULL, '123123123', 'Mosquera', NULL, NULL, 11, NULL, NULL, 34, 11),
(57, 'comerciante', 'comerciante uno', 'comerciante uno', NULL, 'comercianteuno@comerciante.com', NULL, '123123123', 'Chía', NULL, NULL, 3, NULL, NULL, 35, 12),
(58, 'Empresario DOS', 'empresariodos', 'empresariodos', NULL, 'empresariodos@empresario.com', NULL, NULL, 'Mosquera', NULL, NULL, 2, NULL, NULL, 36, 11),
(59, 'Juaquin', 'Angarita', 'Angarita', NULL, 'joaquin@jmail.com', NULL, '12222', 'Mosquera', NULL, NULL, 3, NULL, NULL, 37, 11),
(60, 'Diseñador', 'disenadordos', 'disenadordos', NULL, 'disenadordos@disenador.com', NULL, '24414', 'Mosquera', NULL, NULL, 8, NULL, NULL, 38, 11),
(61, 'nombre', 'apellido', 'apellido', NULL, 'dayanalejo@d.com', NULL, '132123', 'Mosquera', NULL, NULL, 8, NULL, NULL, 39, 11),
(62, 'Oscar', 'Romero', 'Romero', NULL, 'Oeromeroc@Unal.edu.co', NULL, NULL, 'Tenjo', NULL, NULL, 8, NULL, NULL, 40, 94);

--
-- Volcado de datos para la tabla `plataforma_usuarioredes`
--

INSERT INTO `plataforma_usuarioredes` (`id`, `url`, `red_social_id`, `usuario_id`) VALUES
(1, '', 1, 1);
SET FOREIGN_KEY_CHECKS=1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
