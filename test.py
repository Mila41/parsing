from bs4 import BeautifulSoup
import requests

skillbox = requests.get("https://live.skillbox.ru/")
print(skillbox.status_code)


skillbox.headers["Content-Type"]
skillsoup = BeautifulSoup(skillbox.content, "html.parser")  # Парсим html код, полученный с сайта
webinars = skillsoup.findAll(class_ = "webinar-card__title") # Поиск по классу в супе
# .string (BeautifulSoup) - способ получить текст элемента
# .strip (Python) - способ обрезать "лишнее" по краям строки
[w.string.strip() for w in webinars]
# Попробуем получить и название и дату вебинара
webinars_full = skillsoup.findAll(class_ = "webinars__item") # Ищем все карточки вебинаров
# Для каждой карточки вебинара: сделать следующее
for webinar in webinars_full:
    # У конкретной карточки (webinar) находим заголовок
    title = webinar.find(class_ = "webinar-card__title").string.strip()
    # И находим дату
    date = webinar.find(class_ = "webinar-card__date").string.strip()
    print(f"Вебинар {title} прошел {date}")