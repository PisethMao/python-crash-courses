numbers = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
]

print(numbers[0][1][2])
print(numbers[1][0][1])
print(numbers[1][1][0])
print(numbers[0][0][0])

for matrix in numbers:
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()  # Move to the next line after each row
    print()  # Move to the next line after each matrix