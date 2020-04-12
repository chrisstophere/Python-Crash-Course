def show_messages(messages, sent_messages):
    """Loop thru a list named text_messages and
       print a simple text message using each value"""
    for message in messages:
        print(message)

def send_messages(sent_messages):
    """Print each message and then move it to a new list"""
    while messages:
        sent_message = messages.pop()
        print(f"I sent the message {sent_message}.")
        sent_messages.append(sent_message)

# Define the list of text messages
messages = ['"hi"', '"on my way"', '"give me a call"']
# Define an empty list to hold the moved values
sent_messages = []

# Call the function that prints all the messages
show_messages(messages, sent_messages)
print("\n")
# Call the function that prints the message is being sent
# and then moves the value to the new list
send_messages(sent_messages)

# Print the new list showing that it now holds all the values
print("\nThis is the new list. It should now be full since "
      "all the values have been moved to it from the original list.")
print(sent_messages)

# Print the original list showing that all the values have been moved
print("\nThis is the original list. It should now be empty since "
      "all the values have been moved to the new list.")
print(messages)