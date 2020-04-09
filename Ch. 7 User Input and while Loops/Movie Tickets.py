# Ask the user for their age
prompt = "What is your age? "
prompt += "Type 'q' to exit: "
keepGoing = True
while keepGoing:
    age = input(prompt)
    if age == 'q':
        break
    age = int(age)

    if age < 3:
        print(f"Your ticket is free!")
        #keepGoing = False
    elif age <= 12:
        print(f"Your ticket is $10!")
        #keepGoing = False
    elif age > 12:
        print(f"Your ticket is $15!")
        #keepGoing = False
    else:
        continue