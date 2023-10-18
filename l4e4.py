numbers = []

while True:
    number = int(input())
    if number == 0:
        break
    numbers.append(number)

for number in numbers:
    matrix = [[1] * number for _ in range(number)]

    camada = 1
    n = number
    while camada <= n // 2:
        for i in range(camada, n - camada):
            for j in range(camada, n - camada):
                matrix[i][j] = camada + 1
        camada += 1

    for row in matrix:
        for value in row:
            print(value, end="   ")
        print()
    print()
