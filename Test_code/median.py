import statistics
Fnumber=int(input('Input the first Number: '))
Snumber=int(input('Input the second number'))
Tnumber=int(input('Input the third number'))

allNumber=[Fnumber,Snumber,Tnumber]
print(statistics.median(allNumber),'is meadian number')