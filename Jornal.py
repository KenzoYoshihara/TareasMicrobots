print("Bienvenido, introduzca los siguientes datos")
a =input("Horas trabajadas= ")
b =input("Tarifa para hora= ")

a =int(a)
b =int(b)

c =int(a)*int(b)
d =int(a)*int(b)*0.03
e =c-d

print("El total ganado es de Bolivianos= ")
print(c)
print("El valor del descuento es de Bolivianos= ")
print(d)
print("El Pago neto es de Bolivianos= ")
print(e)
