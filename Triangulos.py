print("***INGRESA LAS MEDIDAS QUE TE INDICA PARA SABER QUE TRIANGULO ES***")
print()

a = int(input("Ingrese la medida A: "))
b = int(input("Ingrese la medida B: "))
c = int(input("Ingrese la medida C: "))

if a == b and b == c and a==c:
    print("El Triángulo es Equilátero")

elif a == b or b == c or a==c:
    print("El Triángulo es Isósceles")

else:
    print("El triángulo es Escaleno")

print()
print("***FIN***")
