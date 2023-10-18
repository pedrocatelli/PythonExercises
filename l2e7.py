L = int(input())
T = input()

M = []
for number in range(144):
    M.append(float(input()))

start_position = L * 12
soma = 0
for count in range(start_position, start_position + 12):
    soma = soma + M[count]
    
if T == "S":
    print(soma)
elif T == "M":
    avg = soma/12
    print(avg)