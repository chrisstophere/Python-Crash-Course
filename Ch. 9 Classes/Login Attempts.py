class User:
    """Prints information about users"""
    def __init__(self, first_name, last_name, age, race,):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.race = race
        self.login_attempts = 0
        
    def describe_user(self):
        """Prints a formatted list of the user details"""
        print("Here are the user's details:")
        print(f"First name: {self.first.title()}")
        print(f"Last name: {self.last.title()}")
        print(f"Race: {self.race}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        """Prints a simple greeting to the user"""
        name = self.first + " " + self.last 
        print(f"Welcome {name.title()}.\n")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0    
        
user1 = User('chris', 'ewen', 46, 'white')
user2 = User('tina', 'ewen', 45, 'redneck')
user3 = User('jacob', 'ewen', 12, 'kid')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)