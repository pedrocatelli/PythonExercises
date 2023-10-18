N = []

for i in range(20):
    Y = int(input())
    N.append(Y)
    
i = 19
for count in range(10):
    Y = N[count]
    N[count] = N[i]
    N[i] = Y
    i -= 1
    
for count in range(20):
    print(f"N[{count}] = {N[count]}")