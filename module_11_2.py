# Интроспекция
# Задание: создать функцию "introspection_info"

import inspect
from pprint import pprint
from os import path

class Eagle():  # Орёл

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

def introspection_info(obj):
    chars = {}
    chars['type'] = type(obj)
    chars['attributes'] = [i for i in dir(obj) if not callable(getattr(obj,i))]
    chars['methods_all'] = [i for i in dir(obj) if callable(getattr(obj,i))]
    chars['methods_of_object'] = [i[0] for i in inspect.getmembers(obj, predicate=inspect.ismethod)]

    chars['module'] = obj.__module__ if hasattr(obj, '__module__') else obj.__class__.__module__

    try:
        chars['file'] = path.basename(inspect.getfile(obj))
    except TypeError:
        try:
            chars['file'] = path.basename(inspect.getfile(type(obj)))
        except:
            chars['file'] = obj.__class__.__module__

    return chars

print('Object of class Eagle\n---------------------------------------------------------------')
eagle_obj = Eagle()
pprint(introspection_info(eagle_obj))

# print('\nFunction introspection_info\n---------------------------------------------------------------')
# func_obj = introspection_info
# pprint(introspection_info(func_obj))

print('\nFunction inspect.ismethod\n---------------------------------------------------------------')
func_obj = inspect.ismethod
pprint(introspection_info(func_obj))

print('\nNumber 42\n---------------------------------------------------------------')
number_obj = 42
pprint(introspection_info(number_obj))









