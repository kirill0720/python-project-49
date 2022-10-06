from random import randint, choice


RULE = 'What is the result of the expression?'


def generate_qa():
    N = 100  # max int for this game
    int1, int2 = randint(0, N), randint(0, N)
    operator = choice(['+', '-', '*'])

    question = f'{int1} {operator} {int2}'
    if operator == '+':
        answer = int1 + int2
    elif operator == '-':
        answer = int1 - int2
    else:  # *
        answer = int1 * int2

    return question, str(answer)
