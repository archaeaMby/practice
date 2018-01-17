import random
guesses_made = 0
name = raw_input("Hello! What is your name?\n")

number = random.randint(1,20)
print("Well, {0}, I_am_thinking_of_a_number_between_1_and_20." .format(name))
while guesses_made < 4:
    guess = int(raw_input("Take a guess: "))
    guesses_made += 1

    if guess < number:
        print('Your_guess_is_too_low')
    if guess > number:
        print('Your_guess_is_too_high')
    if guess == number:
        break

if guess == number:
    print('Good_Job, {0}! You_guessed_my_number_in {1} guesses'.format(name, guesses_made))
else:
    print("Nope. The number I was thinking of was {0}, You have guessed {1} times".format(number, guesses_made))
