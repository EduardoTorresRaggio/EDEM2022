def Conocelenguaje():
  Programas= ["Pyhton", "JavaScript", "TypeScript","Dart"]
  respuesta = []
  print("Hola!")
  for n in Programas:
    respuesta.append(input(f"Conoces el programa {n}?\n"))

  
  print(f"{Programas} : {respuesta}")

Conocelenguaje()

def Eliminarlenguaje():
    if 