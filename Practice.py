# Main Zoo class
class Zoo:
    def __init__(self):
        self.animals = []
        self.birds = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def add_bird(self, bird):
        self.birds.append(bird)
    
    def get_animal_count(self):
        return len(self.animals)
    
    def get_bird_count(self):
        return len(self.birds)

# Animal class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

# Bird class
class Bird:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

# Create Zoo
my_zoo = Zoo()

# Insert animals and birds
lion = Animal("Lion")
tiger = Animal("Tiger")
parrot = Bird("Parrot")
eagle = Bird("Eagle")

# Add to zoo
my_zoo.add_animal(lion)
my_zoo.add_animal(tiger)
my_zoo.add_bird(parrot)
my_zoo.add_bird(eagle)

# Print details
print("Animals in zoo:")
for a in my_zoo.animals:
    print(a.get_name())

print("\nBirds in zoo:")
for b in my_zoo.birds:
    print(b.get_name())

print("\nTotal animals:", my_zoo.get_animal_count())
print("Total birds:", my_zoo.get_bird_count())
