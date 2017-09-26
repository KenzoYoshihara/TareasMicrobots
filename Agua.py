print("Bienvenido al sistema de cobro de Aguas Negras")
a =input("Introduzca la cantidad de litros que gasto en su vivienda.\n")
a =int(a)
if a>=0 and a<=50:
	print("La cuota a pagar es de Bolivianos \n6")
if a>=51 and a<=200:
	b=int(a)*0.1
	print("La cuota a pagar es de Bolivianos")
	print(b)
if a>=201:
	b=int(a)*0.3
	print("La cuota a pagar es de Bolivianos")
	print(b)
