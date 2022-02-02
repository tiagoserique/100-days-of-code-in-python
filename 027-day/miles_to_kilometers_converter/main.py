from ctypes import resize
from tkinter import *


def button_clicked():
	miles 	= float(input.get())
	km 		= miles * 1.609

	result_label.config(text=f"{km}")
	# text_box.delete("1.0", END)
	# text_box.insert(END, f"{km}")
    

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)
# End window

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)
# End entry

# Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)
# End label

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
# End button

# Text
# text_box = Text(width=10, height=1)
# text_box.grid(column=1, row=1)
# End text


window.mainloop()