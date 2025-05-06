import random
pets = {}
pet_preferences = {
    'Dog' : ("Bones", "Walk"),
    'Cat': ("Play", "Purring")
}
class Pet:
    def __init__(self, name,species,age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print("Name:",self.name)
        print("Species:",self.species)
        print("Age:",self.age)


class Cat(Pet):
    def __init__(self,name,age,color,breed):
        super().__init__(name, "Cat",age)
        self.breed = breed
        self.color = color
    def display_info(self):
        super().display_info()
        print(f"Breed:{self.breed}")
        print(f"Color:{self.color}")
        print(f"Preferences:{pet_preferences['Cat']}")

class Dog(Pet):
    def __init__(self,name,age,color,breed):
        super().__init__(name,"Dog",age)
        self.breed = breed
        self.color = color
    def display_info(self):
        super().display_info()
        print(f"Breed:{self.breed} Color:{self.color} Preferences:{pet_preferences['Dog']}")


def menu():
    while True:
        user_input = int(input("""Select from below: 
            1. View Available Pets
            2. Adopt a Pet
            3. Add new Pet
            4. Exit: """))
        if user_input == 1:
            view_pets()
        elif user_input == 2:
            print("You're looking Adopt one?")
            adopt_pet()
        elif user_input == 3:
            print("Add new Pet.. :)")
            add_pet()
        elif user_input == 4:
            print("Bye, Have a Nice Day.")
            break
        else:
            print("Invalid Input.")
            print("Try Again.")
            menu()

def view_pets():
    if not pets:
        print("No pets are Available.")
    for pet_id, pet in pets.items():
        print(f"Pet ID: {pet_id}")
        print()
        pet.display_info()

        
def adopt_pet():
    pet_id = int(input("Enter Pet ID: "))
    if pet_id in pets:
        print(f"You've Adopted {pets[pet_id].name}")
        del pets[pet_id]
    else:
        print("Invalid ID.")

def add_pet():
    species = input("Enter Species(Cat/Dog): ").capitalize()
    name = input("Pet Name: ")
    age = int(input("Enter Pet Age: "))
    breed = input("Enter Breed: ")
    color = input("Enter Color: ")

    pet_id = random.randint(100,1000)
    if species == "Dog":
        pet = Dog(name,age,color,breed)
    elif species == "Cat":
        pet = Cat(name,age,color,breed)
    else:
        print("Invalid.")
        return
    
    pets[pet_id] = pet
    print(f"{species} added with ID: {pet_id}")




if __name__ == "__main__":
    menu()