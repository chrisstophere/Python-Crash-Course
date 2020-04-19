def send_messages(messages, sent_messages):
    """Print each message and then move it to a new list"""
    while messages:
        sent_message = messages.pop()
        print(f"I sent the message {sent_message}.")
        sent_messages.append(sent_message)