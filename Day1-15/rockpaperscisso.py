import random

rocks = 0
paper = 1
scissors = 2

choose_random = random.randint(0, 2)




mychoice = int(input("Enter your choice (0 for Rocks, 1 for Paper, 2 for Scissors): "))

if choose_random == mychoice:
    print("It's a tie!")
elif choose_random == rocks and mychoice == paper:
    print("You win!")
elif choose_random == rocks and mychoice == scissors:
    print("Computer wins!")
elif choose_random == paper and mychoice == rocks:
    print("Computer wins!")
elif choose_random == paper and mychoice == scissors:
    print("You win!")
elif choose_random == scissors and mychoice == rocks:
    print("You win!")
elif choose_random == scissors and mychoice == paper:
    print("Computer wins!")
else:
    print("Invalid choice. Please enter 0, 1, or 2.")

if choose_random == 0:
    print("Computer chose: Rocks")
elif choose_random == 1:
    print("Computer chose: Paper")
else:
    print("Computer chose: Scissors")    
print(choose_random)