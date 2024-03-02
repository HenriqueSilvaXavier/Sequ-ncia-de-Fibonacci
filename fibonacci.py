n=int(input("Quantos números da sequencia de fibonacci mostrar? "))
i1=0
i2=1
cont=0
if n==1:
	print(i1)
if n==0:
	print()
elif n>1:
	print("{} {}".format(i1, i2), end=" ")
	for k in range(2,n):
	   	if k%2==0:
	   		i1=i1+i2
	   		print(i1, end=" ")
	   	if k%2==1:
	   		i2=i2+i1
	   		print(i2, end=" ")