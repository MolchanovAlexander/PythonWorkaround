ug = [1, 2, 33, 4, 55, 22, 76]

bin1 = 0b00000101
hex1 = 0x4a1f
print(bin1, " bin1--------")
print(hex1, " hex1--------")

print(bin(442))
print(hex(442))
lambda1 = lambda x: x + 1

print(lambda1(2))

dno = list(filter(lambda z: z % 2 == 0, ug))
print(dno)

dno = list(map(lambda t: t ** 2, ug))
print(dno)

array = [83, 79, 76, 79, 77, 73, 65]
for i in array:
    print(i, '-', chr(i))


def minus_one(list):
    ret_val = []
    for element in list:
        ret_val.append(element - 1)

    return ret_val


print(minus_one(ug))

lambda_minus_one = lambda x: x - 1
another = list(map(lambda_minus_one, ug))
print(another)