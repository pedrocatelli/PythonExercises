numbers = input()

numbers = numbers.split()

A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])

maior1 = ((A+B+abs(A-B)))/2
maior2 = int(((maior1+C+abs(maior1-C)))/2)

print(f"{maior2} eh o maior")