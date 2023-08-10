print("introduce un numero, y para acabar uno negativo")
N=int(input(""))
while N>0:
    suma=0
    for i in range (1,N + 1):
        print(i)
        if N%i==0:
            suma=suma+i
    suma=suma+N
    print("la suma de lsos divisores del numero es", suma)
