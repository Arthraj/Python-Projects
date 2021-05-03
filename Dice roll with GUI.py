from tkinter import *
import random

frame=Tk()
frame.title("Dice Roll Simulator")
frame.geometry("400x300")
frame['bg']='#CCFFFF'

def printDiceOutputs():
    var=str(number_of_dices.get())
    if var.isdigit():
        num=int(var)
    else:
        pass

    diceOutputs=[]      #An empty list to store all outputs off dices rolls

    for i in range(0,num):
        rd=random.randint(1,6)  #Outputs of every dice are randomly guessed
        diceOutputs.append(rd)  #Each dice roll output is then stored in the list

    Label(frame,text=f"Random outputs of dice rolls are {diceOutputs}").pack()

number_of_dices=Entry(frame)
number_of_dices.pack(pady=30)


Button(
    frame,
    text="Roll Dice(s)",
    padx=10,
    pady=5,
    command=printDiceOutputs
).pack()



frame.mainloop()