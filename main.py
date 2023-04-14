# Импорт библиотеки для запросов
import requests
# Импорт библиотеки для формирования ответа
from pprint import pprint
# Импорт библиотеки для форматирования времени
import datetime
# Импорт токена из файла конфиг
from config import open_weather_token

# Функция получения данных погоды
def get_weather(city, open_weather_token):

def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

if __name__ ==  '__main__':
    main()