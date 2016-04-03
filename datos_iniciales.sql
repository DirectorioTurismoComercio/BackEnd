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
-- Volcado de datos para la tabla `plataforma_cuestionario`
--

INSERT INTO `plataforma_cuestionario` (`id`, `titulo`, `descripcion`, `fecha`, `imagen`) VALUES
(1, '¿Qué buscas?', NULL, '0000-00-00 00:00:00', 'boton-que.png'),
(2, '¿Cuál es tu presupuesto?', NULL, '0000-00-00 00:00:00', 'boton-cuanto.png'),
(3, '¿Dónde te encuentras?', NULL, '0000-00-00 00:00:00', 'boton-donde.png'),
(4, '¿Qué productos o servicios ofreces?', NULL, '0000-00-00 00:00:00', 'boton-que.png'),
(5, '¿Cuánto cobras?', NULL, '0000-00-00 00:00:00', 'boton-cuanto.png'),
(6, 'Áreas de interés', NULL, '0000-00-00 00:00:00', 'boton-que.png');

--
-- Volcado de datos para la tabla `plataforma_cuestionariopregunta`
--

INSERT INTO `plataforma_cuestionariopregunta` (`id`, `orden`, `cuestionario_id`, `pregunta_id`) VALUES
(5, 1, 1, 1),
(6, 8, 1, 2),
(7, 0, 2, 3),
(8, 0, 3, 4),
(9, 0, 5, 5),
(12, 0, 4, 6),
(13, 10, 4, 7),
(14, 1, 1, 8),
(15, 2, 1, 9),
(16, 3, 1, 10),
(17, 4, 1, 11),
(18, 5, 1, 12),
(19, 6, 1, 13),
(20, 7, 1, 14),
(21, 1, 4, 15),
(22, 2, 4, 16),
(23, 3, 4, 17),
(24, 4, 4, 18),
(25, 5, 4, 19),
(26, 6, 4, 20),
(27, 7, 4, 21),
(28, 12, 1, 24),
(29, 12, 4, 25),
(30, 13, 1, 22),
(31, 13, 4, 23),
(32, 7, 1, 26),
(33, 2, 6, 27);

--
-- Volcado de datos para la tabla `plataforma_cuestionariopregunta_dependencia_respuestas`
--

INSERT INTO `plataforma_cuestionariopregunta_dependencia_respuestas` (`id`, `cuestionariopregunta_id`, `opcionesderespuesta_id`) VALUES
(13, 6, 123),
(5, 13, 16),
(6, 14, 38),
(7, 15, 39),
(8, 16, 40),
(9, 17, 41),
(10, 18, 42),
(11, 19, 43),
(12, 20, 44),
(16, 21, 73),
(20, 22, 74),
(17, 23, 75),
(18, 24, 76),
(27, 25, 78),
(19, 26, 77),
(14, 27, 124),
(30, 28, 101),
(39, 29, 102),
(42, 30, 59),
(43, 31, 92),
(46, 32, 163);

--
-- Volcado de datos para la tabla `plataforma_cuestionariorol`
--

INSERT INTO `plataforma_cuestionariorol` (`id`, `tipo`, `cuestionario_id`, `rol_id`, `orden`) VALUES
(1, 'P', 1, 3, 0),
(2, 'P', 2, 3, 0),
(3, 'P', 3, 3, 0),
(4, 'P', 1, 2, 0),
(5, 'P', 2, 2, 0),
(6, 'P', 3, 2, 0),
(7, 'P', 1, 4, 0),
(8, 'P', 2, 4, 0),
(9, 'P', 3, 4, 0),
(10, 'S', 6, 5, 0),
(12, 'S', 3, 5, 0),
(13, 'S', 4, 6, 0),
(14, 'S', 5, 6, 0),
(15, 'S', 3, 6, 0),
(16, 'P', 1, 7, 0),
(17, 'P', 2, 7, 0),
(18, 'P', 3, 7, 0),
(19, 'S', 4, 8, 0),
(20, 'S', 5, 8, 0),
(21, 'S', 3, 8, 0),
(22, 'S', 4, 9, 0),
(23, 'S', 5, 9, 0),
(24, 'S', 3, 9, 0);

