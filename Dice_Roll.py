import random

a=int(input("How many dices you want to roll?\n"))

diceOutputs=[]      #An empty list to store all outputs off dices rolls

for i in range(0,a):
    rd=random.randint(1,6)  #Outputs of every dice are randomly guessed
    diceOutputs.append(rd)  #Each dice roll output is then stored in the list

print("Outputs of dices are as follows:-\n"+str(diceOutputs))