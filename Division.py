print("Introduzca dos valores para realizar una division\n")
a =input("a= ")
b =input("b= ")

a =float(a)
b =float(b)

if a==0 or b==0:
	print("Error")
c=a/b
print("El resultado de la division entre= ",a,"y",b,"Es igual a=")
print(c)
