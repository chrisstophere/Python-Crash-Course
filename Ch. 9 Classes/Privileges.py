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
        self.privileges = Privileges() 


class Privileges():
    """Contains all the privileges for Admins or Users"""
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        """Run thru the list of privileges the Admin user has"""
        print(f"The Admin user can do the following things:")
        if self.privileges:  
            for privilege in self.privileges:
                print(f"\t-{privilege.title()}")
        else:
                print("- This user has no privileges.")              
        

chris = Admin('chris', 'ewen', 46, 'caucasion')
chris.describe_user()
chris.privileges.show_privileges()

print("\nAdding privileges...")

chris_privileges = [
                        "can add posts", "can delete posts",
                        "can ban users", "can reboot servers"
                        ]
chris.privileges.privileges = chris_privileges
chris.privileges.show_privileges()