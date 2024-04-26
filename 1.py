datos = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 28}
]

primer_dict = datos[0]
prim_nombre = primer_dict["nombre"]
seg_edad = datos[1]["edad"]

print("El primer nombre en la lista es:", prim_nombre)
print("La edad de la segunda persona en la lista es:", seg_edad)

print("Recorriendo la lista de diccionarios:")
for dicc in datos:
    for clave, valor in dicc.items():
        print(clave + ":", valor)