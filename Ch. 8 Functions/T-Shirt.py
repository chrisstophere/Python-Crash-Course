def make_shirt(size, message):
    """Prints shirt details"""
    print(f"Your shirt size is {size} and it will have"
          f"{message} printed on it.")
make_shirt('xl', 'hello')
make_shirt(message='goodbye', size='large')