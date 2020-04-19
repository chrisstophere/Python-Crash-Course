from showMessages import show_messages
from sendMessages import send_messages

# Define the list of text messages
messages = ['"hi"', '"on my way"', '"give me a call"']
# Define an empty list to hold the moved values
sent_messages = []

# Call the function that prints all the messages
show_messages(sent_messages)
print("\n")

# Call the function that prints the message is being sent
# and then moves the value to the new list
send_messages(messages[:], sent_messages)

# Print the new list showing that it now holds all the values
print("\nThis is the new list. It should now be full since "
      "all the values have been moved to it from the original list.")
print(sent_messages)

# Print the original list showing that all the values have been moved
print("\nThis is the original list. It should now be empty since "
      "all the values have been moved to the new list.")
print(messages)