count = 0
def increment_count():
    global count
    count += 1
    print("Count incremented to:", count)
increment_count()
print("Final count value:", count)