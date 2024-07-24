n = int(input('NUMERO: '))
print(f"valor do N eh: {n}")

def fibonacci(n):
    
    if n == 1:
        print(1)
        return 1
    elif n == 2:
        print(1)
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)

c = fibonacci(n)
