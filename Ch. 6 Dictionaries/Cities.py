# Create a dictionary named cities
# Use the names of 3 cities as keys
# Create a dictionary of info about each city...
# Include the country it's in, approx. pop...
# And 1 thing about the city
# Ex. keys...country, population, and fact\landmark
cities = {
    'philadelphia': {
        'country': 'USA',
        'population': 158_000_000,
        'landmark': 'liberty bell',
                    },
    'danville': {
        'country': 'USA',
        'population': 41_898,
        'landmark': 'a brown river',
                },
    'paris': {
        'country': 'France',
        'population': 215_000_000,
        'landmark': 'eiffel tower',
             }
         }

# Print the name of each city and all the info stored about it
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    landmark = city_info['landmark'].title()
    print(f"The city: {city.title()}\n{country}\n{population}\n{landmark}")