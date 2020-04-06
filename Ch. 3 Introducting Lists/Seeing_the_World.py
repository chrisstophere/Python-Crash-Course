# Five places I would like to visit one day
places = ['colorado', 'egypt', 'europe', 'california', 'alaska']

# Print the list in a raw format
print(places)

# Print the list in alphabetical order
print(sorted(places))

# PShow list is still in original order
print(places)

# Print the list in reverse alphabetical order w/o changing the order of the
# original list
print(sorted(places, reverse=True))

# Show list is still in original order
print(places)

# Reverse the order of the list
places.reverse()

# Print the list to show it has been reversed
print(places)

# Reverse the order of the list to revert it to its original order
places.reverse()

# Print the list to show it has been reverted to its original order
print(places)

# Use the sort method to permanently change the list order
places.sort()

# Print the list to show its order has been changed
print(places)

# Reverse the sort order of the list
places.sort(reverse=True)

# Print the list to show its order reversed
print(places)