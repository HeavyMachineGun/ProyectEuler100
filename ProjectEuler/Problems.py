
#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
def mul_3_5():
	sum=0
	for i in range(0,1000):
		if i%3==0 or i%5==0:
			sum+=i
	print(sum)


#Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be:
#										1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.
def fibo():
	a,b,sum=1,2,2
	while a<4000000:
		a,b=b,b+a
		if(a%2==0):
			sum=sum+a
	print(sum)


#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
class PrimeFactors:
	
	def __init__(self, *args, **kwargs):
		#list where we'll save the prime numbers at run time
		self.primeNumbers=[2]

	#it adds prime number at runtime as it is nedded
	# Sieve of Eratosthenes algorithm
	def generatePrimes(self,number):
		lenght=len(self.primeNumbers)
		lastPrime=self.primeNumbers[lenght-1]
		listNumbers= [val for val in range(lastPrime,lastPrime+number)]
		for value in listNumbers:
			listNumbers=list(filter( lambda x:  x==value or (not x%value==0),listNumbers))
		self.primeNumbers=listNumbers[1:len(listNumbers)]
		
	def primeFactorsNumber(self,value):
		#generates the prime numbers to 30
		primeFactors=[]
		while value>1:
			self.generatePrimes(10)
			for prime in self.primeNumbers:
				if(value%prime==0):
					value=value/prime
					if(primeFactors.count(prime)==0):
						primeFactors.append(prime)
		print(primeFactors)
		print(primeFactors[len(primeFactors)-1])
		
