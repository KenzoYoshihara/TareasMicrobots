print("Bienvenido al sistema de notas del semestre.")
a =input("Introduzca la nota del primer control= ")
b =input("Introduzca la nota del segundo control= ")
c =input("Introduzca la nota del tercer control= ")
d =input("Introduzca la nota del primer laboratorio= ")
e =input("Introduzca la nota del segundo laboratorio= ")
f =input("Introduzca la nota del informe= ")

a =float(a)
b =float(b)
c =float(c)
d =float(d)
e =float(e)
f =float(f)

if (a>=0 and a<=100)and(b>=0 and b<=100)and(c>=0 and c<=100)and(d>=0 and d<=100)and(e>=0 and e<=100)and(f>=0 and f<=100):

	z =((a+b+c)/3)*0.45
	y =((d+e)/2)*0.35
	x =f*0.20
	t =z+y+x
	print("El promedio del semestre de la metira es= ",t,"/100")
else:
	print("Las notas solo pueden estar entre 0 y 100.")
