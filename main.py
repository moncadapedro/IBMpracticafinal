#Hacer una matrix n x n aleatoria

#importamos dos statements, uno para que nos busque los numeros random y el otro para terminar el programa
import random
import sys
#Definimos como se va a generar la matriz
def generar_matriz(n):
    matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    return matriz
#definimos la llamada para que nos imprima por pantalla la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
#se define el calculo de la suma de filas
def calcular_suma_filas(matriz):
    suma_filas = [sum(fila) for fila in matriz]
    return suma_filas
#se define el calculo de la suma de Columnas
def calcular_suma_columnas(matriz):
    suma_columnas = [sum(columna) for columna in zip(*matriz)]
    return suma_columnas
#Definimos como nos va a dar el resultado de las filas una por una
def imprimir_suma_filas(suma_filas):
    print("Suma de cada fila:")
    for i, suma in enumerate(suma_filas):
        print(f"Fila {i + 1}: {suma}")


#Definimos como nos va a dar el resultado de las columnas una por una
def imprimir_suma_columnas(suma_columnas):
    print("Suma de cada columna:")
    for i, suma in enumerate(suma_columnas):
        print(f"Columna {i + 1}: {suma}")

# Obtenemos el tamaño de la matriz del usuario
n_a = int(input("Ingrese el tamaño de la matriz dentro del rango(0,9): "))
#Comprobamos que la numeracion introducida este dentro del rango
if n_a in range(0, 9):
    
    # Generamos la matriz si esta en el rango
    matriz = generar_matriz(n_a)

    # Imprimimos la matriz generada
    print("Matriz generada:")
    imprimir_matriz(matriz)
else:
    print("me temo que el numero introducido no esta dentro del rango")
#Damos una segunda oportunidad para que ingrese un numero dentro del ranto

    n_a = int(input("Ingrese el tamaño de la matriz dentro del rango(0,9): "))
    if n_a in range(0, 9):

        # Generamos la matriz si esta en el rango
        matriz = generar_matriz(n_a)

        # Imprimir la matriz generada
        print("Matriz generada:")
        imprimir_matriz(matriz)
#Si el usuario persiste en dar un numero fuera del rango entonces acabamos el programa
    else:
        print("Entiendo que no quieres hacerme caso")
        sys.exit()


# Calculamos la suma de cada fila y columna
suma_filas = calcular_suma_filas(matriz)
suma_columnas = calcular_suma_columnas(matriz)

# Imprimimos por pantalla la suma de cada fila y columna
imprimir_suma_filas(suma_filas)
imprimir_suma_columnas(suma_columnas)