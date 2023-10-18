O = input()
L = []

for i in range(144):
    L.append(float(input()))

colls_qtd = 11
soma = 0

for i in range(0, 132, 12):
    coll = 12 - colls_qtd
    for j in range(colls_qtd):
        soma += L[i+coll]
        coll += 1
    colls_qtd -= 1

if O == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/66))
    