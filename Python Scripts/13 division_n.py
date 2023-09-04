# Este algoritmo le pide al usuario que ingrese N que sera el total de numeros 
# que seran divididos, se hace un ciclo for que va desde 1 hasta N, dentro del 
# ciclo se le pide al usuario que ingrese todos los valores y se guardan en 
# un arreglo, posteriormente se dividen todos los elementos del arreglo y se 
# imprime el resultado
numeros = []
n = int(input("Ingresa el valor de N: "))
for numero in range(1, n + 1):
    valor = float(input("Ingresa el valor {}: ".format(numero)))
    numeros.append(valor)
resultado = numeros[0]  # Inicializamos el resultado con el primer número
for resul in numeros[1:]:
    if resul != 0:  # Asegurarse de no dividir por cero
        resultado /= resul  # Dividir el resultado por cada número
print("El resultado de la división de los números es:", resultado)