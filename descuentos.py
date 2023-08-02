print("ingrese el costo del articulo")
costo=int(input(""))
print("ingrese la marca")
marca=(input(""))
if costo>=2000 and marca=="NOSY":
    pago=costo*0.90
    pagototal=pago*0.95
    print ("usted pagara",pagototal,"pesos")
elif costo>=2000 and marca!="NOSY":
    pagototal=costo*0.90
    print("ustdes pagara",pagototal,"pesos")
elif costo<2000 and marca=="NOSY":
    pago=costo*0.95
    pagototal=pago+pago*0.20
    print("ustedes pagara",pagototal,"pesos")
elif costo<2000 and marca !="NOSY":
    pagototal=costo*1.20
    print("usted pagara",pagototal,"pesos")

