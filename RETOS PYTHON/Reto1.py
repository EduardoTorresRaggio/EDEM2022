# GUARDAR EN UNA LISTA LOS DISCOS QUE HAY
ListaDiscos =[{'Nombre': 'Thriller','Artista': 'Michael Jackson','Año': 1995,'Precio': 20,'Genero': 'Pop'},
{'Nombre': 'Quedate','Artista': 'Quevedo','Año': 2022,'Precio': 15,'Genero': 'Reggaeton'},
{'Nombre': 'Bad','Artista': 'David Guetta','Año': 2015,'Precio': 30,'Genero': 'Electro'},
{'Nombre': 'Highway to Hell','Artista': 'ACDC','Año': 1995,'Precio': 10,'Genero': 'Rock'},
{'Nombre': 'The number of the beast','Artista': 'Iron Maiden','Año': 1970,'Precio': 12,'Genero': 'Metal'},
{'Nombre': 'Flying Wales','Artista': 'Gojira','Año': 1995,'Precio': 14,'Genero': 'Death Metal'},
{'Nombre': 'Where Dead Angels Lie','Artista': 'Dissection','Año': 1985,'Precio': 17,'Genero': 'Death Metal'}]

# MOSTRAR EN PANTALLA LA LISTA DE DISCOS
for idx in enumerate(ListaDiscos):
  print(idx[0], idx[1]['Nombre'])

#NO FUNCIONA
#for i,Disco in ListaDiscos:
  #print(f"{i}:Album{Disco['Nombre']}")

#PEDIR SELECCION DISCO
seleccion = int(input("Seleccionar un disco: "))

#IMPRIMIR EL DISCO SELECCIONADO
print(ListaDiscos[seleccion]['Genero'])

#SACAR EL PRECIO DEL DISCO SELECCIONADO
if ListaDiscos[seleccion]['Genero'] == 'Electro' or ListaDiscos[seleccion]['Genero'] == 'Black Metal':
  PrecioCarrito = ListaDiscos[seleccion]['Genero'] * 0.7
else:
  PrecioCarrito = ListaDiscos[seleccion]['Genero']


