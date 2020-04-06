rivers = {
          'nile': 'egypt',
          'amazon': 'africa',
          'mississippi': 'the united states'
         }

for river in rivers:
    country = rivers[river].title()
    print(f"The {river.title()} river runs through {country}.")

print("\n")

for keys in rivers:
    print(keys.title())

print("\n")

for values in rivers.values():
    print(values.title())