Здесь Попытался реализовать тг бота на питоне + aiogram + google sheets

Бот помогает отправлять отчет по взвешиваню товаров
Товары, работники и тип упаковки нужно прописать тоже в гугл таблицах

Кто взвешивает - что взвешивает - в какой упаковке - вес

После предлагает отправить отчет в гугл таблицу

Для запуска вам нужен .енв файл с:
BOT_TOKEN = Ваш токен тг-бота
GOOGLE_SHEETS_DATA = id таблицы с данными 
должен содердать 3 страницы:
  1. "workers":
  | worker_id | Last Name | First Name | Middle Name |
  2. "products":
  | product_id | product |
  3. "packaging":
  | packaging_id | packaging |

GOOGLE_SHEETS_REPORTS = id таблицы куда будет загружаться отчет

Также необходимые модули можно установить по команде:
pip install -r requirements.txt

И запустить:
python main.py
