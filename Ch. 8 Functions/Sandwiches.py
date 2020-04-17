def sandwiches(*items):
    print("\nMaking a sandwich with the following stuff:")
    for item in items:
        print(f"-{item.title()}")
sandwiches('ham', 'cheese', 'pickles')
sandwiches('turkey', 'swiss', 'chips')
sandwiches('roast beef')