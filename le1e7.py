from math import floor

N = int(input())

cem = floor(N/100)
cinquenta = floor((N % 100)/50)
vinte = floor(((N % 100) % 50) / 20)
dez = floor((((N % 100) % 50) % 20) / 10)
cinco = floor(((((N % 100) % 50) % 20) % 10) / 5)
dois = floor((((((N % 100) % 50) % 20) % 10) % 5) / 2)
um = floor((((((N % 100) % 50) % 20) % 10) % 5) % 2)

value = ["100,00", "50,00", "20,00", "10,00", "5,00", "2,00", "1,00"]
notas = [cem, cinquenta, vinte, dez, cinco, dois, um]

print(N)

for i in range(7):
    print(f"{notas[i]} nota(s) de R$ {value[i]}")