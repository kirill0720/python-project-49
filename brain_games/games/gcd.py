from random import randint
import math

RULE = 'Find the greatest common divisor of given numbers.'


def generate_qa():
    N = 100
    int1, int2 = randint(0, N), randint(0, N)

    question = f'{int1} {int2}'
    answer = math.gcd(int1, int2)

    return question, str(answer)
