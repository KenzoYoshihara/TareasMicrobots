print("Bienvenido al sistema de pago de empleados.")
a =input("Introduzca la cantidad de años que trabaja en la empresa= ")

a =float(a)

if a<5:
	b= 2000+2000*0.1
	print("El total de pago es= ",b," Bs")
if a>=5 and a<10:
	b=2000+2000*0.15
	print("El total de pago es= ",b," Bs")
if a>=10 and a<15:
	b=2000+2000*0.25
	print("El total de pago es= ",b," Bs")
if a>=15:
	b=2000+2000*0.5
	print("El total de pago es= ",b," Bs")
else:
	print("Error")
