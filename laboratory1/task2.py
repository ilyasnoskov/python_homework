from validators.validators_library import *
from validators.start_info_about_me import start_info
start_info()


print("""
Послуги телефонної мережі оплачуються за таким правилом: за розмови до А хвилин в місяць - В грн.,
а розмови понад встановлену норму оплачуються з розрахунку З грн. за хвилину.
Написати програму, яка обчислює плату за користування телефоном для уведеного часу розмов за місяць. Дані вводити з клавіатури.
""")


while True:
    k = int_input('')
    if k == 1:
        def phone_service(a,b,time):
            var1 = float1_input(a)
            var2 = float2_input(b)
            var3 = float3_input(time)
            delta = var3 - var1
            if var3 <= var1:
                return var2
            else:
                return var2 + 3*delta

        print(phone_service(input('Введіть хвилини тарифу:'), input("Введіть ціну за тариф:"),input("Введіть скільки хвилин було використано:")))
    else:
        exit('BYE')