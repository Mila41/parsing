import requests
from bs4 import BeautifulSoup

detmir = requests.get("https://detmir.ru/") # Делаем запрос и сохраняем ответ в переменную
# HTTP-ответ (response)
print(detmir.status_code) # 200 - ок, 300 - редирект(перенаправление), 400 - ошибка запроса, 500 - ошибка сервера
# Content-Type один из заголовков в HTTP
detmir.headers["Content-Type"]
detmirsoup = BeautifulSoup(detmir.content, "html.parser") # Парсим html код, полученный с сайта
heading = detmirsoup.findAll(class_ = "kl") # Поиск по классу в супе
# .string (BeautifulSoup) - способ получить текст элемента
# .strip (Python) - способ обрезать "лишнее" по краям строки
print([h.string.strip() for h in heading])
