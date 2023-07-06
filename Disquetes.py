Cantidad_de_informacion = float(input("Introduzca la  cantidad de informacion a guardar(Expresada en GB): "))

Informacion_pasado_a_megas = Cantidad_de_informacion * 1024

Cantidad_de_disquetes = Informacion_pasado_a_megas / 1.44

print("Se necesitarian", Cantidad_de_disquetes, "Disquetes para guardar esa cantidad de informacion")