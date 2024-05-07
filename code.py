# Create a file named 'fibonacci.py' and write the following code in it
with open('fibonacci.py', 'w') as file:
    file.write("def fibonacci(n):\n")
    file.write("    fib_sequence = [0, 1]\n")
    file.write("    while len(fib_sequence) < n:\n")
    file.write("        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n")
    file.write("    return fib_sequence\n")

# Import the newly created module and use the fibonacci function
import fibonacci

# Generate the Fibonacci sequence up to the 10th number
fib_sequence = fibonacci.fibonacci(10)
print("Fibonacci Sequence:", fib_sequence)
