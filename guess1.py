import random
n = random.randint(1,25)

for i in range(5):
    guess = int(input("Guess: "))

    if guess == n:
        print("Correct")
        exit()
    elif guess > n:
        print("Number too High")
    elif guess < n:
        print("Number too low")

print(f"Correct Answer = {n}")    
