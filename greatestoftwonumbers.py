def greatest_of_two_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

greatest = greatest_of_two_numbers(number1, number2)
print("The greatest number is:", greatest)