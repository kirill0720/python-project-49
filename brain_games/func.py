import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(game):
    name = welcome_user()

    print(game.RULE)

    correct_count = 0
    while correct_count < 3:
        question, answer = game.generate_qa()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:  # wrong answer
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
        correct_count += 1
    else:  # user gave 3 correct answers
        print(f'Congratulations, {name}!')
