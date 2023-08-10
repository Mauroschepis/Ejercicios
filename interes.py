c=-1
i=0
m=0

while (c<0) or (i<=0) or (i>=100) or (m<=0):
    print ("introduce el capital, el interes y el tiempo apropiados")
    c = int(input("El capital es:"))
    i = int(input("el interes es: "))
    m = int(input("el Tiempo es:"))

    print(c, i ,m)
for i in range(m):
 c=c*(1+i/100)
# 
print("tienes",c,"pesos")