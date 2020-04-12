def show_messages(messages):
    """Loop thru a list named text_messages and
       print a simple text message using each value"""
    for message in messages:
        print(message)

# Define the list text_messages
messages = ['"hi"', '"on my way"', '"give me a call"']
show_messages(messages)