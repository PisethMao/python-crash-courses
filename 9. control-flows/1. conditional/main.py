age = 21;
score = 85;
username = "John Doe"
password = "password123"

# Simple if statement
if age >= 18:
    print("You are an adult.")
print("This line will always be executed.")

# If-else statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# If-elif-else statement
if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("You got a D.")
elif score >= 50:
    print("You got an E.")
else:
    print("You failed the exam.")

# Nested if statement
if username == "John Doe":
    if password == "password123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")