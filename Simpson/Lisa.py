#llamar a la API
from random import random
from urllib import request
import requests
import csv
import time
import os
import shutil
import random

#LISTA VACIA PARA COMPROBAR SI EL AUTOR YA HA SALIDO
autoresfrases =[]

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
   
   
   #COMPROBACIÓN DE QUE FUNCIONA LA PETICION
   print(autor)
   print(frase_simpson)
   print(autoresfrases)

   if (autor in autoresfrases):
    #autor ya existe

    #descargar la imagen
    imagen = str(random.randint(0,100)) + "_" + 'imagen.png'
    image_url = datos[0]['image']
    img_data = requests.get(image_url).content
    with open(imagen,'wb') as handler:
        handler.write(img_data)

    #recorrer directorio
    direc = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
    with os.scandir(direc) as ficheros:
      for i in ficheros:
        if i.name == autor:
         direc1 = os.path.join(direc,autor)
         direc2 = "imagenes"
         direc3 = os.path.join(direc1,direc2)
         #mover la imagen descargada a la carpeta del autor
         shutil.move(imagen,direc3)

   
#PROBLEMA Nº1: COMO HACER QUE ESCRIBA EN EL CSV DEL AUTOR QUE ACABA DE SALIR
    #escribir la frase en el CSV que ya se ha creado ANTES por AUTOR

    #esta es la dirección del autor
      direc = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
      directory99 = autor
      path99 = os.path.join(direc,directory99)
      archivo = 'autor.csv'
    #esta es la ruta del archivo del autor
      path98 = os.path.join(path99,archivo)
  
    #ir a esta ruta
    #quiero añadir una linea en el archivo 'autor.csv'
      with open(path98,"a") as f:
        f.write("\n")
        f.write(frase_simpson)
        

    #cada 30seg haga una peticion
    time.sleep(5)
   

   else:
    #autor no ha salido
    

    #añadir el autor a la lista
    autoresfrases.append(autor)

    print(f"{autoresfrases}\n")

    #crear carpeta autor
    directory = autor
    parent_dir = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)

    #crear archivo csv y guardar la frase
    with open("autor.csv", 'a', newline='') as f:
     f.write(frase_simpson)

    #mover el archivo desde su posicion creada hasta carpeta (autor)
    shutil.move("autor.csv",path)

    #crear carpeta imagenes dentro de autor
    directory1 = "imagenes"
    path1 = os.path.join(path,directory1)
    os.mkdir(path1) 

    #descargar la imagen 
    image_url = datos[0]['image']     
    imagen = str(random.randint(0,100)  ) + "_" + 'imagen.png'
    img_data = requests.get(image_url).content  
    with open(imagen,'wb') as handler:
        handler.write(img_data)
    
    #mover la imagen descargada a la carpeta del autor
    shutil.move(imagen,path1)

    time.sleep(5)