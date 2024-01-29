
marks = float(input('Enter marks - '))

print(marks)

if marks>=0 and marks<35:
    print('Fail')
    print('Candidate got failed')

elif marks>=35 and marks<=100:
    print('Pass')

    if marks>=35 and marks<60:
        print('Candidate is average.')

    elif marks>=60 and marks<70:
        print('Candidate is good.')

    elif marks>=70 and marks<90:
        print('Candidate is distinct.')

    elif  marks>=90 and marks<=100:
        print('Candidate is excellent and bright student.')

elif marks>100:
    print('Bro You are not Chirag')

else:
    print('Enter Valid marks')