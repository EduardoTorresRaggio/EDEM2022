import math

def area_triangulo(altura,base):
    altura = float(input("Dime la altura del traingulo: \n"))
    base = float(input("Dime la base del triangulo: \n"))
    area = (altura * base)/2
    print(f"El area del triangulo es : {area}")
    return area

def area_circulo(radio):
    radio = float(input("Dime el radio: \n"))
    area2 = math.pi*radio*radio
    print(f"El area del circulo es : {area2}")

area_triangulo(5,3)
area_circulo(3)
