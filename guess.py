import random
n = random.randint(1,10)
guess = int(input("Guess: "))

if guess == n:
    print("Correct")
else: 
    print("incorect")
    print(n)

