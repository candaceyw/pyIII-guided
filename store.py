
class Store:
    # attributes
    # name
    # categories (departments)

    # constructor - the function that runs every time you create a new instance
    # self refers to the current instance of the class (in JS the word is 'this')
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        # return a string representing the store
        return f'Welcome to {self.name}: Here are the categories: {self.categories}'


sports_store = Store("Gander Mountain", ["running", "baseball", 'basketball'])

produce_store = Store('Trader Joe\'s', ['dairy', 'meat', 'bread', 'produce'])

print(sports_store)
print(produce_store)
print(sports_store.name)