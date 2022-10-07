#arepera
def Palindromo():
  Ejemplo = str(input("Dime una palabra: "))
  AlReves = Ejemplo [::-1]

  if (Ejemplo == AlReves):
    print("Es un palindromo")
  else:
    print("Intentalo de nuevo")

Palindromo()