--
-- Volcado de datos para la tabla `plataforma_opcionesderespuesta`
--

INSERT INTO `plataforma_opcionesderespuesta` (`id`, `respuesta`, `orden`, `valor`, `pregunta_id`) VALUES
(1, 'Facebook', 2, '1', 2),
(2, 'Twitter', 3, '2', 2),
(3, 'Instagram', 1, '3', 2),
(6, 'Menos de $100.000', 1, '1', 3),
(7, 'Entre $100.000 a $500.000', 2, '2', 3),
(8, 'Entre $500.000 y $1.000.000', 3, '3', 3),
(9, 'Entre $1.000.000 y $5.000.000', 4, '4', 3),
(10, 'Cota', 6, '(4.80944444444444,-74.0980555555556)\r\n', 4),
(11, 'Mosquera', 16, '(4.70583333333333,-74.2302777777778)\r\n', 4),
(12, 'Chía', 3, '(4.85888888888889,-74.0586111111111)\r\n', 4),
(13, 'Facebook', 1, '1', 7),
(14, 'Twitter', 2, '2', 7),
(15, 'Instagram', 3, '3', 7),
(16, 'Redes Sociales', 5, '5', 21),
(18, 'Menos de $100.000', 1, '1', 5),
(19, 'Entre $100.000 a $500.000', 2, '2', 5),
(20, 'Entre $500.000 y $1.000.000', 3, '3', 5),
(21, 'Entre $1.000.000 y $5.000.000', 4, '4', 5),
(23, 'Servidores', 1, '1', 8),
(24, 'Dispositivos de redes', 2, '2', 8),
(25, 'Portátiles', 3, '3', 8),
(26, 'Equipos de Escritorio', 4, '4', 8),
(27, 'Tabletas', 5, '5', 8),
(28, 'Teléfonos Inteligenes', 6, '6', 8),
(29, 'Impresoras', 7, '7', 8),
(30, 'Sistemas para puntos de pago', 8, '8', 8),
(31, 'Sistemas de vigilancia con cámaras', 9, '9', 8),
(32, 'Videojuegos', 11, '1', 9),
(34, 'Programas contables y administrativos', 2, '2', 9),
(35, 'Programas de Facturación', 3, '3', 9),
(36, 'Programas personalizados', 4, '4', 9),
(37, 'Programas de Oficina', 5, '5', 9),
(38, 'Equipos', 1, '1', 1),
(39, 'Programas', 2, '2', 1),
(40, 'Servicios', 3, '3', 1),
(41, 'Diseño', 4, '4', 10),
(42, 'Capacitación', 5, '5', 10),
(43, 'Mantenimiento', 6, '6', 10),
(44, 'Internet', 7, '7', 1),
(47, 'Diseño de logos', 1, '1', 11),
(48, 'Identidad corporativa', 2, '2', 11),
(49, 'Material Publicitario', 3, '3', 11),
(50, 'Fotografía y Video', 4, '4', 11),
(51, 'Manejo de programas', 1, '1', 12),
(52, 'Manejo de Equipos', 2, '2', 12),
(53, 'Manejo de Redes Sociales', 3, '3', 12),
(54, 'Mantenimiento de Páginas Web', 1, '1', 13),
(55, 'Mantenimiento de Equipos', 2, '2', 13),
(56, 'Mantenimiento de redes', 3, '3', 13),
(57, 'Páginas WEB', 1, '1', 14),
(58, 'Herramientas de posicionamiento', 2, '2', 14),
(59, 'Venta en Línea', 3, '3', 14),
(60, 'Dispositivos de redes', 2, '2', 15),
(61, 'Portátiles', 3, '3', 15),
(62, 'Equipos de Escritorio', 4, '4', 15),
(63, 'Tabletas', 5, '5', 15),
(64, 'Teléfonos Inteligenes', 6, '6', 15),
(65, 'Impresoras', 7, '7', 15),
(66, 'Sistemas para puntos de pago', 8, '8', 15),
(67, 'Sistemas de vigilancia con cámaras', 9, '9', 15),
(68, 'Videojuegos', 11, '1', 16),
(69, 'Programas contables y administrativos', 2, '2', 16),
(70, 'Programas de Facturación', 3, '3', 16),
(71, 'Programas personalizados', 4, '4', 16),
(72, 'Programas de Oficina', 5, '5', 16),
(73, 'Equipos', 1, '1', 6),
(74, 'Programas', 2, '2', 6),
(75, 'Servicios', 3, '3', 6),
(76, 'Diseño', 4, '4', 17),
(77, 'Capacitación', 5, '5', 17),
(78, 'Mantenimiento', 6, '6', 17),
(79, 'Internet', 7, '7', 17),
(80, 'Diseño de logos', 1, '1', 18),
(81, 'Identidad corporativa', 2, '2', 18),
(82, 'Material Publicitario', 3, '3', 18),
(83, 'Fotografía y Video', 4, '4', 18),
(84, 'Manejo de programas', 1, '1', 19),
(85, 'Manejo de Equipos', 2, '2', 19),
(86, 'Manejo de Redes Sociales', 3, '3', 19),
(87, 'Mantenimiento de Páginas Web', 1, '1', 20),
(88, 'Mantenimiento de Equipos', 2, '2', 20),
(89, 'Mantenimiento de redes', 3, '3', 20),
(90, 'Páginas WEB', 1, '1', 21),
(91, 'Herramientas de posicionamiento', 2, '2', 21),
(92, 'Venta en Línea', 3, '3', 21),
(93, 'Servidores', 1, '1', 15),
(94, 'Tenjo', 4, '(4.87277777777778,-74.1444444444444)\r\n', 4),
(95, 'Cajicá', 2, '(4.91861111111111,-74.0280555555556)\r\n', 4),
(96, 'Subachoque', 6, '(4.92611111111111,-74.1730555555556)\r\n', 4),
(97, 'Tabio', 7, '(4.91722222222222,-74.0936111111111)\r\n', 4),
(98, 'Girardot', 13, '(4.29861111111111,-74.8047222222222)\r\n', 4),
(99, 'Programas Sector Hotelero', 6, '6', 16),
(100, 'Programas para Restaurantes', 7, '7', 16),
(101, 'Publicidad en Internet', 4, '4', 14),
(102, 'Publicidad en Internet', 4, '4', 21),
(103, 'Diseño de Aplicaciones Móviles', 5, '5', 14),
(104, 'Diseño de Aplicaciones Móviles', 4, '4', 21),
(105, 'Carrito de compras', 1, '1', 22),
(106, 'Carrito de compras', 1, '1', 23),
(107, 'Mercado Libre', 2, '2', 22),
(108, 'Mercado Libre', 2, '2', 23),
(109, 'OXL', 3, '3', 22),
(110, 'OXL', 3, '3', 23),
(111, 'Wallapop', 4, '4', 22),
(112, 'Wallapop', 4, '4', 23),
(113, 'TriVago', 5, '5', 22),
(114, 'Trivago', 5, '5', 23),
(115, 'Despegar', 6, '6', 22),
(116, 'Despegar', 6, '6', 23),
(117, 'Trip Advisor', 7, '7', 22),
(118, 'Trip Advisor', 7, '7', 23),
(119, 'Mas de $5.000.000', 5, '5', 3),
(120, 'Mas de $5.000.000', 5, '5', 5),
(121, 'Programas Sector Hotelero', 6, '6', 9),
(122, 'Programas para Restaurantes', 7, '7', 9),
(123, 'Redes Sociales', 5, '5', 14),
(124, 'Producto o Servicio en Internet', 4, '7', 6),
(125, 'Google Ads', 1, '1', 24),
(126, 'Google Ads', 1, '1', 25),
(127, 'Facebook Ads', 2, '2', 24),
(128, 'Facebook Ads', 2, '2', 25),
(129, 'Youtube Ads', 3, '3', 24),
(130, 'Youtube Ads', 3, '3', 25),
(131, 'Bogota', 1, '(4.63083333333333,-74.0866666666667)', 4),
(132, 'Boita', 2, '(5.02416666666667,-73.8355555555556)', 4),
(133, 'Caqueza', 3, '(4.40555555555556,-73.9469444444445)', 4),
(134, 'Chipaque', 4, '(4.4425,-74.0441666666667)', 4),
(135, 'Choachi', 5, '(4.52888888888889,-73.9227777777778)', 4),
(136, 'Cogua', 6, '(5.06055555555556,-73.9791666666667)', 4),
(137, 'El Rosal', 7, '(4.85305555555556,-74.26)', 4),
(138, 'Facatativa', 8, '(4.81361111111111,-74.3544444444444)', 4),
(139, 'Fomeque', 9, '(4.48805555555556,-73.8975)', 4),
(140, 'Fosca', 10, '(4.33916666666667,-73.9386111111111)', 4),
(141, 'Funza', 11, '(4.71638888888889,-74.2119444444444)', 4),
(142, 'Fusagasuga', 12, '(4.33638888888889,-74.3638888888889)', 4),
(143, 'Gachancipa', 13, '(4.99111111111111,-73.8716666666667)', 4),
(144, 'Guayabetal', 14, '(4.21472222222222,-73.8172222222222)', 4),
(145, 'Las Vegas', 15, '(5.06138888888889,-73.8222222222222)', 4),
(146, 'Madrid', 16, '(4.7325,-74.2641666666667)', 4),
(147, 'Nemocon', 17, '(5.05,-73.8833333333333)', 4),
(148, 'Nilo', 18, '(4.30611111111111,-74.6208333333333)', 4),
(149, 'Nimaima', 19, '(5.12611111111111,-74.385)', 4),
(150, 'Nocaima', 20, '(5.06972222222222,-74.3780555555555)', 4),
(151, 'Pacho', 21, '(5.13277777777778,-74.1597222222222)', 4),
(152, 'Quetame', 22, '(4.33222222222222,-73.8613888888889)', 4),
(153, 'San Antonio del Tequendama', 23, '(4.61888888888889,-74.3538888888889)', 4),
(154, 'San Francisco', 24, '(4.61666666666667,-74.8)', 4),
(155, 'Sibate', 25, '(4.48416666666667,-74.245)', 4),
(156, 'Soacha', 26, '(4.57944444444444,-74.2169444444445)', 4),
(157, 'Sopo', 27, '(4.9075,-73.9383333333333)', 4),
(158, 'Supata', 28, '(5.06083333333333,-74.2372222222222)', 4),
(159, 'Tocaima', 29, '(4.45833333333333,-74.6344444444445)', 4),
(160, 'Tocancipa', 30, '(4.96527777777778,-73.9130555555556)', 4),
(161, 'Ubate', 31, '(5.30944444444444,-73.8158333333333)', 4),
(162, 'Une', 32, '(4.40305555555556,-74.0252777777778)', 4),
(163, 'Tengo un proyecto o idea de emprendimiento.', 8, '8', 1),
(164, 'Desarrollo de Software', 1, '1', 26),
(165, 'Recursos turísticos', 2, '2', 26),
(166, 'Seguridad en la industria hotelera', 3, '3', 26),
(167, 'Estrategias de atención al cliente', 4, '4', 26),
(168, 'Turismo Gastronómico', 5, '5', 26),
(169, 'Producción de Servicios Turísticos', 6, '6', 26),
(170, 'Gestión de destinos', 7, '7', 26),
(171, 'Gestión de Empresas Turísticas', 8, '8', 26),
(172, 'Automatización de procesos', 9, '9', 26),
(173, 'Estudio de mercadeo', 10, '10', 26),
(174, 'Plan estratégico de mercadeo', 11, '11', 26),
(175, 'Diseño de puntos de venta', 12, '12', 26),
(176, 'Estrategia de visibilización', 13, '13', 26),
(177, 'Desarrollo de Software', 1, '1', 27),
(178, 'Recursos turísticos', 2, '2', 27),
(179, 'Seguridad en la industria hotelera', 3, '3', 27),
(180, 'Estrategias de atención al cliente', 4, '4', 27),
(181, 'Turismo Gastronómico', 5, '5', 27),
(182, 'Producción de Servicios Turísticos', 6, '6', 27),
(183, 'Gestión de destinos', 7, '7', 27),
(184, 'Gestión de Empresas Turísticas', 8, '8', 27),
(185, 'Automatización de procesos', 9, '9', 27),
(186, 'Estudio de mercadeo', 10, '10', 27),
(187, 'Plan estratégico de mercadeo', 11, '11', 27),
(188, 'Diseño de puntos de venta', 12, '12', 27),
(189, 'Estrategia de visibilización', 13, '13', 27);

