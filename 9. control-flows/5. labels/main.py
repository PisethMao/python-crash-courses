# Normal nested breaks
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(f"i: {i}, j: {j}")

# Exit both loops using a label
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(f"i: {i}, j: {j}")
    else:
        continue
    break

# Exit nested loops using return
def nested_loops():
    for i in range(5):
        for j in range(5):
            if j == 3:
                return
            print(f"i: {i}, j: {j}")
nested_loops()