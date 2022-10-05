import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_qa():
    question = random.randint(0, 100)
    answer = 'no' if question % 2 else 'yes'
    return question, answer
