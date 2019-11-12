import re
from validators.validators_library import *
from validators.start_info_about_me import start_info
start_info()

while True:
    k = int1_input('')
    if k == 1:
        def func():
            n = int_input(input('Введіть кількість повторень:'))
            x = float_input(input('Введіть значення x:'))
            sum = 0

            for i in range(1, n+1):

                sum = sum + (x - i)**2
            return print(sum)
        func()
    else:
        exit('BYE')