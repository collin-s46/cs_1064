from tkinter import *

root = Tk()
root.config(bg='powderblue')
root.title('Thanksgiving Meal Planner')

meal_entrees = ['Turkey', 'Pasta', 'Veggie Noodles']
sides = ['butter', 'green beans', 'mac and cheese']

meal_choice = IntVar()
meal_choice.set(0)

butter_checked = BooleanVar()
green_beans_checked = BooleanVar()
mac_and_cheese_checked = BooleanVar()

def update_meal():
    side_strings = []

    if butter_checked.get():
        side_strings.append(sides[0])

    if green_beans_checked.get():
        side_strings.append(sides[1])

    if mac_and_cheese_checked.get():
        side_strings.append(sides[2])

    meal_text = 'My thanksgiving meal is ' + meal_entrees[meal_choice.get()]

    if side_strings:
        meal_text += ' with ' + ', '.join(side_strings)

    meal_label.config(text=meal_text)


meal_label = Label(
    root,
    text='This is my thanksgiving meal plan!',
    font=('Arial', 24),
    padx=30,
    pady=30,
    bg='powderblue'
)
meal_label.pack()

meal_frame = Frame(root, bg='pink')
meal_frame.pack(pady=10)

Radiobutton(
    meal_frame,
    text=meal_entrees[0],
    value=0,
    variable=meal_choice,
    command=update_meal,
    bg='pink',
    font=('Arial', 20)
).pack()

Radiobutton(
    meal_frame,
    text=meal_entrees[1],
    value=1,
    variable=meal_choice,
    command=update_meal,
    bg='pink',
    font=('Arial', 20)
).pack()

Radiobutton(
    meal_frame,
    text=meal_entrees[2],
    value=2,
    variable=meal_choice,
    command=update_meal,
    bg='pink',
    font=('Arial', 20)
).pack()

sides_frame = Frame(root, bg='beige', padx=30, pady=30)
sides_frame.pack()

Checkbutton(
    sides_frame,
    text=sides[0],
    variable=butter_checked,
    command=update_meal,
    bg='beige',
    font=('Arial', 20)
).pack(pady=10)

Checkbutton(
    sides_frame,
    text=sides[1],
    variable=green_beans_checked,
    command=update_meal,
    bg='beige',
    font=('Arial', 20)
).pack(pady=10)

Checkbutton(
    sides_frame,
    text=sides[2],
    variable=mac_and_cheese_checked,
    command=update_meal,
    bg='beige',
    font=('Arial', 20)
).pack(pady=10)

root.mainloop()