print("ingrese el valor de B" )
B=int(input(""))
print("ingrese el valor de A")
A=int(input(""))
print("ingrese el valor de C")
C=int(input(""))
D=B**2-4*A*C
if D>0:
    X1=((-B)+D**0.5)/2*A
    x2=((-B)-D**0.5)/2*A

    print("las raices reales son ",X1,x2)
else:
    print("No hay raices")    