from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, sides: list, filled: bool = False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        color_list = [r, g, b]
        color_list.sort()
        if color_list[0] < 0 or color_list[-1] > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, [radius])
        self.radius = radius

    def get_square(self):
        return pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, [a, b, c])
        self.sides = [a, b, c]

    def get_square(self):
        semi_perimeter = self.__len__() / 2
        s = sqrt(semi_perimeter * (semi_perimeter - self.sides[0]) * (semi_perimeter - self.sides[1])
                 * (semi_perimeter - self.sides[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        sides = [side_length] * self.sides_count
        super().__init__(color, sides)

    def get_volume(self):
        side_length = self.get_sides()[0]  # Длина стороны
        return side_length ** 3


# Примеры использования
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 6, 6, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
triangle1.set_color(200, 70, 15)  # Изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Длина окружности

# Проверка объёма (куба):
print(cube1.get_volume())  # Объем куба

# Проверка площади треугольника:
print(triangle1.get_square())
