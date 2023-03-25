# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import logging


class DictComPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('data.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # збереження даних у JSON форматі
        try:
            data = {
                "****": 'tttt',
                "word": item["word"],
                "translation": item["translation"],
                "morphology": item["morphology"]
            }
            line = json.dumps(data) + "\n"
            logging.info(f"line: -{line}")

        except Exception as e:

            logging.error(f"Error, json dumped : {e}")



        # заміна значення "translation" у шаблонному файлі
        with open("template.json") as f:
            template = json.load(f)
        template["translation"] = item["translation"]
        with open("output.json", "w") as f:
            json.dump(template, f, indent=4)

        # запис даних у вихідний файл
        self.file.write(line)
        return item

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        logging.info(f"Processed item: {item['word']}")
        return item
