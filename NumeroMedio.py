print("Introduzca 3 numeros.\n")
a= input("Primer Numero= \n")
b= input("Segundo Numero= \n")
c= input("Tercer Numero= \n")

a= int(a)
b= int(b)
c= int(c)
if a==b and b==c and c==a:
	print("Los numeros son iguales")
if (a>b and b>c) or (a<b and b<c):
	print("El numero del medio es= \n")
	print(b)
if (b>a and a>c) or (b<a and a<c):
	print("El numero del medio es= \n")
	print(a)
if (c>a and b>c) or (c<b and a<c):
	print("El numero del medio es= \n") 
	print(c)
