a = 1
b = 2
c = 3

v = [0]*11      # Definimos o vetor
a = 0           # Definimos o valor de A
while a <= 10:  # Repetimos de 0 a 11
    v[a] = a    # v[posicao] = a
    print(f"A: {a}; Vetor[{a}] = {v[a]}")
    a += 1      # Incremento de A
