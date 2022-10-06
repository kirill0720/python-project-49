import prompt


def play(rule, func):
    '''Engine for brain-like games.
    INPUTS: rule message and a function to generate questions and answers.'''

    correct_count_limit = 3  # number of correct answer to exit the game

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(rule)

    correct_count = 0
    while correct_count < correct_count_limit:
        question, ans = func()
        print(f'Question: {question}')
        u_ans = prompt.string('Your answer: ')
        if u_ans != ans:  # wrong answer
            print(f"'{u_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
        correct_count += 1
    else:  # user gave enough correct answers
        print(f'Congratulations, {name}!')
