import scrapy
import logging
import json, os


def get_data_from_json_file_words(json_file_name):
    row = []

    try:
        with open(json_file_name, 'r') as file:
            data = json.load(file)

        for item in data:
            for key, value in item.items():

                if value['status'] == False:
                    row.append([value['word'],
                                value['id'],
                                value['status']])

    except Exception as ex:
        print(ex, os.path.abspath(__file__))

    return row


class DictSpider(scrapy.Spider):
    name = "dict"
    allowed_domains = ["dict.com"]
    file_json = '/home/fox/PycharmProjects/python_parsing/scrapy/dict_com/dict_com/spiders/words.json'
    words = get_data_from_json_file_words(file_json)

    # start_urls = [f"https://dict.com/ukrainisch-deutsch/{row[0]}" for row in words]

    def parse(self, response):
        print(f'parse {response.meta["id"]} {response.meta["word"]} ')

        word = response.xpath("//span[@class='lex_ful_entr l1']/text()").get()

        translation_xpath = "//span[@class='lex_ful_labl']/text() | //span[@class='lex_ful_v']/text() | //span[@class='lex_ful_tran w l2']/text()"
        translation = response.xpath(translation_xpath).getall() or None

        part_of_speech_xpath = "//span[@class='lex_ful_morf']/text()"
        part_of_speech = response.xpath(part_of_speech_xpath).get() or None

        german_alternatives_xpath = "//span[@class='lex_ful_coll2s w l1']/text() | //span[@class='lex_ful_cc']/text() | //span[@class='lex_ful_coll2t w l2']/text()"
        german_alternatives = response.xpath(german_alternatives_xpath).getall() or None

        logging.debug(f"translation_xpath: -{word}|{translation}|{part_of_speech}|{german_alternatives}")
        # logging.debug(f"translation_xpath: -{word}|{translation}|{part_of_speech_xpath}|{german_alternatives_xpath}")

        yield {
            "index": response.meta['index'],
            "id": response.meta['id'],
            "word": word,
            "translation": translation if translation else None,
            "part_of_speech": part_of_speech if translation else None,
            "german_alternatives": german_alternatives
        }
        print(
            f"index  - {response.meta['index']} -- translation_xpath: -{word}|{translation}|{part_of_speech}|{german_alternatives}")

    def start_requests(self):
        print('start_requests')
        for i, row in enumerate(self.words):
            if i > 10:
                break

            yield scrapy.Request(
                url=f"https://dict.com/ukrainisch-deutsch/{row[0]}",
                callback=self.parse,
                meta={'index': i, 'id': row[1]}
            )
