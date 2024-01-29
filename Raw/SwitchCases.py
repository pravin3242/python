marks = float(input('Enter Percentage : - '))

match marks:
    case marks if 0 <= marks <35:
        print('Fails')

    case marks if 35 <= marks <=100:
        print('Pass')
        if marks >= 35 and marks < 60:
            print('Candidate is average. ')

        elif marks >=60 and marks <70:
            print('Candidate is good. ')

        elif marks >=70 and marks <90:
            print('Candidate is distinct. ')
            
        elif marks >=90 and marks<=100:
            print('Candidate is excellent and bright student.')


