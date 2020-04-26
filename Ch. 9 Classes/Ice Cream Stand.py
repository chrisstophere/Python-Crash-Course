class Restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and type of cuisine it has"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a description of the restaurant"""
        print(
                f"{self.name.title()} serves {self.type.title()} food."
                )

    def open_restaurant(self):
        """Prints a message stating that the restaurant is open"""
        print(f"{self.name.title()} is open.")
        
    def served_customers(self):
        """Prints how many customers have been served"""
        print(f"{self.name.title()} has served {self.number_served} customers.")

    def set_number_served(self, number_served):
        """Set the number of customers to the given value"""
        self.number_served = number_served
        
        
class IceCreamStand(Restaurant):
    """Describes an Ice Cream Stand's stuff"""
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
        
    def list_flavors(self):
        """Print a statement that lists the Ice Cream flavors"""
        for flavor in self.flavors:
            print(f"We have {flavor.title()} ice cream.")    

# Call the method IceCreamStand
restaurant = IceCreamStand("Frosty's", "deserts")
restaurant.list_flavors()