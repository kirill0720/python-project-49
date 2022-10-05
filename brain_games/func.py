import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    while correct_count < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        ans = prompt.string('Your answer: ')
        if (number % 2 == 0 and ans == 'no') or \
           (number % 2 == 1 and ans == 'yes'):  # wrong answer is_even?
            reply = 'yes' if ans == 'no' else 'no'
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{reply}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
        correct_count += 1
    else:  # user gave 3 correct answers
        print(f'Congratulations, {name}!')
