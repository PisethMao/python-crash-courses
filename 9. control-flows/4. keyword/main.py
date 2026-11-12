# Break - stop the loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Continue - skip the current iteration
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Pass - do nothing
for i in range(1, 11):
    if i == 5:
        pass
    print(i)

# Return - exit the function and return a value
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))