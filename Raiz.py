bandera= 0
print("Bienvenido, introduzca el valor de una raiz y un numero m")
a =input("Indice= ")
b =input("Radicando= ")

a= float(a)
b= float(b)


d=(1/a)**b
g=b**(1/a)

if a==0:
	print("El resultado de la raiz es igual a= ",a)
if a==1:
	print("El resultado de la raiz es igual a= ",b)
if a>0 and b>0:
	print("El resultado de la raiz es igual a= ",d)
if a>0 and b<0:
	b=-b
	bandera=1
if bandera==1:
	print("El resultado es imaginario")
	print(g,"i")
