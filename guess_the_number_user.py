import random

def guess_user_number(x):
    low = 1
    high = x
    feedback = ''
    while(feedback != 'c'):
        if high!=low:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H) , too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'YAY!!! You have guessed the correct number {guess}.')

guess_user_number(1000)