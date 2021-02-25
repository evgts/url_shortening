import string
import random


def base_str():
    return string.ascii_letters + string.digits


def code_gen(code_len=20):
    """
    :param code_len: int to generate a code code_len length
    :return: str Lq1UQ2hngRdV9mo1sLkd
    """
    key_list = [random.choice(base_str()) for _ in range(code_len)]
    return "".join(key_list)
