import random
Computer = random.randint(0,2)
Player = input("Rock Paper or Scissors?")
Player = str(Player)   
if Computer == 0:
    Computer = "Rock"
elif Computer == 1:
    Computer ="Paper"
else:
    Computer = "Scissors"


if Player == Computer:
    result = "Draw"
else:
    if Computer == "Rock":
        if Player == "Paper":
            Result = "Win"
        else: 
            Result = "Lose"
    elif Computer == "Paper":
        if Player == "Scissors":
            Result = "Win"
        else:
            Result = "Lose"
    elif Computer == "Scissors":
        if Player == "Rock":
            Result = "Win"
        else:
            Result = "Lose"

print ("----------")


print ("Player Pick", Player)
print ("Computer Pick", Computer)
print (Result)


print ("----------")