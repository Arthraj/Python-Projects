from tkinter import *

Root=Tk()
Root.title("My frame")
Root.geometry("400x200")

def _enter_(event):
    print(f"Entered at {event.x},{event.y}")

def _exit_(event):
    print(f"Exit at {event.x},{event.y}")

my_frame=Frame(Root, width=400, height=200)

my_frame.bind('<Enter>',_enter_)
my_frame.bind('<Leave>',_exit_)

my_frame.pack()
Root.mainloop()