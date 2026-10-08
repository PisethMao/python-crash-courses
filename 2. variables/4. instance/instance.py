class User:
    def __init__(self, name):
        self.name = name
        self.count = 0
user1 = User("Alice")
user2 = User("Bob")
print(user1.name)  # Output: Alice
print(user2.name)  # Output: Bob