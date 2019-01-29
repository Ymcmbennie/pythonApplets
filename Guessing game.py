import random
from tkinter import *



window = Tk()
window.title("Guessing game")
window.geometry('350x200')
lbl = Label(window, text="Enter any number from 1 to 10")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=0, row=1)
def clicked():
      a=random.randrange(0,10)
      b =txt.get()
      if a==int(b):
            lbl.configure(text="The number was {} You won!".format(a))
      else:
            lbl.configure(text="The number was {}. So you lost".format(a))

def reseted():
      lbl.configure(text="Enter any number from 1 to 10")
            
    
btn = Button(window, text="Submit Answer", command=clicked)
btn.grid(column=0, row=2)
btn = Button(window, text="Reset", command=reseted)
btn.grid(column=0, row=3)
window.mainloop()