--
-- Volcado de datos para la tabla `plataforma_pregunta`
--

INSERT INTO `plataforma_pregunta` (`id`, `enunciado`, `tipo_pregunta`, `imagen`) VALUES
(1, '¿Qué necesitas?', 'U', NULL),
(2, '¿Qué redes sociales necesitas?', 'M', NULL),
(3, '¿Cuál es tu presupuesto?', 'U', NULL),
(4, '¿Dónde estás Ubicado?', 'L', NULL),
(5, '¿Cuánto cobras?', 'U', NULL),
(6, '¿Qué producto o servicio ofreces?', 'U', NULL),
(7, '¿Qué redes sociales ofreces?', 'M', ''),
(8, '¿Qué equipos buscas?', 'M', NULL),
(9, '¿Qué programas buscas?', 'M', NULL),
(10, '¿Qué servicio necesitas?', 'U', NULL),
(11, '¿Qué tipo de diseño?', 'U', NULL),
(12, '¿Qué tipo de capacitación necesitas?', 'M', NULL),
(13, '¿Qué tipo de mantenimiento necesitas?', 'M', NULL),
(14, '¿Qué necesitas en Internet?', 'U', NULL),
(15, '¿Qué equipos ofreces?', 'M', NULL),
(16, '¿Qué tipo de programas ofreces?', 'M', NULL),
(17, '¿Qué tipo de servicios ofreces?', 'U', NULL),
(18, '¿Qué tipo de diseño ofreces?', 'U', NULL),
(19, '¿Qué tipo de mantenimiento ofreces?', 'M', NULL),
(20, '¿Qué tipo de capacitación ofreces?', 'M', NULL),
(21, '¿Qué  ofreces en Internet?', 'U', NULL),
(22, '¿Qué herramientas de Venta en Línea necesitas?', 'M', NULL),
(23, '¿Qué herramientas de Venta en Línea ofreces?', 'M', NULL),
(24, '¿Qué herramientas de publicidad necesitas?', 'M', NULL),
(25, '¿Qué herramientas de publicidad ofreces?', 'M', NULL),
(26, '¿Qué tipo de proyecto?', 'M', NULL),
(27, '¿Cuál es son tus áreas de interés? ', 'M', NULL);

