# Este algoritmo le pide al usuario que ingrese N que sera el total de numeros 
# que seran multiplicados, se hace un ciclo for que va desde 1 hasta N, dentro del 
# ciclo se le pide al usuario que ingrese todos los valores y se guardan en 
# un arreglo, posteriormente se multiplican todos los elementos del arreglo y se 
# imprime el resultado
numeros = []
n = int(input("Ingresa el valor de N: "))
for numero in range(1, n + 1):
    valor = float(input("Ingresa el valor {}: ".format(numero)))
    numeros.append(valor)
resultado = 1  # Inicializamos el resultado en 1
for resul in numeros:
    resultado *= resul  # Multiplicamos cada número con el resultado
print("El producto de los números es:", resultado)