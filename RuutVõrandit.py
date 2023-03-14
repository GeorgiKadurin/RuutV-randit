from tkinter import*


aken = Tk()

aken.geometry("750x320")


spin9 = Label(aken, 
             fg="#041208", 
             bg="yellow", 
             width=45, 
             height=3, 
             text="Решение", 
             font="Broadway 20")


spin1 = Label(aken, 
             fg="green",
             bg="lightblue", 
             text="Решение квадратного уравнения", 
             font="Broadway 20", 
             justify=CENTER)

spin2 = Entry(aken, 
          fg="blue", 
          bg="lightblue",
          width=4, 
          font="Broadway 20")


spin6 = Label(aken, 
            fg="green", 
            text="x**2", 
            font="Broadway 20", 
            justify=CENTER)

spin4 = Entry(aken, 
          fg="blue", 
          bg="lightblue", 
          width=4, 
          font="Broadway 20")

spin7 = Label(aken, 
             fg="green", 
             text="x+", 
             font="Broadway 20", 
             justify=CENTER)

spin3 = Entry(aken, 
          fg="blue", 
          bg="lightblue",
          width=4, 
          font="Broadway 20")

spin8 = Label(aken, 
             fg="green", 
             text="=0", 
             font="Broadway 20", 
             justify=CENTER)

spin5 = Button(aken, 
             fg="#041208", 
             bg="green", 
             text="Решение", 
             width=6, 
             font="Broadway 20")




spin9.pack(side=BOTTOM)

spin1.pack()

spin2.pack(side=LEFT)

spin6.pack(side=LEFT)

spin4.pack(side=LEFT)

spin7.pack(side=LEFT)

spin3.pack(side=LEFT)

spin8.pack(side=LEFT)

spin5.pack(side=LEFT)




aken.mainloop()















