--
-- Volcado de datos para la tabla `plataforma_preguntassimilitud`
--

INSERT INTO `plataforma_preguntassimilitud` (`id`, `funcion_id`, `pregunta_A_id`, `pregunta_B_id`) VALUES
(1, 3, 1, 6),
(2, 2, 3, 5),
(4, 1, 2, 7),
(5, 1, 8, 15),
(6, 1, 9, 16),
(7, 3, 10, 17),
(8, 1, 11, 18),
(9, 1, 12, 20),
(10, 1, 13, 19),
(13, 3, 14, 21),
(14, 3, 6, 1),
(15, 2, 5, 3),
(16, 4, 4, 4),
(17, 1, 7, 2),
(18, 1, 15, 8),
(19, 1, 16, 9),
(20, 1, 17, 10),
(21, 1, 18, 11),
(22, 1, 20, 12),
(23, 1, 19, 13),
(24, 3, 21, 14),
(25, 1, 22, 23),
(26, 1, 24, 25),
(27, 1, 23, 22),
(28, 1, 25, 24),
(29, 1, 26, 27),
(30, 1, 27, 26);

--
-- Volcado de datos para la tabla `plataforma_redsocial`
--

INSERT INTO `plataforma_redsocial` (`id`, `nombre`, `url`, `icono`) VALUES
(1, 'Facebook', 'Facebook', ''),
(2, 'Twitter', 'Twitter', '');

