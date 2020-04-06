# establish a list of liked pizzas
pizzas = ['pepperoni', 'plain', 'spinach', 'bbq chicken', 'vegetable',
          'bacon', 'sausage']

# copy my pizza list to my friends list
friend_pizzas = pizzas[:]

# add an extra item to each of our pizza lists
pizzas.append('cheese')
friend_pizzas.append('ham')

# Print a list of my pizzas with the added append item - cheese
print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

# Print a list of my friend's pizzas with the added append item - ham
print(f"\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
