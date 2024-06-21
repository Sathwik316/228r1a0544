def is_perfect_number(number):
    if number <= 0:
        return False

    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum == number

# Example usage:
user_input = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(user_input):
    print(f"{user_input} is a perfect number.")
else:
    print(f"{user_input} is not a perfect number.")