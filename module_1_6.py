my_dict = {'Anya':2001, 'Pasha':1999, 'Nikita':1994, 'Roma':2005}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Pasha']}')
print(f'Not existing value: {my_dict.get('Masha', 'Not found')}')
del_key = my_dict.pop('Anya')
print(f'Deleted value: {del_key}')
print(f'Modified dictionary: {my_dict}')

my_set = {1, 1, 2, 2, 'String', 'String', True}
print(f"\nSet: {my_set}")
my_set.add(3)
my_set.remove(1)
print(f'Modified set: {my_set}')
