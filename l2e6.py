N = int(input())

numbers = input().split()

X = []
for count in range(N):
    X.append(int(numbers[count]))

smallest = X[0]
s_position = 0
i = 0

for number in X:
    if smallest > number:
        smallest = number
        s_position = i
    i += 1

print(f"Menor valor: {smallest}")
print(f"Posicao: {s_position}")