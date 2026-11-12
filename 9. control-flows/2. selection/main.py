# Basic match-case statement
day = 3;
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# Multiple values in a single case
days = "Saturday";
match days:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday.")
    case _:
        print("Invalid day")

# Match-case with guards
role = "admin"
is_active = True
match role:
    case "admin" if is_active:
        print("Admin user is active.")
    case "admin":
        print("Admin user is not active.")
    case "user" if is_active:
        print("Regular user is active.")
    case _:
        print("Unknown role or inactive user.")

# Matching tuples
point = (2, 3)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Point is on the x-axis at x={x}")
    case (0, y):
        print(f"Point is on the y-axis at y={y}")
    case (x, y):
        print(f"Point is at coordinates ({x}, {y})")

# Matching lists
numbers = [1, 2, 3]
match numbers:
    case []:
        print("Empty list")
    case [one]:
        print(f"List with one element: {one}")
    case [one, two]:
        print(f"List with two elements: {one}, {two}")
    case [one, *two]:
        print(f"List with one element: {one} and the rest: {two}")

# Matching dictionaries
person = {"name": "Alice", "age": 30}
match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case {"name": name}:
        print(f"Name: {name}, Age not provided")
    case _:
        print("Invalid person data")