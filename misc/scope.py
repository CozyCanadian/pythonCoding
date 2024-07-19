exampleVar = "one" #Global variable

def exampleFunction():
    exampleVar2 = "two" #Local variable
    print(exampleVar2)
    print(exampleVar2) #Can access global variable

def exampleFunction2():
    print(exampleVar)

exampleFunction()
exampleFunction2()
