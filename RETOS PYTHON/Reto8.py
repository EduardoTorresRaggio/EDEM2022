#3 = 3(2)(1)
def factorial():
  numero = int(input("Dime el numero: "))
  factoriales = []

  while numero > 2:
    if numero > 1:
      añadir = numero - 1
      factoriales.append(añadir)
    else:
      break

  print(f"La lista de factoriales es {factoriales} ")

factorial()