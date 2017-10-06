print("Bienvenido al sistema de promedio de practicas.")
a =input("Introduzca la nota de la primer practica= ")
b =input("Introduzca la nota de la segunda practica= ")
c =input("Introduzca la nota de la tercera practica= ")
d =input("Introduzca la nota de la cuarta practica= ")

a =float(a)
b =float(b)
c =float(c)
d =float(d)

if (a>=0 and a<=100)and(b>=0 and a<=100)and(c>=0 and c<=100)and(d>=0 and d<=100):
	if (a==b and b==c and c==d):
		print("El promedio de practicas= ",a,"/100")

	if (a<b and a<c and a<d):
		z=((b+c+d)/3)
		print("El promedio de practicas es= ",z,"/100")
	if (b<a and b<c and b<d):
		z=(a+c+d)/3
		print("El promedio de practicas es= ",z,"/100")
	if (c<a and c<b and c<d):
		z=(a+b+d)/3
		print("El promedio de practicas es= ",z,"/100")
	if (d<a and d<b and d<c):
		z=(a+b+c)/3
		print("El promedio de practicas es= ",z,"/100")
else:
	print("Los valores de las notas solo pueden estar entre 0 y 100")
