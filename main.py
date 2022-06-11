from tkinter import *

window = Tk()
window.title("My First GUI Program")
# window.minsize(width=250, height=200)




# my_label["text"] = "Maga"
# my_label.config(text="Maga")

my_label = Label(text="Miles", font=("Arial", 10, "bold"))
my_label.grid(column=4, row=2)

new_label = Label(text="Km", font=("Arial", 10, "bold"))
new_label.grid(column=1, row=1)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=7)


input = Entry(width=10)
input.grid(column=2, row=2)


# new_button = Button(text="aaaa")
# new_button.grid(column=2, row=0)
window.mainloop()