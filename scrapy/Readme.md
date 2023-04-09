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

Команда crawl була виконана в неправильному каталозі. Переконайтеся, що ви виконуєте команду scrapy crawl spider_name в каталозі зі скриптом, де знаходиться scrapy.cfg файл.

Ви використовуєте стару версію Scrapy, яка не підтримує команду crawl. Відкрийте командний рядок і введіть scrapy version, щоб перевірити, яка версія Scrapy встановлена. Якщо ви використовуєте застарілу версію, оновіть її до останньої версії за допомогою pip install --upgrade scrapy.


---
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
в мене вже є файл pipelines.py у папці проекту. з таким кодом. його заміняти?
    class DictComPipeline:
        def process_item(self, item, spider):
            return item


---
Щоб зпарсити локальний файл HTML у Scrapy shell, ви можете використовувати команду fetch і передати їй шлях до вашого локального файлу.

Ось приклад:

Запустіть Scrapy shell в терміналі, використовуючи команду 
        
    scrapy shell.
Використовуйте команду fetch та передайте їй шлях до вашого локального файлу. Наприклад, якщо ваш файл HTML знаходиться у тій же теки, що і ваш термінал, то ви можете використати таку команду:
   
   
    fetch('file:////gehen.html')


Після цього ви можете використовувати селектори, щоб отримати дані з вашого файлу HTML. Наприклад:

   
    response.css('h1::text').get()

Будьте уважні, щоб правильно вказати шлях до вашого файлу HTML у команді fetch. Якщо ви використовуєте операційну систему Windows, не забудьте використовувати подвійні зворотні слеші для шляхів, наприклад:

   
    fetch('file:///C:\\path\\to\\your\\local\\file.html')
