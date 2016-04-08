mysql -u root -p -e 'drop database plataforma;create database plataforma'

python manage.py migrate

mysql -u root -p plataforma < datos_iniciales.sql

