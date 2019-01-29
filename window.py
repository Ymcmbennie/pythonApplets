from tkinter import *
window = Tk()
window.title("BensonAD program")

window.geometry('300x300')
lbl = Label(window, text="Welcome to BensonAD", font=("Roboto bold",20))
lbl.grid(column=0, row=1)
txt = Entry(window,width=20)
txt.grid(column=0, row=2)


def clicked():
    res = "Welcome " + txt.get()
    lbl.configure(text= res)
    
btn = Button(window, text="Learn More", bg="grey", fg="white", command=clicked)
btn.grid(column=0, row=3)

window.mainloop()
