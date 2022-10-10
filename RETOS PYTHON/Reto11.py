#lista vacia
Clientes = []

#crear un diccionario
Peticion = bool(input('¿Desea ingresar un nuevo cliente?\n'))
Cantidad = int(input('Cuantos quieres: \n'))

def IngresarCliente():
    #traduccion
    if Peticion == "si":
        Peticion == True
    else:
        Peticion == False

    if Peticion == True:
        #abrir un diccionario
        Clientei = {
            "NIF" : str(input('Dime el NIF: \n')),
            "Nombre" : str(input('Dime el Nombre: \n')),
            "Apellidos" : str(input('Dime los Apellidos: \n')),
            "Telefono" : str(input('Dime el Telefono: \n')),
            "Email" : str(input('Dime el email: \n')),
            "Preferente" : bool(input('Dine si es preferente: \n')),
        }
        Clientes.append(Clientei)
    else:
        print('Gracias')

def EliminarCliente():
    NIFX = str(input('Dime el NIF que deseas eliminar: \n'))
    if Clientes['NIF'] == NIFX:
        for i,idx in enumerate(Clientes):
          print(i,idx)
    else:
        print("El cliente no esta en la base de datos \n")
    
    FilaX = int('Dime la fila donde esta el DNI: \n')
    FilaX.clear()
    

'''
   for i,idx in enumerate(Clientes):
     print(i,idx)
'''


IngresarCliente()
EliminarCliente()
