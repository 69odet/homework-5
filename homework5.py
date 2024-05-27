my_dict = {'Nasty': 2004, 'Dimas': 2002, 'Sasha': 2006 }
print(my_dict)
print(my_dict['Dimas'])
print(my_dict.get('Sofiy', 'Такого ключа нет'))
my_dict.update({'Sofiy': 2000,
                'Mikita': 2004})
print(my_dict)
del my_dict['Sasha']
print(my_dict)
my_set = {10, 20, 30, 40, 10, 20, 30, 'int', True, (10, 20, 30)}
print(my_set)
list = [10, 20, 30, 40, 20, 40, 10]
list = set(list)
print(list)
print(list.add(50))
print(list.add(60))
print(list)
print(list.discard(40))
print(list)
