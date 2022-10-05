import random

RULE = 'What number is missing in the progression?'


def generate_qa():
    p_len = random.randint(5, 10)  # length of progression
    p_start = random.randint(0, 90)
    p_lst = [str(x) for x in range(p_start, p_start + p_len)]
    ind = random.randint(0, p_len)  # index of hidden element
    answer = p_lst[ind]
    p_lst[ind] = '..'
    question = ' '.join(p_lst)

    return question, answer
