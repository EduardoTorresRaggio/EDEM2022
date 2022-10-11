
Introducir = 8
Lista = []
while Introducir > 0:
    Altura = float(input("Dime la altura del edificio: \n"))
    Introducir -=1
    Lista.append(Altura)
    print(Lista)

Lista.sort()
print(Lista[0])
print("Los 3 edificios mas altos son " + str(Lista[0]) + " " + str(Lista[1]) +" "+ str(Lista[2]))
