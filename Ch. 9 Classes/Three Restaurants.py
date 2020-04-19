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

ital_restaurant = Restaurant("luigi's", 'italian')
bbq_restaurant = Restaurant("bubba's", 'american')
mex_restaurant = Restaurant("paco's", 'mexican')

ital_restaurant.describe_restaurant()
bbq_restaurant.describe_restaurant()
mex_restaurant.describe_restaurant()