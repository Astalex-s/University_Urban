class Vehicle:  # Класс любого транспортного средства
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # список допустимых цветов для окрашивания

    def __init__(self, owner: str, __model: str,  __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):  # Метод возвращает наименование модели транспорта
        return f'Модель: {self.__model}'

    def get_horsepower(self):  # Метод возвращает мощность двиготеля транспорта
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):  # Метод возвращает цвет транспорта
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()