def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]  # Calculate the next Fibonacci number
        sequence.append(next_num)
    return sequence

num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = fibonacci_sequence(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fib_sequence)