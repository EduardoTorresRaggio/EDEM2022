import math as m

def Precios():
  listaprecios = []
  Npreguntas = 1
  while Npreguntas <= 5:
    listaprecios.append(float(input("Dime el precio: \n")))
    Npreguntas += 1

  print("El precio medio es =",sum(listaprecios) / len(listaprecios));

Precios()