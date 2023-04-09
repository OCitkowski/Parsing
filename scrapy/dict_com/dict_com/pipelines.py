# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import logging


def save_data_in_json_file(self, data):
    result = False
    try:
        with open(self._json_file_name + '.json', 'w') as write_file:
            json.dump(data, write_file, ensure_ascii=False)
            result = True
        print(f'{self._json_file_name}.json save to root')
    except:
        print(f'{self._json_file_name}.json don`t save to root')
    return result


class DictComPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline:
    file_json = "/home/fox/PycharmProjects/python_parsing/scrapy/dict_com/dict_com/spiders/words.json"

    def open_spider(self, spider):
        self.file = open(self.file_json, "r+")
        try:
            self.items = json.load(self.file)
        except ValueError:
            self.items = []

    def process_item(self, item, spider):
        # перетворення номера на ціле число
        item_number = int(item["number"])

        # пошук слова за номером в списку
        for i, stored_item in enumerate(self.items):
            if stored_item["number"] == item_number:
                # заміна значення translation та зміна статусу
                self.items[i]["translation"] = item["translation"]
                self.items[i]["status"] = True
                break
        else:
            # якщо слово за номером не знайдено, додаємо новий запис
            self.items.append({
                "number": item_number,
                "translation": item["translation"],
                "status": True
            })

        # перемотка файлу на початок
        self.file.seek(0)

        # запис у вихідний файл
        json.dump(self.items, self.file, ensure_ascii=False, indent=4)

        # обрізання файлу, щоб він був тільки такого ж розміру, як вміщує даних
        self.file.truncate()

        return item

    def close_spider(self, spider):
        self.file.close()