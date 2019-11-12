from validators.validators_library import *
from validators.start_info_about_me import start_info
start_info()

while True:
    k=int_input('')
    if k==1:
        def task3(x):
            var1 = float_input(x)
            if var1 >= float(-3.5):
                return 4 * var1 ** 2 + 2 * var1 - 19
            elif var1 < float(3.5):
                return -(2 * var1 / (-4 * var1 + 1))

        print(task3(input('Введіть х:')))
    else:
        exit('BYE')