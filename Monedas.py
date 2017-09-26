print("Introduzca la cantidad de monedas que posee")
a =input("Monedas de Bs 5 = \n")
b =input("Monedas de Bs 2 = \n")
c =input("Monedas de BS 1 = \n")
d =input("Monedas de 50 centavos = \n")
e =input("Monedas de 20 centavos = \n")
f =input("Monedas de 10 centavos = \n")

a =int(a)
b =int(b)
c =int(c)
d =int(d)
e =int(e)
f =int(f)

a= a*5
b= b*2
c= c*1
d= (d*0.50)
e= (e*0.20)
f= (f*0.10)
z= a+b+c+d+e+f
print("La cantidad de Bolivianos que posee es de= ",z," Bs")
