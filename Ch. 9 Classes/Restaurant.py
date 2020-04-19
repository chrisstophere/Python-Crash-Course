class Restaurant:
    """A simple attemp to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and type of cuisine it has"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Prints a description of the restaurant"""
        print(
                f"{self.name.title()} serves {self.type.title()} food."
                )

    def open_restaurant(self):
        """Prints a message stating that the restaurant is open"""
        print(f"{self.name.title()} is open.")

restaurant = Restaurant("luigi", 'italian')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()