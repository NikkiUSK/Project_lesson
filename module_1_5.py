immutable_var = (1, 2, 'str', True, [3, 4, 5])
print(f'\nImmutable tuple: {immutable_var}')

# immutable_var[0] = 3
# immutable_var[-1] = False
# print(immutable_var)
# Объект изначально задан как неизменяемый тип данных (кортеж / tuple),
# при попытках внести изменения в терминал вывалится ошибка типа, но если в кортеж добавить изменяемый объект,
# то такая монипуляция возможна:

immutable_var[-1][1] = 44
print(f'New immutable tuple: {immutable_var}')

mutable_list = [1, 2, 'str', True, [3, 4, 5]]
print(f'\nMutable list: {mutable_list}')
mutable_list[0] = 10
mutable_list[2] = 'int'
mutable_list[3] = False
mutable_list[-1][1] = 555
print(f"New mutable list: {mutable_list}")


