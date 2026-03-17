#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
def shout(self):
    print(f'my name is {self.name}')

# 1 Instantiate the Cat object with 3 cats
orangecat = Cat("cookie", 4)
bigcat = Cat("tomtom", 8)
greycat = Cat("lala", 2)
print(shout(bigcat))

# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(*args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest_cat(orangecat.age, bigcat.age, greycat.age)} years old.")






