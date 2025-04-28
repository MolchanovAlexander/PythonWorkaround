try:
    with open("data/test.txt", "r", encoding="utf-8") as file:
        print(file.read())
except Exception as e:
    print("You've got some error: ", e)
