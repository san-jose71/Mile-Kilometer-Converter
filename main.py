from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")




window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Miles - label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#Is equal to - label
equal_to_label = Label(text="Is iqual to")
equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)













window.mainloop()