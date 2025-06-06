# Tom Cruise Movies Scraper

Этот проект предназначен для автоматического извлечения первых 10 фильмов с актёром Томом Крузом со страницы [Letterboxd](https://letterboxd.com/actor/tom-cruise/) и сохранения их в Excel-файл.

## Установка

Установите необходимые библиотеки:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Использование

Запустите скрипт `scrape_tom_cruise_movies.py`. Он выполнит парсинг страницы, получит названия фильмов и сохранит их в файл `tom_cruise_movies.xlsx`.

## Структура проекта

- `scrape_tom_cruise_movies.py` — основной скрипт для парсинга и сохранения данных.

