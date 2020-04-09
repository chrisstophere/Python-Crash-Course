# Ask the user for a number
prompt = "Enter a number to find out whether "
prompt += "it is a multiple of 10: "
# Put answer into a variable.
number = input(prompt)
# Convert answer into an integer
number = int(number)
# Print whether number is a multiple of ten
if number % 10 == 0:
    print(f"Yes, {number} is a multiple of 10.")
else:
    print(f"No, {number} is not a multiple of 10.")