my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

for food in my_foods:
    print(f"I enjoy eating {food.title()}.")
for food in friend_foods:
    print(f"He enjoys eating {food.title()}.")