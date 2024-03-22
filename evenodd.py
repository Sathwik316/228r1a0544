def is_even_odd(number):
    if (number%2 == 0):
        return True
    else:
        return False

number = int(input("Enter the number: "))

if is_even_odd(number):
    print(number, "is even.")
else:
    print(number, "is odd.")