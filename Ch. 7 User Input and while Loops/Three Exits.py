# Ask the user for their age
prompt = "What is your age? "
prompt += "Type 'q' to exit: "

keepGoing = True
stop = 0

while keepGoing:
    if stop >= 4:
        break
    age = input(prompt)
    if age == 'q':
        break
    age = int(age)

    if age < 3:
        print(f"Your ticket is free!")
        stop += 1
        # keepGoing = False
    elif age <= 12:
        print(f"Your ticket is $10!")
        stop += 1
        # keepGoing = False
    elif age > 12:
        print(f"Your ticket is $15!")
        stop += 1
        # keepGoing = False
    else:
        keepGoing = False