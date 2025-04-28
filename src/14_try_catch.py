import traceback

num = None

while num is None:
    try:
        num = input("enter dno: ")
        let = 10 / int(num)
        print(let)
    except Exception as e:
        print("You've got some error: ", e)
        traceback.print_exc()
    else:
        print("I don't know for what is this?")
    finally:
        print("finally")