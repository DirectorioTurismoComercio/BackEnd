mysql -u root -proot -e 'drop database plataforma;create database plataforma'

python manage.py migrate
mysql -u root -proot plataforma < datos_iniciales.sql

