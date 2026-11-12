# ============================
# PRACTICE SHEET: LIST
# ============================
shopping_list = ["milk", "apple", "rice", "milk", "banana"]
print("Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list), "\n")

shopping_list.append("eggs")
shopping_list.insert(1, "bread")
shopping_list.remove("milk")
print(shopping_list, "\n")

print("Does milk still exist?", "milk" in shopping_list)
print("Total remaining items:", len(shopping_list), "\n")

for item in shopping_list:
    print(item)
print("Total items after loop:", len(shopping_list), "\n")

removed_item = shopping_list.pop()
print("Removed item:", removed_item)
print("Updated list:", shopping_list, "\n")

unsorted_list = shopping_list.copy()
shopping_list.sort()
print("Sorted list:", shopping_list)
print("Unsorted copy:", unsorted_list, "\n")





# ============================
# PRACTICE SHEET: TUPLE
# ============================
student = ("Dara", 20, "Computer Science", "Year 3")
print("Student Name:", student[0])
print("Major:", student[2])
print("Total Items:", len(student))
print("Student Year:", student[-1])

courses = ("Python", "Database", "Networking", "Python", "Web Development")
print("\nPython Count:", courses.count("Python"))
print("Networking Index:", courses.index("Networking"), "\n")
for course in courses:
    print(course)

registered_courses = ("Python", "Database", "Networking")
courses_list = list(registered_courses)
courses_list.append("Cloud Computing")
registered_courses = tuple(courses_list)
print("\nUpdated Courses:", registered_courses, "\n")





# ============================
# PRACTICE SHEET: SET
# ============================
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}
new_files = today - yesterday
deleted_files = yesterday - today
print("New files:", sorted(new_files))
print("Deleted files:", sorted(deleted_files), "\n")

unchanged_files = yesterday & today
print("Unchanged files:", sorted(unchanged_files), "\n")

all_changes = yesterday ^ today
print("All changes:", sorted(all_changes), "\n")

all_files = yesterday | today
print("All files ever seen:", sorted(all_files), "\n")





# ============================
# PRACTICE SHEET: DICTIONARY
# ============================
inventory = {
    "Apple": 20,
    "Banana": 15,
    "Orange": 30
}
stock = inventory.get("Mango", "Product not found\n")
print("Mango:", stock)

inventory.update({
    "Mango": 10,
    "Grape": 25
})
inventory.update({"Apple": 50})
print(inventory, "\n")

for product, stock in inventory.items():
    print(f"{product}: {stock}")

inventory.pop("Banana")
print(inventory, "\n")

inventory.setdefault("Pineapple", 12)
print(inventory)

total_stock = sum(inventory.values())
print("\nTotal stock:", total_stock)

backup = inventory.copy()
inventory.clear()
print("\nOriginal inventory:", inventory)
print("Backup inventory:", backup)