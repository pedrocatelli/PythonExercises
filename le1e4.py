salary = float(input())
taxes = 0

if salary > 0.00 and salary <= 2000.00:
    print("Isento")
elif salary > 2000.00 and salary <= 3000.00:
    taxes = (salary-2000.00)*0.08
    print("R$ %.2f" % taxes)
elif salary > 3000.00 and salary <= 4500.00:
    taxes = (3000.00-2000.00)*0.08 + (salary-3000.00)*0.18
    print("R$ %.2f" % taxes)
elif salary > 4500.00:
    taxes = (3000.00-2000.00)*0.08 + (4500.00-3000.00)*0.18 + (salary-4500.00)*0.28
    print("R$ %.2f" % taxes)