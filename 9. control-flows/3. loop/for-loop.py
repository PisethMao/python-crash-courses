# For loop
for i in range(5):
    print(i)

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Interate over a string
for letter in "hello":
    print(letter)

# Iterate over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# For loop with enumerate
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# For loop with zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# For-else loop
for i in range(3):
    print(i)
else:
    print("Loop completed without break.")