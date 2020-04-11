# Create an empty dictionary to hold all the responses
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for person's name and response
    name = input("What is your name? ")
    vacation = input("What is your dream vacation? ")

    # Store the answers in the dictionary
    responses[name] = vacation

    # Find out if anyone else wants to take the polling
    repeat = input("Would you like anyone else to take the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")







