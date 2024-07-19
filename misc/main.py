def checkForNegatives(number):
    if number >= 0:
        print('not negative')
        return False
    elif number < 0:
        print('negative')
        return True
    
inputNumber = 10

if checkForNegatives(inputNumber):
    print('it is indeed a negative')