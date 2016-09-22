mysql -u root -proot -e 'drop database plataforma;create database plataforma  CHARACTER SET latin1 COLLATE latin1_swedish_ci'

python manage.py migrate
mysql -u root -proot --default-character-set=utf8  plataforma < datos_iniciales.sql
