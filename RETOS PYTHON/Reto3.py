def PagoImpuestos():
  personas = ["Edu", "Marina", "Javi", "Miguel", "Franzis", "Elyca", "Carlos"]
  for nombre in personas:
    print(f"Hola {nombre}")
    edad = int(input("Dime la edad:  "))
    if (edad > 16 and edad < 70):
        ingresos = int(input("Dime los ingresos mensuales: "))
        if (ingresos < 800):
            impuesto1 = ingresos *0.1
            print(f"Hola {nombre} has de pagar {impuesto1}")
            print("")
        elif (ingresos >= 800 and ingresos < 2000):
            impuesto2 = ingresos * 0.3
            print(f"Hola {nombre} has de pagar {impuesto2}")
            print("")
        elif (ingresos >= 2000):
             impuesto3= ingresos * 0.5
             print(f"Hola {nombre} has de pagar {impuesto3}")
             print("")
    else:
        print(f"Hola {nombre} no pagas impuestos")
        impuesto4 = 0
        print("")

PagoImpuestos()