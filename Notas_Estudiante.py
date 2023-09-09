print("***INGRESA LAS NOTAS DE TUS 4 MATERIAS***")
print()

español = float(input("Ingresa tu nota de Español: "))
ingles = float(input("Ingresa tu nota de Ingles: "))
matematicas = float(input("Ingresa tu nota de Matematicas: "))
sociales = float(input("Ingresa tu nota de Sociales: "))

promedio = (español + ingles + matematicas + sociales)/4

if promedio >= 3.6:
    print("Aprobado")

elif promedio == 3.5 or promedio >= 3.0:
    print("Aprobaste pero debes mejorar para la próxima")

elif promedio <= 2.9:
    print("Reprobado")

else:
    print("VALOR INVALIDO INTENTE DE NUEVO")

print()
print("***FIN***")
