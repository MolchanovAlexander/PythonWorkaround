file = open("data/test.txt", "a")
data = input("ty noob? :")
file.write(data + "\n")
file.close()

file_read = open("data/test.txt", "r")
symbols = file_read.read(4)
print(symbols, "___symbo")
lines = file_read.read()
for line in file_read:
    print(line, end="")
file_read.close()

print(lines, " +++++++=")
