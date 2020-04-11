sandwich_orders = ['ham', 'roast beef', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I have made your {sandwich} sandwich.")