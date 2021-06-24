import math
 
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2-4*a*c

if delta == 0:
	x_prim = (-b + math.sqrt(delta))/(2*a)
	print ("A única raiz é: ", x_prim)
else:
        if delta < 0:
                print ("Essa equação não possui raizes reais")
        else:
                x_prim = (-b + math.sqrt(delta))/ (2*a)
                x_seg = (-b - math.sqrt(delta))/ (2*a)
                print ("As raizes dessa equação são: ", x_prim, "e", x_seg)

        
	
