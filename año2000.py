print ("ingrese el año")
Año=int(input(""))
print("ingrese el mes")
mes=int(input(""))
print("ingrese el dia")
dia=int(input(""))

if dia>0 and dia <30:
    dia=dia+1
    print("el dia es",dia)
    print("el mes es",mes)
    print("el año es",Año)
elif mes>0 and mes<12:
    print("1")
    mes=mes+1
    print("el mes es",mes)
    print("el año es",Año)
else:
    print("1")
    print("1")
    Año=Año+1
    print("el año es",Año)
    