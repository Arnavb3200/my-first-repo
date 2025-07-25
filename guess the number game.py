import random

target = random.randint(1, 100)

while True:
        yourchoice = input("Guess the target number OR Quit(Q): ")

        if yourchoice.upper() == "Q":
            print("You quit the game.")
            break

        
        yourchoice = int(yourchoice)

        if yourchoice == target:
            print("Congrats, Correct Guess! 🎯")
            break
        elif yourchoice < target:
            print("Too small! Try a bigger number.")
        else:
            print("Too large! Try a smaller number.")


print("Game over ..........")
  







   
      
                     
