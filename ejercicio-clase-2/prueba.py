with open("bases.txt" , "r") as file:
    base = [int(line.strip()) for line in file]

factor = [2, 3, 4]

for x in base:
    pol = 0
    for exp in range(0, 3):
        pol = pol + factor[exp] * pow(x, exp)
        print(exp, pow(x, exp), factor[exp])
    print("Valor: " + str(x) + " polinomio :" + str(pol))