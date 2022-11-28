def Conocelenguaje():
  Programas= ["Pyhton", "JavaScript", "TypeScript","Dart"]
  respuesta = []
  print("Hola!")
  
  for n in Programas:
    respuesta.append(input(f"Conoces el programa {n}?\n"))
    print(f"{Programas} : {respuesta}")

  #si la respuesta en la posicion 0 es no, entonces borrar el programa en la posicion 0
  if respuesta[0] == "no":
    Programas.pop(0)
  elif respuesta[1] == "no":
    Programas.pop(1)
  elif respuesta [2] == "no":
    Programas.pop(2)
  elif respuesta [3] == "no":
    Programas.pop(3)
  else:
    print("Sos un crack")
    
  print(f"{Programas}")
    
Conocelenguaje()
