print("Bienvenido a venta de computadoras.\nCada computadora cuesta $ 750.")
a =input("Introduzca la cantidad de computadoras que desea comprar= ")
a =int(a)

if a>=1:
	if a>=1 and a<5:
		z=750*a-750*0.1
		print("El precio con descuento del 10% para comprar ",a," computadoras es = $ ",z)
	if a>=5 and a<10:
		z=750*a-750*0.2
		print("El precio con descuento del 20% para comprar ",a," computadoras es = $ ",z)
	if a>=10:
		z=750*a-750*0.4
		print("El precio con descuento del 40% para comprar ",a," computadoras es = $ ",z)
else:
	print("Error")
