# Assignment Expression
numbers = [10, 20, 30, 40, 50]
if (n := len(numbers)) > 3:
    print(f"The list has {n} elements, which is more than 3.")

# Martrix Multiplication
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A @ B
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix C (A @ B):\n", C)

# Unary
x = 5
print("Unary plus:", +x)
print("Unary minus:", -x)
print("Unary negation:", ~x)
print("Logical NOT:", not x)

# Operators on strings
first_name = "John"
last_name = "Doe"
print("Concatenation:", first_name + " " + last_name)
print("Repetition:", first_name * 3)

# Precedence and Associativity
result = 2 + 3 * 4
print("Result of 2 + 3 * 4:", result)