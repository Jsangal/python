print("Hola")

def factorial(num):
    if (num <= 2):
        return num * 1
    else:
        return num * factorial(num-1)

print(factorial(5))

def tabla(a):
    for i in range(1,11):
        print(a, " por ", i, "=", a*i)

print(tabla(1))
