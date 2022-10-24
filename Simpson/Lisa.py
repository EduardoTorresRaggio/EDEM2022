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
   diccionario_palabras = {}
   
   
   #COMPROBACIÓN DE QUE FUNCIONA LA PETICION
   print(autor)
   print(frase_simpson)
   print(autoresfrases)

   if (autor in autoresfrases):
    #autor ya existe

    #################### CARPETA IMAGENES + DESCARGA ################
    '''
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
    '''
     ######################  GUARDAR FRASE AUTOR  ####################

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
    
     ####################### CONTEO PALABRAS ###############

    for i in frase_simpson:
      if i in diccionario_palabras:
        #ya está palabra, por lo que suma 1
        diccionario_palabras[i] += 1
      else:
        #no está palabra, definimos palabra y =1
        diccionario_palabras [i] = 1

    #cada 30seg haga una peticion
    time.sleep(5)
   

   else:
    #autor no ha salido
    
    #######################  CARPETA AUTOR  #################

    #añadir el autor a la lista
    autoresfrases.append(autor)

    print(f"{autoresfrases}\n")

    #crear carpeta autor
    directory = autor
    parent_dir = 'C:\\Users\\sragg\\Documents\\GitHub\\EDEM2022\\Simpson'
    path = os.path.join(parent_dir,directory)
    os.mkdir(path)

    ######################  GUARDAR FRASE AUTOR  ############

    #crear archivo csv y guardar la frase
    with open("autor.csv", 'a', newline='') as f:
     f.write(frase_simpson)

     #mover el archivo desde su posicion creada hasta carpeta (autor)
    shutil.move("autor.csv",path)

   #################### CARPETA IMAGENES + DESCARGA ########

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

     ####################### CONTEO PALABRAS ###############

     #contar palabras
    '''
    with open("autor.csv",'r', newline = '') as f:
    f.read()
    '''
    
    
    palabras = frase_simpson.split(" ")
    for i in palabras:
      if i in diccionario_palabras:
        #ya está palabra, por lo que suma 1
        diccionario_palabras[i] += 1
      else:
        #no está palabra, definimos palabra y =1
        diccionario_palabras [i] = 1
    
    #guardar el conteo
    with open("Conteo",'w',newline='') as f:
      f.write(f"{diccionario_palabras}")

    #mover el diccionario al autor 
    shutil.move("Conteo",path)

    #muestre el conteo de palabras
    print(diccionario_palabras)

    time.sleep(5)