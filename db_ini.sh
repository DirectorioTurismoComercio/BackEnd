mysql -u root -proot -e 'drop database plataforma;create database plataforma  CHARACTER SET latin1 COLLATE latin1_swedish_ci'

python manage.py migrate
mysql -u root -proot plataforma < datos_iniciales.sql
mysql -u root -proot plataforma < sitios_sitio.sql
mysql -u root -proot plataforma < sitios_foto.sql
mysql -u root -proot plataforma < authentication_module_customuser.sql

