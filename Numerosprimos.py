Contador=0
minimo=1
maximo=1001
for i in range(1,1001):
    primo=True
    j=2
    while i>j and primo==True:
        if i%j==0:
            primo=False
        else:
            j==j+1
    if primo==True:
        print(i,"es primo") 
        Contador=Contador+1
    print("entre",minimo, "y", maximo, "hay",Contador,"numeros primos")       
        

