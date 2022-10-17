gross_income = float(input('Enter the gross income: '))
deps = int(input('Enter number of dependents: '))
std_ded = 10000

if deps == 0:
    net_income = gross_income - std_ded
    tax = net_income * 0.20
    print(f'The income tax is: ${tax}')
else:
    bonus_ded = 3000 * deps 
    net_income = gross_income - std_ded - bonus_ded
    tax = net_income * 0.20
    print(f'The income tax is ${tax}')

