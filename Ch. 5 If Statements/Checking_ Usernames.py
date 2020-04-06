current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['User1', 'user2', 'user6', 'user7', 'user8']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username taken, try another username.")
    else:
        print(f"That username is available!")