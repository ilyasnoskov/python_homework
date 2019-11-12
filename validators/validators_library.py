import re

def int_input(text):
    '''
    :param text: (str)
        123132 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (int)
    '''
    pattern_int = r"^[-\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Недопустиме значення, спробуйте ще раз:")
    return int(user_input)

def int1_input(text):
    '''
    :param text: (str)
        123132 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (int)
    '''
    pattern_int = r"^[-\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Щоб запустити програму натисніть 1:")
    return int(user_input)

def float_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[-\d]\d*\.?\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Недопустиме значення, введіть ще раз:")
    return float(user_input)

def float1_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть хвилини тарифу типу float >0:")
    return float(user_input)

def float2_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть ціну за тариф типу float >0:")
    return float(user_input)


def float3_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть кількість використаних хвилин типу float >0:")
    return float(user_input)

import re

def int_input(text):
    '''
    :param text: (str)
        123132 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (int)
    '''
    pattern_int = r"^[-\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Щоб почати натисніть 1, щоб вийти натисніть відмінну від 1 клавішу:")
    return int(user_input)

def float_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[-\d]\d*\.?\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Enter float:")
    return float(user_input)

def float1_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть хвилини тарифу типу float >0:")
    return float(user_input)

def float2_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть ціну за тариф типу float >0:")
    return float(user_input)


def float3_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[^0\D]\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Введіть кількість використаних хвилин типу float >0:")
    return float(user_input)

