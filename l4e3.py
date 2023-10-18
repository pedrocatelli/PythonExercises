O = input()

L = []
soma = 0

for i in range(144):
    L.append(float(input()))

lin = 7
col = 0
positions = 2

while lin <= 11:
    if lin == 7:
        col = 5
    elif lin == 8:
        col = 4
    elif lin == 9:
        col = 3
    elif lin == 10:
        col = 2
    elif lin == 11:
        col = 1
    j = lin*12
    for i in range(positions):
        soma += L[j+col]
        col += 1
    lin += 1
    positions += 2

if O == 'S':
    print("%.1f" % soma)
else:
    avg = soma/30
    print("%.1f" % avg)