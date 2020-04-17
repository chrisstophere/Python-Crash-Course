def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('chris', 'ewen',
                             location='danville',
                             field='IT')
# print(user_profile)
test = build_profile('chris', 'ewen', location='VA', field='IT')
print(test)