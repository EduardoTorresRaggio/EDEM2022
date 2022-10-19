#llamar a la API
from urllib import request
import requests
import csv
import time
import os
import shutil


while True:
   URL= 'https://thesimpsonsquoteapi.glitch.me/quotes'
  
  #Obtenemos el paquete/caja que nos viene de ahi con el get'
   respuesta = requests.get(url=URL)
   
  #extraemos los datos en formato JSON
   datos = respuesta.json()
   estado = respuesta.status_code
  #accedemos a datos, y especificamente a la clave donde esta el chiste
  #y lo guardamos en una variable
   frase_simpson:str = datos[0]['quote']
   autor:str = datos[0]['character']
   
   #LISTA VACIA PARA COMPROBAR SI EL AUTOR YA HA SALIDO
   autoresfrases =[]

   #COMPROBACIÓN DE QUE FUNCIONA LA PETICION
   print(autor)
   print(frase_simpson)

   if (print(autor in autoresfrases)):
    #autor ya existe
    with open(autor, 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(frase_simpson)
    #descargar la imagen

   else:
    #autor no ha salido

    #añadir el autor a la lista
    autoresfrases.append(autor)

    #crear carpeta autor
    directory = autor
    parent_dir = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)

    #comprobación donde se ha creado
    print("Directory '%s' created" %directory)

    #crear archivo csv y guardar la frase
    with open("autor.csv", 'a', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
     spamwriter.writerow(frase_simpson)

    #mover el archivo desde su posicion creada hasta carpeta (autor)
    shutil.move("autor.csv",path)

    #crear carpeta imagenes dentro de autor
    directory1 = "imagenes"
    parent_dir1 = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
    path1 = os.path.join(parent_dir1,directory1)
    os.mkdir(path1) 

    #descargar la imagen en la carpeta imagenes, dentro de autor
    imagen = datos[0]['image']
    with open(imagen, 'wb') as handler:
	    handler.write(respuesta)

    #mover la imagen descargada a la carpeta del autor
    shutil.move('imagen.png',path1)

