class User:
    company = "ISTAD"  # Class variable shared by all instances
    def __init__(self, name):
        self.name = name  # Instance variable unique to each instance
        self.count = 0    # Instance variable unique to each instance
user1 = User("Alice")
user2 = User("Bob")
print(user1.company)  # Output: ISTAD
print(user2.company)  # Output: ISTAD