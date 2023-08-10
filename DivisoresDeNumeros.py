print("introduce un numero, y para acabar uno negativo")
N=int(input(""))
while N>0:
    suma=0
    i=1
    for i in range (1,int (N/2)):
        print(i)
        if N%i==0:
            suma=suma+1
    suma=suma+N
    print("la suma de lsos divisores del numero es", suma)
