import random

def guessing_game():
    target_num = random.randint(1, 99)
    
    print('Try to guess the number im thinking of!')
    print("A little hint it's below 100 XD")

    guesses_num = 0

    while True:
        guess = int(input('Take a guess:'))
        guesses_num += 1
    
        if guess == target_num:
            print(f'Wow! You guessed right in {guesses_num} tries!')
            break
    
        elif guess > target_num:
            print("You're guessing too high!")
            
        else:
            print('Try a higher number')

guessing_game()


