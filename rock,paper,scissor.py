import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == "rock":
        if you == "scissor":
            return False
        elif you == "paper":
            return True
    elif comp == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True
    elif comp == "scissor":
        if you == "rock":
            return True
        elif you == "paper":
            return False

print("Computer's turn: rock (r), paper (p), or scissor (s)?")
randNO = random.randint(1, 3)
if randNO == 1:
    comp = "rock"
elif randNO == 2:
    comp = "paper"
else:
    comp = "scissor"    
you = input("Your turn: rock (r), paper (p), or scissor (s)? ").lower()

result = gamewin(comp.lower(), you.lower())

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if result == None:
    print("The game is a tie!")
elif result:
    print('You win!')
else:
    print("You lose!")
