guests = ['einstein', 'jesus', 'cesaer', 'moses']
print(f'{guests[0].title()}, you are invited to dinner.')
print(f'{guests[1].title()}, you are invited to dinner.')
print(f'{guests[2].title()}, you are invited to dinner.')
print(f'{guests[3].title()}, you are invited to dinner.\n')

print(f"{guests[1].title()}, can't make it. He had to die for our sins.\n")

guests[1] = 'tina'
print(f'{guests[0].title()}, you are invited to dinner.')
print(f'{guests[1].title()}, you are invited to dinner.')
print(f'{guests[2].title()}, you are invited to dinner.')
print(f'{guests[3].title()}, you are invited to dinner.')