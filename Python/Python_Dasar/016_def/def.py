def sayHello():
    print("Hello my name is John Doe")
    print("Hello World!");

# call sayHello function
sayHello()


# function with parameter and return value
def mathPlus(num1, num2):
    result = num1 + num2
    return result

print(mathPlus(10, 10))


# function with default value
def multiplePlus(num1, num2, dfltNum = 20):
    return num1 * num2 + dfltNum

print(multiplePlus(30, 30))