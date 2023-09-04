# Este algoritmo le pide al usuario que ingrese N que sera el total de numeros 
# que seran restados, se hace un ciclo for, que va desde 1 hasta N, dentro del 
# ciclo se le pide al usuario que ingrese todos los valores y se guardan en 
# un arreglo, posteriormente se restan todos los elementos del arreglo y se 
# imprime el resultado
numeros = []
n = int(input("Ingresa el valor de N: "))
for numero in range(1, n + 1):
    valor = float(input("Ingresa el valor {}: ".format(numero)))
    numeros.append(valor)
resta = numeros[0] - sum(numeros[1:])
print("La resta es: " +  str(resta))