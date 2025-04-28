person = {"name": "newbie", "age":19, 4: 415, (3, 5): "Ty noob", False: "False"}
person[False] = "True"
person["Some"] = "None"
print(person)
print(person[(3, 5)], person[False], "---------------", person.get(4))
#person.values() #-> list of values
for key in person:
    print(key)
print(person.popitem())
print(person.pop(4))
person2 = dict(name="guf", dead="rip")
person2["some"] = "none"
print(person2, "----------")

for key, value in person2.items(): #Like EntrySet - tuple list by itself
    print(key, value, sep=" = ")