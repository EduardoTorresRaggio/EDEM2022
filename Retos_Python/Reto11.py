#lista vacia
Clientes = []

#crear un diccionario



def IngresarCliente():
    Peticion = (input('¿Desea ingresar un nuevo cliente?: \n'))
    Cantidad = int(input('Cuantos quieres: \n'))

    '''
    if Peticion == "si":
        Peticion == "True"
    else:
        Peticion == "False"

    while Cantidad > 0:
    '''
    Clientei = {
        "NIF" : str(input('Dime el NIF: \n')),
        "Nombre" : str(input('Dime el Nombre: \n')),
        "Apellidos" : str(input('Dime los Apellidos: \n')),
        "Telefono" : str(input('Dime el Telefono: \n')),
        "Email" : str(input('Dime el email: \n')),
        "Preferente" : bool(input('Dine si es preferente: \n')),
        }
    Clientes.append(Clientei)

    print(Clientes)

def EliminarCliente():
    for i,idx in enumerate(Clientes):
     print(i,idx)

    Seleccion = int(input("Dime el numero donde esta el DNI: \n"))
    
'''
   for i,idx in enumerate(Clientes):
     print(i,idx)
'''


IngresarCliente()
EliminarCliente()
