from tkinter import *


# window

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# my_label.place(x=100, y=200)
my_label.config(padx=50, pady=50)



# Button

def button_clicked():
	new_text = input.get()
	my_label.config(text=f"{new_text}")


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
print(input.get())













window.mainloop()
