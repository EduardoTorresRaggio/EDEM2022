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
carrito = list()

#PEDIR SELECCION DISCO
while True:
  seleccion = int(input("Seleccionar un disco: "))
  if seleccion == -1:
    break
  else: 
    carrito.append({ListaDiscos[seleccion]["Nombre"]},{ListaDiscos[seleccion]["Precio"]},{ListaDiscos[seleccion]["Genero"]})




#IMPRIMIR EL DISCO SELECCIONADO
print(ListaDiscos[seleccion]['Genero'])

#SACAR EL PRECIO DEL DISCO SELECCIONADO 
#METODO 1
for i in carrito:
  if i['Genero'] == 'Electro' or i['Genero'] == 'Black Metal':
    PrecioCarrito = i['precio'] * 0.7
    cantidadDescuento = i['precio'] * 0.3
  else:
    PrecioCarrito = i['Genero']


#METODO 2
for i in range(len(carrito)):
  if carrito[i]['estilo'] == 'Electro' or  carrito[i]['estilo'] == 'Black Metal':
    PrecioCarrito = carrito[i]['precio' * 0.7]
    cantidadDescuento = carrito [i]['precio'] * 0.3
  else:
    PrecioCarrito = carrito [i]

#METODO 3A
for idx,i in enumerate(carrito):
  if carrito[idx]['estilo'] == 'Electro' or carrito[idx]['estilo'] == 'Black Metal':
    PrecioCarrito = carrito[idx]['precio' * 0.7]
    cantidadDescuento = carrito [idx]['precio'] * 0.3
  else:
    PrecioCarrito = carrito [idx]
#METODO 3A  
  if i['estilo'] == 'Electro' or i['estilo'] == 'Black Metal':
    PrecioCarrito = carrito[i]['precio' * 0.7]
    cantidadDescuento = carrito [i]['precio'] * 0.3
  else:
    PrecioCarrito = carrito [i]