--
-- Volcado de datos para la tabla `plataforma_rol`
--

INSERT INTO `plataforma_rol` (`id`, `nombre`, `descripcion`, `imagen`, `tipo_rol`) VALUES
(2, 'Empresario', 'Descripción Empresario', 'RegistroRolEmpresario.png', 'BC'),
(3, 'Comerciante', 'Descripción Comerciante...', 'RegistroRolComerciante.png', 'BC'),
(4, 'Emprendedor', 'Descripción Emprendedor', 'RegistroRolEmprendedor.png', 'BC'),
(5, 'Académico', 'Descripción Universidad', 'RegistroRolAcademico.png', 'O'),
(6, 'Empresa TIC', 'Empresa TIC', 'RegistroRolEmpresaTIC.png', 'O'),
(7, 'Agencia de Turismo', 'Agencia de Turismo', 'RegistroRolInstitucion.png', 'BT'),
(8, 'Diseñador ', 'Diseñador ', 'RegistroRolDisenador.png', 'O'),
(9, 'Programador', 'Programador', 'RegistroRolProgramador.png', 'O'),
(10, 'Tendero', 'Tendero', 'RegistroRolTendero.png', 'BC'),
(11, 'Artesano', 'Artesano', 'RegistroRolArtesano.png', 'BC'),
(12, 'Publicista', 'Publicista', 'RegistroRolPublicista.png', 'O'),
(13, 'Hotelero', 'Hotelero', 'RegistroRolHotelero.png', 'BT'),
(14, 'Dueño de Restaurante', 'Dueño de Restaurante', 'RegistroRolDuenoRestaurante.png', 'BT'),
(15, 'Guía Turístico', 'Guía Turístico', 'RegistroRolGuiaTuristico.png', 'BT');

