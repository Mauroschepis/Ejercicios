print("Ingrese la velocidad de el primer coche")
A=int(input(""))
print("ingrese la velocidad del otro coche")
B=int(input(""))
print("Ingrese la distancia")
D=int(input(""))

if A>0 and B>0 and D>0:
    

    T=D/(A+B)
    print("El tiempo del choque es ",T)
else:
    print("No hubo choque")
