def fibonachi(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return fibonachi(x - 2) + fibonachi(x - 1)


while True:
    try:
        terms = int(input("give the desired number of terms in the fibonachi sequence."))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    for i in range(terms + 1):
        print("Fibonachi[" + str(i) + "] " + str(fibonachi(i)))
    flag = input("continue? (y/n)")
    if flag.upper() == "N" or flag.upper() == "NO":
        break
