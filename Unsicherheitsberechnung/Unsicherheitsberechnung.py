from tkinter import *

main = Tk()
slider = Scale(main, from_=0, to=20, orient=HORIZONTAL)
inputsNumber = 0

variables = []

def get_inputsNumber():
 inputsNumber = slider.get()
 count = 0
 while (count <= inputsNumber):
    variable = input()
    variables.insert(count, variable)
    count = count + 1

button = Button(main, text="Continue", command=get_inputsNumber)

slider.pack()
button.pack()
mainloop()