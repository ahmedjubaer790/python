marks=int(input("Enter your marks: "))
if marks>=93:
    print('Grade is A Excellent')
elif marks>=90 and marks<93:
    print('Grade is A-')
elif marks>=87 and marks<90:
    print('Grade is B+')
elif marks>=83 and marks<87:
    print('Grade is B good')
elif marks>=80 and marks<83:
    print('Grade is B-')
elif marks>=77 and marks<80:
    print('Grade is C+')
elif marks>=73 and marks<77:
    print('Grade is C Average')
elif marks>=70 and marks<73:
    print('Grade is C-')
elif marks>=67 and marks<70:
    print('Grade is D+')
elif marks>=60 and marks<67:
    print('Grade is D poor')
else:
    print('F* Failure')