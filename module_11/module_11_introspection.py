from inspect import getmodule
from random import randint
from pprint import pprint


class Car:
    def __init__(self, color, year, model):
        self.color = color
        self.year = year
        self.model = model

    '''
        Хочу перекрасить свой автомобиль, но не решил в какой цвет.
        Если цвет моего автомобиля присутствует в палитре, то не перекрашивать его, если такой цвет
        в палитре отсутствует, то перекрасить в любой цвет из палитры выбрав его рандомно.
    '''
    def get_color(self):
        colors = ['red', 'blue', 'black', 'gold']
        if self.color.lower() not in colors:
            self.color = colors[randint(0, len(colors) - 1)]
        return self.color


obj = Car('wite', 1990, 'BMW')


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'metods': dir(obj),
        'module': getmodule(obj)
    }


number_info = introspection_info(obj)
pprint(number_info)
