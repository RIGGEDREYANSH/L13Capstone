from tkinter import *

states = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
    "New Hampshire","New Jersey","New Mexico","New York","North Carolina",
    "North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island",
    "South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","West Virginia","Wisconsin","Wyoming"
]

def search():
    q = txt.get().lower()
    lst.delete(0, END)
    found = False
    for state in states:
        if q in state.lower():
            lst.insert(END, state)
            found = True
    if not found:
        lst.insert(END, "No matches")

win = Tk()
win.title("State Search")

Label(win, text="Search").pack()

txt = Entry(win)
txt.pack()

Button(win, text="Search", command=search).pack()

lst = Listbox(win, width=30, height=15)
lst.pack()

for state in states:
    lst.insert(END, state)

win.mainloop()
