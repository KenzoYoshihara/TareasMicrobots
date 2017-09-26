print("Sistema de calificaciones Standard Grading System\n Calificacion= 9-10	A	Sobresaliente\n Calificacion= 7-8	B	Muy Bueno\n Calificacion= 6	C	Bueno\n Calificacion= 5	D	Promedio\n Calificacion= 4	E	Pobre\n Calificacion= 3-1	F	Aplazo\n")
print("Bienvenido al Sistema de calificaciones, Introduzca su nota.\n")
a= input("Nota final= ")
a = int(a)

if a>=1 and a<=10:
	if a>=9:
		print("Su calificacion en el Standard Grading System es A, Sobresaliente\n Has demostrado mucha capacidad en ti,continua en la excelencia.")
	if a==7 or a==8:
		print("Su calificacion en el Standard Grading System es B, Muy bueno\n felicitaciones, aun puedes demostrar mucho mas, busca la excelencia.")
	if a==6:
		print("Su calificacion en el Standard Grading System es C, Bueno\n Vamos, no te quedes conforme puedes mejorar.")
	if a==5:
		print("Su calificacion en el Standard Grading System es D, Promedio\n Demuestra que vales mas, eres una persona bastante sabia pero sin motivacion.")
	if a==4:
		print("Su calificacion en el Standard Grading System es E, Pobre\n No seas mediocre y mejora, No te conformes con esta nota.")
	if a>=1 and a<=3:
		print("Su calificacion en el Standard Grading System es F, Aplazado\n No te rindas, debes mejorar, sabes mucho mas que esta calificacion.")
else:
	print("Valor de la calificacion no valida.")
