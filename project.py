from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

def converter():
    value = float(input_value.get())
    result = value * 1.609
    label_2.config(text=round(result, 2))

#Is equal to label
label_1 = Label(text="is equal to", font=("Arial", 12, "normal"))
label_1.grid(column=0, row=1)

#changing KM value label
label_2 = Label(text="0", font=("Arial", 12, "normal"))
label_2.grid(column=1, row=1)

#miles label
label_3 = Label(text="Miles", font=("Arial", 12, "normal"))
label_3.grid(column=2, row=0)

#Km Label
label_4 = Label(text="KM", font=("Arial", 12, "normal"))
label_4.grid(column=2, row=1)

#input value
input_value = Entry(width=8)
input_value.grid(column=1, row=0)

#calculate button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)
window.mainloop()