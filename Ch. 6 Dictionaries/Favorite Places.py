# Create a dictionary named favorite_places...
# Make 3 keys named as people, and store 1-3 places...
# for each person
#
favorite_places = {
                    'chris': ['coloroda', 'valley forge', 'vermont'],
                    'tina': ['florida', 'disney world', 'bahamas'],
                    'jacob': ['virginia', 'toyland']
                  }

# Loop thru the names and lists in the dictionary
for person, places in favorite_places.items():
    # Print the names in the dictionary
    print(f"{person.title()}'s favorite places are: ")
    # Loop thru and print all the items in the list that was given
    # the variable places
    for place in places:
        print(f"\t{place.title()}")