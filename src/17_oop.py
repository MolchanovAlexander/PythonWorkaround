class Dog:
    name = None
    age = None
    isSmelling = None

shitty_dog = Dog()
shitty_dog.age = 11
shitty_dog.name = "smerduchiy"
shitty_dog.isSmelling = True

dog2 = Dog()
dog2.name = "guf"
dog2.age = 2
dog2.isSmelling = False

print(shitty_dog.isSmelling, dog2.isSmelling)