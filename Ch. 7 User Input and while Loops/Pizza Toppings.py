# While looping, ask user for a pizza topping
prompt = "What would you like on your pizza? "
prompt += "\nType 'quit' to exit."
# Quit loop when user enters 'quit'
keepGoing = True
while keepGoing:
    topping = input(prompt)
    if topping == 'quit':
        keepGoing = False
    # Print message about pizza toppping
    else:
        print(f"\t{topping.title()} added to your pizza!")