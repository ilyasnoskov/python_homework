from validators.validators_library import *
from validators.start_info_about_me import start_info
start_info()


print("""Вивести на екран букву "W" з символів "*" (зірочка).

""")


while True:
    k=int_input('')
    if k==1:
        def symbol():
            print('''
                **	    **	    **
                  **    **    **
                    **  **  **
                     ** ** **
                      ** **''')
        symbol()
    else:
        exit('BYE')