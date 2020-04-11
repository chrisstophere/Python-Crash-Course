def make_shirt(message = "I love Python", size = "Large"):
    """Prints shirt details"""
    print(f"Your shirt size is {size} and it will have "
          f"{message} printed on it.")
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='goodbye')