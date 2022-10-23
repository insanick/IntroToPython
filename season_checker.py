input_month = input()
input_day = int(input())

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
days = []
for day in range(1,32):
    days.append(day)
month30 = ['april', 'june', 'september', 'november']

    

if input_month.lower() in months and input_day in days:
    if input_month.lower() in month30 and input_day == 31:
        print('Invalid')
    elif input_month.lower() == 'february' and input_day > 28:
        print('Invalid')
    elif input_month.lower() == ('april') or input_month.lower() == ('may'):
        print('Spring')
    elif input_month.lower() == ('july') or input_month.lower() == ('august'):
        print('Summer')
    elif input_month.lower() == ('october') or input_month.lower() == ('november'):
        print('Autumn')
    elif input_month.lower() == ('january') or input_month.lower() == ('february'):
        print('Winter')
        
    elif (input_month.lower() == 'march' and input_day >= 20) or (input_month.lower() == 'june' and input_day <= 20):
        print('Spring')
    elif (input_month.lower() == 'june' and input_day > 20) or (input_month.lower() == 'september' and input_day <= 21):
        print('Summer')
    elif (input_month.lower() == 'september' and input_day >= 22) or (input_month.lower() == 'december' and input_day <= 20):
        print('Autumn')
    elif (input_month.lower() == 'december' and input_day >= 21) or (input_month.lower() == 'march' and input_day <= 19):
        print('Winter')
else:
    print('Invalid')
