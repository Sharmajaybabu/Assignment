class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Meow")


def animal_sound_in_zoo(animal):
    animal.make_sound()


# Create instances of Dog and Cat classes
dog_instance = Dog()
cat_instance = Cat()

# Call the function with instances as arguments
print("Dog in the zoo:")
animal_sound_in_zoo(dog_instance)

print("\nCat in the zoo:")
animal_sound_in_zoo(cat_instance)
