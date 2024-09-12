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
    chars['attributes'] = list(vars(obj).keys())
    chars['methods'] = inspect.getmembers(obj, predicate=inspect.ismethod)
    chars['module'] = __name__ #inspect.getmodulename(obj)
    chars['file'] = path.basename(inspect.getfile(obj.fly))

    return chars

eagle_obj = Eagle()
pprint(introspection_info(eagle_obj))









