class User:
    """Prints information about users"""
    def __init__(self, first_name, last_name, age, race):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.race = race
        
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
        
class Admin(User):
    """Describes the Administrator user"""
    def __init__(self, first_name, last_name, age, race):
        """
        Initializes attributes of the parent class
        Then initializes attributes specific to an Admin user
        """
        super().__init__(first_name, last_name, age, race)
        self.privileges = []
        
    def show_privileges(self):
        """Run thru the list of privileges the Admin user has"""
        print(f"The Admin user can do the following things:")  
        for privilege in self.privileges:
            print(f"\t-{privilege.title()}")
            
        
user1 = User('emily', 'mayes', 20, 'white')
user2 = User('tina', 'ewen', 45, 'redneck')
user3 = User('jacob', 'ewen', 12, 'kid')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

adminUser = Admin('chris', 'ewen', 46, 'caucasion')
adminUser.privileges = [
                        "can add posts", "can delete posts",
                        "can ban users", "can reboot servers"
                        ]
adminUser.show_privileges()