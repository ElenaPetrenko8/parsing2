import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы актёра
url = 'https://letterboxd.com/actor/tom-cruise/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/115.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# Ищем список фильмов
movies = []

# Попробуем найти все карточки фильмов
film_items = soup.find_all('li', class_='poster-container')  # примерный селектор

for item in film_items:
    # Внутри каждого элемента ищем название фильма по alt у изображения
    title_tag = item.find('img', alt=True)
    if title_tag:
        title = title_tag['alt']
        movies.append(title)
    if len(movies) >= 10:
        break

# Выводим список фильмов
print("10 фильмов с Томом Крузом:")
for i, movie in enumerate(movies, start=1):
    print(f"{i}. {movie}")

# Сохраняем в Excel файл
df = pd.DataFrame({'Фильмы': movies})
df.to_excel('tom_cruise_movies.xlsx', index=False)
print("Список фильмов сохранён в файл 'tom_cruise_movies.xlsx'")