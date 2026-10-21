curso = {"nombre": "Fundamentos de Python", "codigo": "PY-01",
         "temas": ["Variables", "Condiciones", "Ciclos"],
         "instructor": {"nombre": "Esteban", "area": "Software"}}

print(curso["nombre"])
print(curso["temas"][1])
print(curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))
