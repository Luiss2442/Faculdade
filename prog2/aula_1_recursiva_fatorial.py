a = 5

def fatorial(a):
    if (a == 1):
        return 1
    return a * fatorial(a-1)

a = fatorial(a)
print(a)