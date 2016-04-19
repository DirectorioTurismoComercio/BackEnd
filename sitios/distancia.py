from math import *

def geodesica_a_cartesiana(coordenada):
  R=6372.795477598
  latitudRadianes=float(coordenada[0])*pi/180
  longitudRadianes=float(coordenada[1])*pi/180
  x=R*sin(longitudRadianes)
  y=R*sin(latitudRadianes)
  return (x,y)

def hallar_angulo_rotacion(coordenadaInicial,coordenadaFinal):
  return pi-(atan((coordenadaFinal[1]-coordenadaInicial[1])/(coordenadaFinal[0]-coordenadaInicial[0])))

def hallar_punto_rotado(coordenada,anguloRotacion):
  coordenadaXRotada=(coordenada[0]*cos(anguloRotacion))-(coordenada[1]*sin(anguloRotacion))
  coordenadaYRotada=(coordenada[0]*sin(anguloRotacion))+(coordenada[1]*cos(anguloRotacion))
  return (coordenadaXRotada, coordenadaYRotada)

def hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal):
  return sqrt(pow((coordenadaFinal[0]-coordenadaInicial[0]),2)+pow((coordenadaFinal[1]-coordenadaInicial[1]),2))

def hallar_a(distanciaSinRotar):
  return hallar_distancia_sin_rotar(coordenadaInicial,coordenadaFinal)/2

def hallar_distancia_traslacion_X(puntoRotado,a):
  return puntoRotado-a

def hallar_coordenada_trasladada(coordenadaRotada,distanciaTranslacion):
  return coordenadaRotada-distanciaTranslacion
  
def hallar_distancia_geodesica(a,b):
  R=6372.795477598
  ar=(float(a[0])*pi/180,float(a[1])*pi/180) # se convierte a radianes
  br=(float(b[0])*pi/180,float(b[1])*pi/180)
  distancia = R*acos(sin(ar[0])*sin(br[0])+cos(ar[0])*cos(br[0])*cos(ar[1]-br[1]))

  return distancia 

def esta_dentro_de_elipse(a,b,x,y):
  resultado=(pow(x,2)/pow(a,2))+(pow(y,2)/pow(b,2))
  return resultado <=1

