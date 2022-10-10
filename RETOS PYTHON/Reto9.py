from audioop import reverse


def Binario():
    #dime un numero
    numero = float(input("Dime el numero que quieras convertir en binario: "))
    binario = []

    #mientras sea mayor que 2, dame el resto
    while numero >= 1:
        cociente = numero / 2
        resto = int(numero % 2)
        binario.append(resto)
        numero = cociente
  
    print(f' La lista es: {binario}')
    #guardarlo en lista
    #invertir en lista
    binario.reverse()
    print(f'El numero binario es {binario}')
    #imprimir lista

Binario()