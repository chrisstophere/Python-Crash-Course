# Define a set of programming words used in Python.
prog_words = {'function': 'a block of reusable code',
              'method': 'a function available for an object',
              'list': 'a collection of data that is mutable',
              'tuple': 'a collection of data that is unmutable',
              'variable': 'a name for a piece of data that can change'
              }

# Print the key and value on a single line.
for words in prog_words.keys():
    prog = prog_words[words].title()
    print(f"A {words.title()} is: {prog}")
print("\n")
# Print the key on one line then print the definition on a 2nd line.
for words in prog_words.keys():
    prog = prog_words[words].title()
    print(f"A {words.title()} is:")
    print(f"\t{prog.title()}")