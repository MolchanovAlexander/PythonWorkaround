class Dog:
    name = None
    age = None
    isSmelling = None

    def __init__(self, name=None, age=None, isSmelling=None):
        self.name = name
        self.isSmelling = isSmelling
        self.age = age
        self.get_sran()


    def dog_data(self, name, age, isSmelling=True):
        self.name = name
        self.isSmelling = isSmelling
        self.age = age

    def get_sran(self):
        print(self.name, "age:", self.age, " .isSmelling: ", self.isSmelling)


shitty_dog = Dog("dniwe", 11, False)
shitty_dog.dog_data("peregniy", 4)
dog2 = Dog("guf", 2, False)


print(shitty_dog.isSmelling, dog2.isSmelling)
dog2.get_sran()

dog3 = Dog(age=23)
