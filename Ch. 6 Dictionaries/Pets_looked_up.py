# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.

pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# print each item in the list in the form of a sentence
for pet in pets:
    print(f"Here's what I know about {pet['owner'].title()}'s pet {pet['animal type']}:")
# print(pets)