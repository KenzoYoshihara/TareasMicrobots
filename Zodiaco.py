print("Introduzca su dia y mes de nacimiento\n")
dia =input("Dia: ")
mes =input("Mes: ")

dia =int(dia)
mes =int(mes)

if dia>=1 and dia<=31:
	print("El dia es correcto")
	if mes>=1 and mes<=12:
		print("El mes es correcto\n\n")
		if (mes==3 and dia>=21):
			print("El signo es Aries")
		if (mes==4 and dia<=20):
			print("El signo es Aries")

		if (mes==4 and dia>=21):
			print("El signo es Tauro") 
		if (mes==5 and dia<=21):
			print("El signo es Tauro")

		if (mes==5 and dia>=22):
			print("El signo es Geminis")
		if (mes==6 and dia<=21):
			print("El signo es Geminis")

		if (mes==6 and dia>=22): 
			print("El signo es Cancer")
		if (mes==7 and dia<=22):
			print("El signo es Cancer")

		if (mes==7 and dia>=23): 
			print("El signo es Leo")
		if (mes==8 and dia<=23):
			print("El signo es Leo")

		if (mes==8 and dia>=24):
			print("El signo es Virgo")
		if (mes==9 and dia<=23):
			print("El signo es Virgo")

		if (mes==9 and dia>=24):
			print("El signo es Libra") 
		if (mes==10 and dia<=23):
			print("El signo es Libra")

		if (mes==10 and dia>=24): 
			print("El signo es Escorpio")
		if (mes==11 and dia<=22):
			print("El signo es Escorpio")

		if (mes==11 and dia>=23):
			print("El signo es Sagitario")
		if (mes==12 and dia<=21):
			print("El signo es Sagitario")

		if (mes==12 and dia>=22): 
			print("El signo es Capricornio")
		if (mes==1 and dia<=20):
			print("El signo es Capricornio")

		if (mes==1 and dia>=21): 
			print("El signo es Acuario")
		if (mes==2 and dia<=19):
			print("El signo es Acuario")

		if (mes==2 and dia>=20):
 			print("El signo es Piscis")
		if (mes==3 and dia<=20):
			print("El signo es Piscis")

	else:
		print("El mes es incorrecto")
else:
	print("El dia es incorrecto")	
