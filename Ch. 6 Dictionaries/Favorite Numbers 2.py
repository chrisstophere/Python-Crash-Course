favorite_number = {'Chris': [3, 33, 99],
                   'Tina': [4, 8],
                   'Jacob': [13, 26, 72, 100]
                   }
for name, numbers in favorite_number.items():
    print(f"{name.lower()}'s favorite numbers are:")

    for number in numbers:
        print(f"\t{number}")