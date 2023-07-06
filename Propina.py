Cuenta = float(input("Ingrese la Cuenta de Consumo en el Restaurant: "))
Porcentaje_propina = float(input("Ingrese el porcentaje de Propina: ")) 

Propina = Cuenta * Porcentaje_propina / 100

print("Se debera pagar", Propina, "de propina")

total = Cuenta + Propina

print("En total se pagara", total)