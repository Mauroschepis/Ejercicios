print ("ingrese valores del menu")
print ("1: area del triangulo")
print("2:area del circulo")
opc=int(input("opc :"))
pi=3.1416
if opc ==1:
    print ("Area del triangulo")
    print("ingrese el lado del tringulo")
    L=int(input("el lado es :"))
    A=((3**0.5)/4)*L**2
    print ("El area del tringulo es :",A)
elif opc ==2:
    print ("area del circulo")
    print("ingrese el radio del circulo")
    R=int(input("el radio es: "))
    c=pi*R**2
    print("El area del circulo es",c)
else:
    print("Valor no encontrado")
