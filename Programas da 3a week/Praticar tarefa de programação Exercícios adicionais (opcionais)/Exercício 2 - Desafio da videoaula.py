import math
 
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2-4*a*c

if delta == 0:
	x_prim = (-b + math.sqrt(delta))/(2*a)
	print ("a raiz desta equação é", x_prim)
else:
        if delta < 0:
                print ("esta equação não possui raízes reais")
        else:
                x_prim = (-b + math.sqrt(delta))/ (2*a)
                x_seg = (-b - math.sqrt(delta))/ (2*a)
                if x_prim < x_seg:
                        menor = x_prim
                        maior = x_seg
                        print ("as raízes da equação são", menor, "e", maior)
                else:
                        menor = x_seg
                        maior = x_prim
                print ("as raízes da equação são", menor, "e", maior)
			

