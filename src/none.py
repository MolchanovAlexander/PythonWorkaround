def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")

greet("Alice")  # Hello, Alice!
greet()         # Hello, stranger!

value = None
if value is None:
    print("No value")

#object User
class User:
    def __init__(self):
        self.profile = Profile()

class Profile:
    def __init__(self):
        self.name = "Alice"

    def __repr__(self):
        return f"Profile(name={self.name})"

user = User()
p = Profile()
p.name = "guf"
print(p)
profile = getattr(user, "profile", None)
print(profile)
if profile is not None:
    name = getattr(profile, "name", None)
    print(name)

