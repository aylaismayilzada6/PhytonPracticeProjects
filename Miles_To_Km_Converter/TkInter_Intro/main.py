import tkinter
from tkinter import Button, Entry

window = tkinter.Tk()


def button_clicked():
    print("I got clicked") #prints the input as a string
    new_text = input.get()
    my_label.config(text=new_text)
    input.config()
# pack() just organizes all widgets in the top center
# place() is more about precise positioning
#grig()


#window parameters
window.title("My First GUI Program")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

#label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 16, "italic"))
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

#button
button  = Button(text="Click me!", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Entry (input)
input = Entry(width=10)
#input.pack()
input.grid(column=3,row=2)

#new button
new_button = Button()
new_button = Button(text="slap me!", command=button_clicked)
new_button.grid(column=2, row=0)







window.mainloop()
