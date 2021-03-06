def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


while True:
    try:
        num = int(input("Give me an Integer and I will check if any number between 1 and it inclusive is prime."))
    except ValueError:
        print("Please use a valid integer.")
        continue
    for i in range(num):
        if isPrime(i):
            print(str(i) + " is prime.")
    if not isPrime(num):
        print(str(num) + " is not prime.")
    flag = input("continue? (y/n)")
    if flag.upper() == "N" or flag.upper() == "NO":
        break
	
