num = int(input("Ingresa un número natural positivo: "))

# Verificar si el número ingresado es positivo
if num < 0:
    print("El número ingresado no es válido. Inténtalo de nuevo.")
else:
    # Calcular la suma del rango
    suma = 0
    for i in range(num+1):
        suma += i
    
    # Mostrar el resultado
    print("La suma del rango que va desde 0 hasta", num, "es:", suma)
