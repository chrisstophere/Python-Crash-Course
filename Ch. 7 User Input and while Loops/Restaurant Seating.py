#  Putting the answer into a variable...
#  Ask user how many people need to be seated in their dinner party
question = input("How many in your dinner party? ")
# Convert answer into an integer
question = int(question)
#  Compare answer to 8. If answer is greater than 8...
#  print message party will have to wait. If answer is less than ...
#  8, print message party's table is ready
if question > 8:
    print("I'm sorry, you'll have to wait.")
else:
    print("Your table is ready.")