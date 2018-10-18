#import math
#A = float(input("A= "))
#B = float(input("B= "))
#C = float(input("C= "))


#delta = (B*B)-(4*A*C)

#if(delta >= 0):
#	raiz1 = ((-B) + math.sqrt(delta))/(2*A)
#	raiz2 = ((-B) - math.sqrt(delta))/(2*A)
#	print("raiz1 = " + str(raiz1) + "\nraiz2 = "+ str(raiz2)) 
#else:
#	print("Raizes nao existem")


#A = int(input("numero = "))
#n = 1
#for numero in range(A,0,-1):
#	n = numero * n

#print(str(n))


alt = int(input("altura = "))

larg = int(input("largura = "))
j = 0
i = 0
string = []
for i in range(0,alt):
	for j in range(0,larg):
		if(i==0 or i == alt-1 or j==0 or j==larg-1):
			string.append("#")
		else:
			string.append(" ")
	print(string)
	string = []
