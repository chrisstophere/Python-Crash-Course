usernames = ['admin', 'administrator', 'root', 'user', 'chris']

for username in usernames:
    if username == 'admin':
        print(f"Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, welcome to the system.")