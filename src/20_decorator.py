import  webbrowser

print("start")

def validator(func):
    def wrapper(url):
        print("before")
        func(url)
        print("after")
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


open_url("https://itproger.com")