--
-- Volcado de datos para la tabla `plataforma_similitud`
--

INSERT INTO `plataforma_similitud` (`id`, `funcion`, `descripcion`) VALUES
(1, 's1', 'Determina el porcentaje de respuestas de A que están en B\r\n\r\n'),
(2, 's2', 'Determina la distancia entre una respuesta a y una respuesta b en R1.\r\nDistancia=abs(a-b)'),
(3, 's3', 'devuelve 1 si dos respuestas son exactamente iguales o 0 en caso contrario'),
(4, 's4', 'devuelve la distancia euclideana en r2');

--
-- Volcado de datos para la tabla `plataforma_variable`
--

INSERT INTO `plataforma_variable` (`id`, `variable`, `valor`, `descripcion`) VALUES
(1, 'MUNICIPIOS', 4, 'El valor de esta variable debe ser el mismo del id_pregunta de "Dónde te encuentras"');
SET FOREIGN_KEY_CHECKS=1;

--
-- Volcado de datos para la tabla `sitios_sitio`
--
INSERT INTO `sitios_sitio` (`nombre`, `latitud`, `longitud`) VALUES
('OPIO LOUNGE',4.66828,-74.055457),
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
('RINCON PAISA DE ORTIZ',4.58416050236045,-74.1014570927021);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
