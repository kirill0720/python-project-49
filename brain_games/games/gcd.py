import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def generate_qa():
    int1 = random.randint(0, 100)
    int2 = random.randint(0, 100)

    question = f'{int1} {int2}'
    answer = math.gcd(int1, int2)

    return question, str(answer)
