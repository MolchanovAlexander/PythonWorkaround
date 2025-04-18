from tkinter import *

def click():

    x = float(entry1.get())
    y = float(entry2.get())
    z = x + y
    label_result['text'] = str(z)
    #label_result.config(text=str(z))


root = Tk()
root.geometry("300x250")
root.title("Sofiyka Adder")

label1 = Label(text='First Number:')
label1.pack(pady=5)

entry1 = Entry(width=26)
entry1.pack(pady=5)

label2 = Label(text='Second Number:')
label2.pack(pady=5)

entry2 = Entry()
entry2.pack(pady=5)

button = Button(text="Add", command=click)
button.pack(pady=10)

label_result = Label(text="Result:")
label_result.pack(pady=5)

root.mainloop()
