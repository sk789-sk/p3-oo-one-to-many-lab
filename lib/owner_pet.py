class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []

    def __init__(self,name,pet_type,owner='placeholder') -> None:
        self.name = name

        if pet_type in Pet.PET_TYPES:
            self.pet_type= pet_type
        else:
            raise Exception("what u doing")
        Pet.all.append(self)

        if isinstance(owner,Owner):
            self.owner = owner
            owner.my_pets.append(self)
    
class Owner:

    def __init__(self,name) -> None:
        self.name = name
        self.my_pets = []

    def pets(self):
        return self.my_pets
    
    def add_pet(self, pet): #pet should be an instance of a pet
        if isinstance(pet,Pet):
            self.my_pets.append(pet)
            pet.owner = self
        else:
            raise Exception("???")

    def get_sorted_pets(self): #return a sorted list of pets by name
        new_list = sorted(self.my_pets, key=lambda x: x.name) #x.name is the name in the pet instance
        return new_list


# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)       

# print(owner.get_sorted_pets())