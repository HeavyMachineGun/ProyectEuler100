def mul_3_5():
	sum=0
	for i in range(0,1000):
		if i%3==0 or i%5==0:
			sum+=i
	print(sum)
def fibo():
	a,b,i=1,2,0
	sum=2
	while a<4000000:
		a,b=b,b+a
		if(a%2==0):
			sum=sum+a
	print(sum)


