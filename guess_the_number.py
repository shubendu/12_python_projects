import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Enter the number between 1 and {x}: "))

        if guess > random_number:
            print("Your number is too high")
        elif guess < random_number:
            print("Your number is too low")

    print(f"YAY!!!! You have guessed the correct number {random_number}.")
        

guess(10)