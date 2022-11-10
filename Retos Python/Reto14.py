
import math
def area_circulo(radio):
    area2 = math.pi*radio*radio
    print(f"El area del circulo es : {area2}")

def vol_cilindro(h,radio):
    area_circulo(radio)
    h = float(input("Dime la altura: \n"))
    vol = math.pi * radio * radio * h
    print(f"El volumen del clindro es: {vol}")

area_circulo(5)
vol_cilindro(10,5)