# Basic while
count = 1;
while count <= 5:
    print(count)
    count += 1

# Infinite while loop
while True:
    command = input("Type 'exit' to exit: ")
    if command == 'exit':
        break
    print("You typed:", command)

# Simulating a do-while loop
count = 1
while True:
    number = int(input("Please enter a positive number: "))
    if number > 0:
        print("You entered:", number)
        break
    print("That's not a positive number. Try again.")

# While-else loop
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("Counting finished.")