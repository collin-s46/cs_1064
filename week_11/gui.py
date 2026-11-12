import tkinter
root = tkinter.Tk()

root.title('My first GUI!')
root.configure(width=500, height=500, background='blue')

label = tkinter.Label(
    root, 
    text='Hello', 
    font=('Ariel', 24, 'bold')
    )

label.place(relx=0.5, rely=0.5)

root.mainloop()

