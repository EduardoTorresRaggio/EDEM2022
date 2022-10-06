#nombramos los diccionarios
Disco1 = dict
Disco2 = dict
Disco3 = dict
Disco4 = dict
Disco5 = dict
Disco6 = dict
Disco7 = dict

Disco1 = {
  'Nombre': 'Thriller',
  'Artista': 'Michael Jackson',
  'Año': 1995,
  'Precio': 20,
  'Genero': 'Pop',
  }

Disco2 = {
  'Nombre': 'Quedate',
  'Artista': 'Quevedo',
  'Año': 2022,
  'Precio': 15,
  'Genero': 'Reggaeton',
  }

Disco3 = {
  'Nombre': 'Bad',
  'Artista': 'David Guetta',
  'Año': 2015,
  'Precio': 30,
  'Genero': 'Electro'
  }

Disco4 = {
  'Nombre': 'Highway to Hell',
  'Artista': 'ACDC',
  'Año': 1995,
  'Precio': 10,
  'Genero': 'Rock'
  }

Disco5 = {
  'Nombre': 'The number of the beast',
  'Artista': 'Iron Maiden',
  'Año': 1970,
  'Precio': 12,
  'Genero': 'Metal'
  }

Disco6 = {
  'Nombre': 'Flying Wales',
  'Artista': 'Gojira',
  'Año': 1995,
  'Precio': 14,
  'Genero': 'Death Metal',
  }

Disco7 = {
  'Nombre': 'Where Dead Angels Lie',
  'Artista': 'Dissection',
  'Año': 1985,
  'Precio': 17,
  'Genero': 'Death Metal',
  }

LibreriaDiscos= [
    Disco1, Disco2, Disco3, Disco4, Disco5, Disco6, Disco7
]
#Crear una función que lea la lista de diccionarios, guarde en una lista los nombres y los imprima
def BuscarDisco():
    for discos in LibreriaDiscos:
        #guardar en lista el nombre de los discos
        #ERRROR: dice que nombre no está definido cuando está dentro del diccionario
        NombreDiscos= [{Nombre.discos}]
        #imprimir por pantalla los discos que hay
        print(NombreDiscos)

#Que el usuario elija el disco que quiera
def EleccionDisco():
    Eleccion:str = input("Elige el disco: ")
    #Si la eleccion no existe en Nombre, pedir que los introduzca de nuevo
    if Eleccion == NombreDiscos:
        pass
    else:
        Eleccion:str = input(print("Error al leer la petición, porfavor escribalo de nuevo: "))ç

#Dar a pantalla los datos del disco
def ImprimirDatosDisco():
    for n in LibreriaDiscos:
        if(Eleccion == NombreDiscos)
        print()
