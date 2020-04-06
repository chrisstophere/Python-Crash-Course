# define a set of programming words used in Python.
prog_words = {'function': 'a block of reusable code',
              'method': 'a function available for an object',
              'list': 'a collection of data that is mutable',
              'tuple': 'a collection of data that is unmutable'
              }
# print the word on one line then print the meaning on a 2nd line.

definition = prog_words['function']
print(f"a function:".title())
print(f"\t{definition}.".title())

definition = prog_words['method']
print(f"\na method:".title())
print(f"\t{definition}.".title())

definition = prog_words['list']
print(f"\na list:".title())
print(f"\t{definition}.".title())

definition = prog_words['tuple']
print(f"\na tuple:".title())
print(f"\t{definition}.".title())