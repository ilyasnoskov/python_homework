import re
from validators.validators_library import *
from validators.start_info_about_me import start_info
start_info()

print(''''Дано додатні числа A і B (A>B). 
На відрізку довжиною A розміщено максимально можлива кількість відрізків довжиною B (без накладання). 
Не використовуючи операції множення і ділення, знайти кількість відрізків B, розміщених на відрізку A.\n''')


def segments():
    a = int_input(input('Введіть значення більшого відрізку А:'))
    b = int_input(input('Введіть значення меншого відрізка В:'))
    amount = 0
    if a>b and b == 1:
        for i in range(0, a, b):
            amount+=1
        return print(amount)
    elif a>b and b>1:
        for i in range(1, a, b):
            amount+=1
        return print(amount)
    else:
        print('Відрізок А має бути більшим за В\n')


while True:
    k = int1_input('')
    if k==1:
        segments()
    else:
        exit('BYE')