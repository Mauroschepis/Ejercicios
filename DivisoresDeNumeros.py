print("introduce un numero, y para acabar uno negativo")
N=int(input(""))
while N>0:
    suma=0
    for i in range (1,N + 1):
        if N%i==0:
            suma=suma+i
    print("la suma de los divisores del numero es", suma)
    N= int (input("ingrese numero"))
