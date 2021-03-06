INSERT INTO `sitios_sitio` (`id`, `nombre`, `telefono`, `whatsapp`, `horariolocal`, `web`, `latitud`, `longitud`, `descripcion`, `correolocal`, `ubicacionlocal`, `municipio_id`, `usuario_id`, `tipo_sitio`) VALUES
(3000, 'Facatativá', '2708842', '', '', '', 4.802013413359239000, -74.339445233345030000, 'Facatativá, también conocido como Faca, es uno de los 116 municipios del departamento de Cundinamarca, centro de Colombia. Su nombre proviene del muisca, y tiene significados diferentes; sin embargo, «cercado fuerte al final de la llanura» es el más conocido y aceptado.', '', 'Cra 24 # 15-16', 26, 3000, 'M'),
(3001, 'Zipaquirá', '2708842', '', '', '', 5.014092899650111000, -73.990972638130190000, 'Zipaquirá es un municipio colombiano localizado en la provincia de Sabana Centro, de la que es su capital, sede de su diócesis y su ciudad más importante.Comúnmente llamado Zipa en referencia al Zipa; título que ostentaba el cacique muisca del Cacicazgo de Bacatá. Es uno de los centros de explotación de sal más importantes en Colombia, razón por la cual se le llama la "Ciudad de la Sal" y "el congelador de Cundinamarca" debido a su clima frío con niebla en las mañanas. ', '', 'Cra 24 # 15-16', 116, 3000, 'S'),
(3002, 'Suesca', '2708842', '', '', '', 4.802013413359239000, -74.339445233345030000, 'Suesca es un municipio de Cundinamarca, en el centro de (Colombia), ubicado en la provincia de Almeidas. La palabra Suesca se deriva del vocablo muisca "Suehica", que significa "Roca de las Aves".', '', 'Cra 24 # 15-16', 88, 3000, 'S'),
(3003, 'Nemocón', '2708842', '', '', '', 5.060604453534960000, -73.878019452095030000, 'Nemocón es un municipio de Cundinamarca (Colombia), ubicado en la provincia de Sabana Centro, se encuentra a 45 km de Bogotá. Nemocón significa, en idioma muisca, "Lamento o Rugido del Guerrero". Los primitivos pobladores eran los nemzas, de la nación muisca. Desde tiempo inmemorial, los indígenas explotaban las minas de sal. El 9 de julio de 1593 llegó de visita el oidor Miguel de Ibarra. El 11 de agosto, Francisco de Rivero hizo descripción de los indios, de la que resultaron 302. El 26 de julio de 1600 llegó de visita el Pedro Gonzales Rioja y profirió auto de esta fecha y junto con los indios de Tasgata fundó el pueblo. Más tarde, los de Tasgara fueron agregados a Tausa por Joaquín de Aróstequi.', '', 'Cra 24 # 15-16', 60, 3000, 'S');

INSERT INTO `sitios_foto` (`id`, `URLfoto`, `tipo`, `sitio_id`) VALUES
(3000, 'Fotos/blob.jpg', 'P', 3001),
(3001, 'Fotos/blob.jpg', 'P', 3002),
(3002, 'Fotos/Catedraldefaca.jpg', 'P', 3000),
(3003, 'Fotos/1280px-Paque_Nemocón_Cundinamarca.jpg', 'P', 3003);

INSERT INTO `authentication_module_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `tipo_cuenta`, `es_cuenta_activa`) VALUES
(3000, 'pbkdf2_sha256$20000$G47cKQseOQrx$ZPZ02mjl7vTe9XVuJ8/3oBHokGi1DIHGUsdQfqtrRiM=', '2016-09-14 17:23:07.282342', 0, 'municipio', 'Municipio', 'Municipio', 'm@m.mm', 0, 1, '2016-09-14 17:23:07.223316', 'M', 1);

INSERT INTO `authentication_module_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `tipo_cuenta`, `es_cuenta_activa`) VALUES
(3001, 'pbkdf2_sha256$20000$G47cKQseOQrx$ZPZ02mjl7vTe9XVuJ8/3oBHokGi1DIHGUsdQfqtrRiM=', '2016-09-14 17:23:07.282342', 0, 'municipio', 'Municipio', 'Municipio', 't@t.tt', 0, 1, '2016-09-14 17:23:07.223316', 'C', 1);

