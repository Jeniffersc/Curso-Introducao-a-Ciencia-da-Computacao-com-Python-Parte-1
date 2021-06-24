import math

x1 = int(input("Digite o primeiro x: "))
y1 = int(input("Digite o primeiro y: "))
x2 = int(input("Digite o segundo x: "))
y2 = int(input("Digite o segundo y: "))

dis = math.sqrt ((x1 - x2)**2 + (y1 - y2)**2)

if dis > 10:
	print("longe")

else:
	print ("perto")

