# Задача:использование сторонних библиотек в Python и применение их в различных задачах.
import requests
# import pandas
# import matplotlib.pyplot as plt

from pprint import pprint

"""
Получаем данные о погоде в выбранном городе и на выбранное количество дней 1-14, записываем 
полученные данные в переменную result в формате json.
Далее функцией parse_weather_data парсим json и получаем из него все полученные даты с минимальной и максимальной
температурой за указанный день.
"""


class WeatherForecast:
    def __init__(self, city, days):
        self.city = city
        self.days = days
        self.URL = 'http://api.weatherapi.com/v1/forecast.json'

    def run(self):
        headers = {'key': '132022b25e5b463e9fa161802241111', 'Content-Type': 'application/json'}
        params = {'q': self.city, 'days': self.days, 'lang': 'ru'}
        res = requests.get(self.URL, headers=headers, params=params)
        if res.ok:
            try:
                res = res.json()
            except requests.exceptions.JSONDecodeError as exc:
                print(f'Содержимое ответа не в формате json. Ошибка: {exc}',
                      'От источника был получен следующий ответ:', res, sep='\n')
            else:
                pass
        return res

    @staticmethod
    def parse_weather_data(res):
        if not res or 'forecast' not in res:
            print("Нет данных для обработки.")
            return None

        forecast_days = result['forecast']['forecastday']
        total_dates = {}

        for day in forecast_days:
            date = day['date']
            day_temp_min = day['day']['mintemp_c']
            day_temp_max = day['day']['maxtemp_c']
            total_dates[date] = [day_temp_min, day_temp_max]  # Добавляем дату и температуры в словарь

        return total_dates


# Пример использования
weather = WeatherForecast('Кувандык', 10)
result = weather.run()
weather_data = weather.parse_weather_data(result)
pprint(weather_data)  # Используем pprint для более красивого вывода
