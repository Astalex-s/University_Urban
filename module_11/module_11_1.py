# Задача:использование сторонних библиотек в Python и применение их в различных задачах.
import requests
import pandas as pd
import matplotlib.pyplot as plt

"""
Раьота с библиотекой requests.
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

    '''
    Работа с библиотекой pandas. 
    Создаем таблицу excel. Если данные от сервиса получены заносим их в созданную таблицу
    '''

    @staticmethod
    def save_to_excel(data, filename='weather_forecast.xlsx'):
        if data is None:
            print("Нет данных для записи в Excel.")
            return

        # Преобразуем данные в DataFrame
        df = pd.DataFrame.from_dict(data, orient='index',
                                    columns=['Temp min(°C)', 'Temp max(°C)'])

        # Записываем DataFrame в Excel файл
        df.index.name = 'Data'
        df.to_excel(filename)

    '''
    Работа с библиотекой matplotlib.
    Получаем данные, если они есть из таблицы excel. На основе полученных данных строим график температур 
    в выбранном городе. В графике рисуем две кривые изменения температур в выбранном диапазоне дней, начиная
    с текущей даты. График сохраняем в файл формата png.
    '''
    def plot_weather_data(self, data):
        if data is None:
            print("Нет данных для построения графика.")
            return

        df = pd.DataFrame.from_dict(data, orient='index',
                                    columns=['Temp min(°C)', 'Temp max(°C)'])

        # Построение графика
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['Temp min(°C)'], marker='o', label='Temp min(°C)',
                 color='blue')
        plt.plot(df.index, df['Temp max(°C)'], marker='o', label='Temp max(°C)',
                 color='red')

        plt.title(f'Прогноз погоды для города {self.city}')
        plt.xlabel('Дата')
        plt.ylabel('Температура (°C)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()

        # Сохраняем график в файл
        plt.savefig(f'{self.city}_weather_forecast.png')

        # Показываем график
        plt.show()


if __name__ == '__main__':
    weather = WeatherForecast('Москва', 5)
    result = weather.run()
    weather_data = weather.parse_weather_data(result)
    weather.save_to_excel(weather_data)
    weather.plot_weather_data(weather_data)
