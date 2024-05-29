import random

print("Welcome to Rock Paper Scissors Game")

start = input("Do you want to play? ")

if start.lower() == "yes" :
    print("OK let's begin!\n")
else:
    print("Comeback when you are ready to fight")
    quit()

print("Round 1 - FIGHT")

pick1 = input("Type your pick of Rock, Paper, or Scissors: ").lower()

if pick1.lower() == "rock" or pick1.lower() == "paper" or pick1.lower() == "scissors":
    print("Player 1 you chose",pick1,"for Round 1")
    score = 0
    fightoptions = ["rock","paper","scissors"]
    cpu_pick1 = random.choice(fightoptions)
    if pick1 == "rock" and cpu_pick1 == "paper":
        print("CPU chose paper - You Lost...")
    elif pick1 == "rock" and cpu_pick1 == "scissors":
        print("CPU chose scissors - YOU WIN!!!!")
        score += 1
    elif pick1 == "rock" and cpu_pick1 == "rock":
        print("CPU chose rock - DRAW")
    
    elif pick1 == "paper" and cpu_pick1 == "rock":
        print ("CPU chose rock - YOU WIN!!!!")
        score += 1

    elif pick1 == "paper" and cpu_pick1 == "paper":
        print("CPU chose paper - DRAW")

    elif pick1 == "paper" and cpu_pick1 == "scissors":
        print ("CPU chose scissors - You Lost...")

    elif pick1 == "scissors" and cpu_pick1 == "rock":
        print("CPU chose rock - You Lost...")

    elif pick1 == "scissors" and cpu_pick1 == "scissors":
        print ("CPU chose scissors - DRAW")

    elif pick1 == "scissors" and cpu_pick1 == "paper":
        print("CPU chose paper - YOU WIN!!!!")
        score += 1


else: 
    print("Error choose Rock, Paper, or Scissors")
    quit()

print("Player 1 - Score:",score)

print("\n")

print("Round 2 - FIGHT")

pick2 = input("Type your pick of Rock, Paper, or Scissors: ").lower()

if pick2.lower() == "rock" or pick2.lower() == "paper" or pick2.lower() == "scissors":
    print("Player 1 you chose",pick2,"for Round 2")
    fightoptions = ["rock","paper","scissors"]
    cpu_pick2 = random.choice(fightoptions)
    if pick2 == "rock" and cpu_pick2 == "paper":
        print("CPU chose paper - You Lost...")
    elif pick2 == "rock" and cpu_pick2 == "scissors":
        print("CPU chose scissors - YOU WIN!!!!")
        score += 1
    elif pick2 == "rock" and cpu_pick2 == "rock":
        print("CPU chose rock - DRAW")
    
    elif pick2 == "paper" and cpu_pick2 == "rock":
        print ("CPU chose rock - YOU WIN!!!!")
        score += 1

    elif pick2 == "paper" and cpu_pick2 == "paper":
        print("CPU chose paper - DRAW")

    elif pick2 == "paper" and cpu_pick2 == "scissors":
        print ("CPU chose scissors - You Lost...")

    elif pick2 == "scissors" and cpu_pick2 == "rock":
        print("CPU chose rock - You Lost...")

    elif pick2 == "scissors" and cpu_pick2 == "scissors":
        print ("CPU chose scissors - DRAW")

    elif pick2 == "scissors" and cpu_pick2 == "paper":
        print("CPU chose paper - YOU WIN!!!!")
        score += 1


else: 
    print("Error choose Rock, Paper, or Scissors")
    quit()

print("Player 1 - Score:",score)

print("\n")

print("Round 3 - FIGHT")

pick3 = input("Type your pick of Rock, Paper, or Scissors: ").lower()

if pick3.lower() == "rock" or pick3.lower() == "paper" or pick3.lower() == "scissors":
    print("Player 1 you chose",pick3,"for Round 3")
    fightoptions = ["rock","paper","scissors"]
    cpu_pick3 = random.choice(fightoptions)
    if pick3 == "rock" and cpu_pick3 == "paper":
        print("CPU chose paper - You Lost...")
    elif pick3 == "rock" and cpu_pick3 == "scissors":
        print("CPU chose scissors - YOU WIN!!!!")
        score += 1
    elif pick3 == "rock" and cpu_pick3 == "rock":
        print("CPU chose rock - DRAW")
    
    elif pick3 == "paper" and cpu_pick3 == "rock":
        print ("CPU chose rock - YOU WIN!!!!")
        score += 1

    elif pick3 == "paper" and cpu_pick3 == "paper":
        print("CPU chose paper - DRAW")

    elif pick3 == "paper" and cpu_pick3 == "scissors":
        print ("CPU chose scissors - You Lost...")

    elif pick3 == "scissors" and cpu_pick3 == "rock":
        print("CPU chose rock - You Lost...")

    elif pick3 == "scissors" and cpu_pick3 == "scissors":
        print ("CPU chose scissors - DRAW")

    elif pick3 == "scissors" and cpu_pick3 == "paper":
        print("CPU chose paper - YOU WIN!!!!")
        score += 1


else: 
    print("Error choose Rock, Paper, or Scissors")
    quit()

print("Player 1 - Final Score:",score)
print("\n")
