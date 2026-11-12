import tkinter

def happy_button_clicked():
    label.configure(text='You feels happy today!')

def tired_button_clicked():
    label.configure(text='Too many in-class activities!')

# TODO define your button event handler here (function)
def sad_button_clicked():
    label.configure(text='I hope your day gets better!')

root = tkinter.Tk()

# TODO: Update to your name
root.title("Collin Steele's First Tkinter GUI!!!!")
root.configure(width=700, height=400, background='powderblue')

label = tkinter.Label(root, text='Hello, How are you feeling today?', font=('Arial', 24, 'bold'))
label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

button = tkinter.Button(
    root, 
    text='Happy', 
    font=('Times New Roman', 24, 'bold'),
    command=happy_button_clicked
    )

button.place(
    relx=0.5, 
    rely=0.4, 
    anchor=tkinter.CENTER)

tired_button = tkinter.Button(
    root, 
    text='Tired', 
    font=('Times New Roman', 24, 'bold'),
    command=tired_button_clicked
    )

tired_button.place(
    relx=0.5, 
    rely=0.6, anchor=tkinter.CENTER)

# TODO: define your button and place your button here
sad_button = tkinter.Button(
    root, 
    text='Sad', 
    font=('Times New Roman', 24, 'bold'),
    command=sad_button_clicked
)
sad_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

root.mainloop()