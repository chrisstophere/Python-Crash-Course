sandwich_orders = ['ham', 'pastrami', 'roast beef', 'pastrami', 'turkey',
                   'pastrami']
finished_sandwiches = []

print('Uh oh, the deli has run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} sandwich.")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I have made your {sandwich.title()} sandwich.")
