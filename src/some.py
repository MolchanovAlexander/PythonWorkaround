ug = [1, 2, 33, 4, 55, 22, 76]

bin1 = 0b00000101
print(bin1)
lambda1 = lambda x: x + 1

print(lambda1(2))

dno = list(filter(lambda i: i % 2 == 0, ug))
print(dno)

dno = list(map(lambda i: i ** 2, ug))
print(dno)

array = [83, 79, 76, 79, 77, 73, 65]
for i in array:
    print(i, '-', chr(i))