
# immutable list from slice
katya = [1, 2, 3, 4, 5]
rev = katya.reverse() # this reverse katya list and return None
solomka = katya[::-1]
katya.remove(1)
katya.remove(3)
katya.append(13)
katya.append((1, "ccc"))
katya[4] = (4, "44")
print(katya, rev, solomka)

# tuples
data = ("dno", 4.5, 46, [1, 2, 3], True, ("dniwe", 4))

print(data[-1][0]) # from last element
print(data[2:-2:])
tupKatya = tuple(katya)
print(tupKatya) # transform to tuple
# for element in data:
#     print(element, " <- dno")


