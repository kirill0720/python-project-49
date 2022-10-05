import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa():
    int1 = random.randint(0, 100)
    question = str(int1)

    for i in range(2, int1):
        if int1 % i == 0:
            answer = 'no'
            break
    else:
        answer = 'yes'

    return question, answer
