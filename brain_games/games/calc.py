import random


RULE = 'What is the result of the expression?'


def generate_qa():
    int1 = random.randint(0, 100)
    int2 = random.randint(0, 100)
    operator = random.choice(['+', '-', '*'])

    question = f'{int1} {operator} {int2}'
    if operator == '+':
        answer = int1 + int2
    elif operator == '-':
        answer = int1 - int2
    else:  # *
        answer = int1 * int2

    return question, str(answer)
