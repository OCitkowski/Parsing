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


class JsonWriterPipelineOLD(object):
    def open_spider(self, spider):
        self.file = open('data.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # зчитування шаблонного файлу
        with open("data.json", "r") as filedata:
            data = filedata.read()

        data.append(item)
        print(f'item - {item}')
        # # запис значень з item в template
        data["word"] = item["word"]
        data["translation"] = item["translation"]
        data["part_of_speech"] = item["part_of_speech"]
        data["german_alternatives"] = item["german_alternatives"]
        # # ...

        # запис template у вихідний файл
        with open("data.json", "w") as filewrite:
            # json.dump(data, f, ensure_ascii=False, indent=4)
            filewrite.write(json.dumps(data, indent=4))

        return item

    def __process_item(self, item, spider):
        # Відкрийте файл та завантажте його в змінну data
        with open('deck.json', 'r') as f:
            data = json.load(f)
        i = 0
        # Перезаписати значення
        for note in data['notes']:
            fields = note['fields']
            i += 1

            if fields[0] == item["word"]:
                for i, field in enumerate(fields):

                    if i == 2:
                        fields[i] = item["translation"]
                    elif i == 7:
                        fields[i] = item["german_alternatives"]
                logging.debug(f"for: {i} -- {item['word']}| Ukr - {fields[2]} | german_alternatives - {fields[7]} ")

            # print(i, fields)

        # Зберегти нові дані у файл
        with open('deck.json', 'w') as f:
            json.dump(data, f)

        return item


class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("data.json", "r+")
        try:
            self.items = json.load(self.file)
        except ValueError:
            self.items = []

    def process_item(self, item, spider):
        # додавання item у список
        self.items.append(dict(item))

        # перемотка файлу на початок
        self.file.seek(0)

        # запис у вихідний файл
        json.dump(self.items, self.file, ensure_ascii=False, indent=4)

        # обрізання файлу, щоб він був тільки такого ж розміру, як вміщує даних
        self.file.truncate()

        return item

    def close_spider(self, spider):
        self.file.close()