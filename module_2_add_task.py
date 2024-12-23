import random

#Ввод вручную
def create_password_1(l):
    correct_number = []
    for i in range(1, l):
        for j in range(2, l):
            if l % (i+j) == 0 and i < j:
                correct_number.append(i)
                correct_number.append(j)
            else:
                pass
    p = ''.join(str(x) for x in correct_number)
    return p

def enter_first_field():
    while True:
        first_field = int(input('Напишите число из первого поля: '))
        if 3 < first_field <= 20:
            password_1 = create_password_1(first_field)
            print(f'Ваш пароль от двери: {password_1}')
            break
        else:
            print('В первом поле могут быть только числа от 3 до 20, видимо вы плохо посмотрели :(')
            print('Попробуйте еще раз!\n')
            continue

enter_first_field()

#Случайное число
def create_password_2():
    ff = random.randint(3, 21)
    correct_number = []
    for i in range(1, ff):
        for j in range(2,ff):
            if ff % (i+j) == 0 and i < j:
                correct_number.append(i)
                correct_number.append(j)
            else:
                pass
    p = ''.join(str(x) for x in correct_number)
    return p, ff

password_2, first_field_2 = create_password_2()
print(f'\nДля числа {first_field_2}, паролем будет: {password_2}')