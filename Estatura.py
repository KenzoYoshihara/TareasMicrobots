print("Introduzca su estatura en centimetros.\n")
a =input("Estatura= ")
a =int(a)

if a<=150:
	print("Persona de estatura baja.")
if a>=151 and a<=170:
	print("Persona de estatura media.")
if a>=171:
	print("Persona de estatura alta.")
	
