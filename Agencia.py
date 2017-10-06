print("Bienvenido a la plataforma digital de la agencia de Automoviles.")
a =input("Introduzca el precio del automovil que desea comprar = ")
a =float(a)
if a>=10000:
	if a>=10000 and a<15000:
		z=a*0.25
		y=(a-z)/18
		print("El precio inicial para obtener el automovil es igual a Bs. ",z)
		print("El precio que debera pagar en 18 mensualidades es igual a Bs. ",y)
	if a>=15000:
		z=a*0.35
		y=(a-z)/24
		print("El precio inicial para obtener el automovil es igual a Bs. ",z)
		print("El precio que debera pagar en 24 mensualidades es igual a Bs. ",y)
else:
	print("El precio debe valer mas de 9999 Bs para comprar un automovil.")
