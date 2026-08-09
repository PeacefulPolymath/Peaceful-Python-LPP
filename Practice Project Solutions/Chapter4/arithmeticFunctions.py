def plus_one(number):
    return number + 1
def add(number1 , number2):
    totalsum = number1
    for i in range(number2):
        totalsum = plus_one(totalsum)
    return totalsum
def multiply(num1 , num2):
    product = 0
    for a in range(num2):
        product = add(product , num1)
    return product


print(multiply(2 , 3))