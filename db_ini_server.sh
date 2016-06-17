mysql -u cundimercado -plabvirtuales@2015 -e 'drop database plataforma2;create database plataforma2'

python manage.py migrate
mysql -u cundimercado -plabvirtuales@2015 plataforma2 < datos_iniciales.sql