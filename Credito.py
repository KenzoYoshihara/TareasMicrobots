print("Bienvenido al sistema de cobro de libros a credito.\n")
a =input("Introduzca el precio del libro en Bolivianos.\n")
b =input("Escoja el plan a pagar.\n")
c =input("1. Pagar el costo total del libro.\n2. Pagar el costo del libro a plazos.") 

a= int(a)
b= int(b)
c= int(c)
d= int(d)

if c==1:
	print("El Precio a pagar es de Bolivianos = ")
	print(a)
if c==2:
	z= input("Introduzca en cuantas cuotas comprara el libro.\n")
	z= int(z)
	y=(int(a)/int(z)+(0.03*int(z))
	print("El precio a pagar en cada cuota es de Bolivianos.\n")
	print(y)
else:
	print("Opcion invalida")
