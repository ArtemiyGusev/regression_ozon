import random


def rand_string(length=int):
    return ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(length)])


def rand_int(from_number, to_number):
    return random.randint(from_number, to_number)