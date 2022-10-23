change_required = int(input())

if change_required <= 0:
    print('No change')

while change_required != 0:   
    if (change_required >= 100):
        dollars = change_required // 100
        change_required = change_required % 100
        if dollars == 1:
            print(f'{dollars} Dollar')
        else: 
            print(f'{dollars} Dollars')
            
    if (change_required >= 25):
        quarters = change_required // 25
        change_required = change_required % 25
        if quarters == 1:
            print(f'{quarters} Quarter')
        else:
            print(f'{quarters} Quarters')
            
    if (change_required >= 10):
        dimes = change_required // 10
        change_required = change_required % 10
        if dimes == 1:
            print(f'{dimes} Dime')
        else:
            print(f'{dimes} Dimes')
            
    if (change_required >= 5):
        nickels = change_required // 5
        change_required = change_required % 5
        if nickels == 1:
            print(f'{nickels} Nickel')
        else:
            print(f'{nickels} Nickels')
            
    if (change_required > 0):
        pennies = change_required
        change_required -= change_required
        if pennies == 1:
            print(f'{pennies} Penny')
        else:
            print(f'{pennies} Pennies')
    
    