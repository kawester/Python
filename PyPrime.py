def isPrime(x):
	if(x<1):return False
	for i in range(2,x):
		if(x%i==0):
			return False
	return True

while(isPrime(1)):
	try:
		num=int(input("Give me an Integer and I will check if any number between 1 and it inclusive is prime."))
	except:
		print("Please use a valid Integer.")
		continue
	for i in range(num):
		if(isPrime(i)):
			print(str(i)+" is prime.")
	if(not isPrime(num)):
			print(str(num)+" is not prime.")
	flag=input("continue? (y/n)")
	if(flag.upper()=="N" or flag.upper()=="NO"): break