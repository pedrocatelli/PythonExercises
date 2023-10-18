X = int(input())
Y = int(input())

sum = 0

if Y < X:
    C = X
    X = Y
    Y = C

for i in range(X+1, Y):
    if i % 2 == 1:
        sum = sum + i

print(sum)