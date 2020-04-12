def city_country(city, state):
    return f'"{city.title()}, {state.title()}"'

place = city_country('danville', 'va')
print(place)