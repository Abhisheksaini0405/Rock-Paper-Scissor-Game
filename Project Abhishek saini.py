# Import Required Library
from tkinter import *
from random import *

# Create Object
window = Tk()

# Set geometry
window.geometry("400x400")

# Set title
window.title("Rock Paper Scissor Game")

# Computer Value
comp_dict = {"0": "Rock", "1": "Paper", "2": "Scissor"}

# Reset The Game


def reset_game():
  b1["state"] = "active"
  b2["state"] = "active"
  b3["state"] = "active"
  l1.config(text="Player    ")
  l3.config(text="Computer")
  l4.config(text="")


# Disable the Button


def button_disable():
  b1["state"] = "disable"
  b2["state"] = "disable"
  b3["state"] = "disable"


# If player selected rock


def isrock():
  value = comp_dict[str(randint(0, 2))]
  if value == "Rock":
    match_result = "Match Draw"
  elif value == "Scissor":
    match_result = "Player Win"
  else:
    match_result = "Computer Win"
  l4.config(text=match_result)
  l1.config(text="Rock   ")
  l3.config(text=value)
  button_disable()


# If player selected paper


def ispaper():
  value = comp_dict[str(randint(0, 2))]
  if value == "Paper":
    match_result = "Match Draw"
  elif value == "Scissor":
    match_result = "Computer Win"
  else:
    match_result = "Player Win"
  l4.config(text=match_result)
  l1.config(text="Paper   ")
  l3.config(text=value)
  button_disable()


# If player selected scissor


def isscissor():
  value = comp_dict[str(randint(0, 2))]
  if value == "Rock":
    match_result = "Computer Win"
  elif value == "Scissor":
    match_result = "Match Draw"
  else:
    match_result = "Player Win"
  l4.config(text=match_result)
  l1.config(text="Scissor   ")
  l3.config(text=value)
  button_disable()


# Add Labels, Frames and Button
Label(window, text="Rock Paper Scissor", font="times  25 bold",
      fg="red").pack(pady=20)

f1 = Frame(window)
f1.pack()
window.rowconfigure(0,weight=1,minsize=10)
window.columnconfigure([0,1,2],weight=1,minsize=10)
l1 = Label(f1, text="Player   ", font="times 15")

l2 = Label(f1, text="VS   ", font="times 15 bold")

l3 = Label(f1, text="Computer", font="times 15")

l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=0,column=2)

l4 = Label(window,
           text="",
           font="times 20 bold",
           bg="white",
           width=20,
           fg="orange",
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)

f2 = Frame(window)
f2.pack()

b1 = Button(f2, text="Rock", fg="yellow",bg="green",font="times 10", width=8, command=isrock)

b2 = Button(f2, text="Paper ", fg="black",bg="red" ,font="times 10", width=8, command=ispaper)

b3 = Button(f2, text="Scissor",fg="yellow",bg="green", font="times 10", width=8, command=isscissor)

b1.pack(side=LEFT, padx=12)
b2.pack(side=LEFT, padx=12)
b3.pack(padx=12)

Button(window,
       text="Reset Game",
       font="times 10",
       fg="white",
       bg="black",
       command=reset_game).pack(pady=20)

# Execute Tkinter
window.mainloop()
