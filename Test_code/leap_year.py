take_year=int(input('Enter year you want to check: '))

if (take_year %400==0) or (take_year %100!=0 and take_year % 4==0):
    print(take_year,' year is leap year')
else:
    print(take_year,' year is not the leap year')