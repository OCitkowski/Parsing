___
venv

    python3 -m venv venv
    source venv/bin/activate  (deactivate)

___
requirements

    pip freeze > requirements.txt 
    pip install -r requirements.txt
    pip uninstall requirements.txt
___
Scrapy

    pip install Scrapy

    scrapy startproject dict_com
    cd dict_com

Створити новий файл зі Spider класом за допомогою команди
    scrapy genspider [ім'я Spider] [домен].

або команда 
    scrapy genspider myspider example.com -p /path/to/myproject 
    створить новий файл у папці "/path/to/myproject/spiders".

    scrapy crawl dict 

Щоб зберегти інформацію, яку ви отримали під час парсингу, у файл, 
    ви можете використовувати Scrapy's Feed exports або Item pipelines.

Feed exports: Цей метод дозволяє зберігати дані у файлівому форматі. 
    Для використання цього методу, ви повинні вказати формат виводу та ім'я файлу 
    у конфігураційному файлі settings.py.

Наприклад, якщо ви бажаєте зберегти дані у CSV форматі, то ви можете додати 
    наступний рядок до settings.py:

    FEED_FORMAT = "csv"
    FEED_URI = "data.csv"

Після цього, Scrapy збереже дані у файл data.csv.

___

