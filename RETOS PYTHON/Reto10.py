#MCD MCM
#MCD: numeros inferiores que al dividir el resto da 0

def factores1():
  divisores1 = []
  numero1 = int(input("Dime el numero: "))
  while numero1 > 1:
    if numero1 % 2 == 0:
      divisores1.append("2")
      numero1 = numero1/2
    elif numero1 % 3 == 0:
      divisores1.append("3")
      numero1 = numero1/3
    elif numero1 %5 == 0:
      divisores1.append("5")
      numero1 = numero1/5
    else:
      divisores1.append("numero1")
  print(list(divisores1))
    
factores1()

def factores2():
  divisores2 = []
  numero2 = int(input("Dime el numero: "))
  while numero2 > 1:
    if numero2 % 2 == 0:
      divisores2.append("2")
      numero2 = numero2/2
    elif numero2 % 3 == 0:
      divisores2.append("3")
      numero2 = numero2/3
    elif numero2 % 5 == 0:
      divisores2.append("5")
      numero2 = numero2/5
    else:
      divisores2.append("numero2")
  print(list(divisores2))
    
factores2()
#comunes y no comunes al mayor exponente
def MCM():
  rep12 = []
  rep13 = []
  rep15 = []
  rep22 = []
  rep23 = []
  rep25 = []
  listaMCM = []
  divisores1a = divisores1[]
  divisores2a = divisores2[]

  for n in divisores1a:
    if n == 2:
      rep12 +=1
    elif n == 3:
      rep13 +=1
    elif n == 5:
      rep15 +=1

  for n in divisores2a:
    if n == 2:
      rep22 +=1
    elif n == 3:
      rep23 +=1
    elif n == 5:
      rep25 +=1

  if (rep12 > rep22):
    listaMCM.append(rep12)
  else:
    listaMCM.append(rep22)

  if (rep13 > rep23):
    listaMCM.append(rep13)
  else:
    listaMCM.append(rep23)
    
  if(rep15 > rep25):
    listaMCM.append(rep15)
  else:
    listaMCM.append(rep25)

  print(f"El MCM es {listaMCM}")

MCM()
  