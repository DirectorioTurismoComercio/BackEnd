import mysql.connector
from mysql.connector import errorcode
from os import listdir
from os.path import isfile, join
import os


path='Fotos/Fotos/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
urls = []
try:
  cnx = mysql.connector.connect(user='root',
  								password='root',
                                database='plataforma')
  print "connected successfully"
  cursor = cnx.cursor()
  query = ("SELECT URLfoto from sitios_foto")
  cursor.execute(query)

  for (URLfoto) in cursor:
     	urls.append(URLfoto[0].split('Fotos/')[1].encode())
  i=0
  for file in onlyfiles:
  	if file not in urls:
  	    print "deleting...",path+'/'+file
  	    os.remove(path+'/'+file)
  	    i = i+1

  print "urls:", len(urls)
  print "files:", len(onlyfiles)
  print "diff:", i
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()