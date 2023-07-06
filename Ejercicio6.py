Cuenta = float(input("Ingrese la cuenta: "))
Porcentaje_propina = float(input("Ingrese el porcentaje de: ")) 

Propina = Cuenta * Porcentaje_propina / 100

print("Se debera pagar", Propina, "de propina")

total = Cuenta + Propina
print("En total se pagara", total)