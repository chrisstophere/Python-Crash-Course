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

print(f"Good news all! There is a larger table so more people have been invited.\
        \n")

guests.insert(0, 'jason')
guests.insert(2, 'emily')
guests.append('jacob')

print(f'{guests[0].title()}, you are invited to dinner.')
print(f'{guests[1].title()}, you are invited to dinner.')
print(f'{guests[2].title()}, you are invited to dinner.')
print(f'{guests[3].title()}, you are invited to dinner.')
print(f'{guests[4].title()}, you are invited to dinner.')
print(f'{guests[5].title()}, you are invited to dinner.')
print(f'{guests[6].title()}, you are invited to dinner.\n')

print("Change of plans. I can only invite two people.\n")

popped_guest = guests.pop(0)
print(f"{popped_guest.title()}, sorry, you can't come to dinner.")

popped_guest = guests.pop(1)
print(f"{popped_guest.title()}, sorry, you can't come to dinner.")

popped_guest = guests.pop(2)
print(f"{popped_guest.title()}, sorry, you can't come to dinner.")

popped_guest = guests.pop(3)
print(f"{popped_guest.title()}, sorry, you can't come to dinner.")

popped_guest = guests.pop()
print(f"{popped_guest.title()}, sorry, you can't come to dinner.")

del guests[1]
del guests[0]

print(guests)
