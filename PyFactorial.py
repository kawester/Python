def factorial(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac


while True:
    try:
        answer = int(input("enter a number to get its factorial series."))
    except ValueError:
        print("Please use a valid integer.")
        continue
    for i in range(1, answer + 1):
        print("factorial[" + str(i) + "] " + str(factorial(i)))
    flag = input("continue? (y/n)").upper()
    if flag == "N" or flag == "NO":
        break
