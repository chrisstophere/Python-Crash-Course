# Define an empty list
people = []
# Dictionary 1
person1 = {
            'first_name': 'chris',
            'last_name': 'caserta',
            'age': 47,
            'city': 'roxborough'
          }
# Add dictionary 1 to the people list
people.append(person1)
# Dictionary 2
person2 = {
            'first_name': 'tina',
            'last_name': 'ewen',
            'age': 46,
            'city': 'danville'
          }
# Add dictionary 2 to the people list
people.append(person2)
# Dictionary 3
person3 = {
            'first_name': 'jacob',
            'last_name': 'ewen',
            'age': 13,
            'city': 'danville'
          }
# Add dictionary 3 to the people list
people.append(person3)

# Loop thru the people list
for person in people:
# Assign a variable to each value in the people list.
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
# Print a sentence using the variables created above.
    print(f"{name}, of {city}, is {age} years old.")


