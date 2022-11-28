comunidades = ["Madrid", "Aragón",
                    "Valencia", "Cataluña",
                    "Extremadura", "Castilla y León",
                    "Castilla La Mancha", "Asturias",
                    "Murcia", "Cantabria", "País Vasco",
                    "Andalucia"]

comunidades_ordenadas = sorted(comunidades, key=len,reverse=True)
print(comunidades_ordenadas)