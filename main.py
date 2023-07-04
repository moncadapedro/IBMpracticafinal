# hacer una matrix n x n aleatoria

from random import randint #con esto importamos un comando para poder conseguir numeros aleatorios

#ahora definimos la matriz

def n_matriz (n):
    matriz = []
    
    for r in range (n):
        fila = []
        
        for c in range (n):
            fila.append (randint(0,9))
            
        matriz.append (fila)
        
    return matriz

#solicitamos a la persona que nos de un numero para calcular las matrices
print ("introduce un numero del 0 al 9 ")
n_a = int(input())

# comprobaos que n_a está en el rango 0 - 9
if n_a in range(0, 9): 
    
    resultado = n_matriz(n_a)
    
    print(resultado)
    
else:
    print("me temo que el numero introducido no esta dentro del rango")

