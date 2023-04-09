import scrapy
import logging
import json, os


def get_data_from_json_file(json_file_name):
    template = None

    try:
        with open(json_file_name, 'r') as read_file:

            template = json.load(read_file)

    except Exception as ex:
        print(ex, os.path.abspath(__file__))
    # finally:
    #     read_file.close()

    return template


class DictSpider(scrapy.Spider):
    name = "dict"
    allowed_domains = ["dict.com"]
    file_json = '/home/fox/PycharmProjects/python_parsing/scrapy/dict_com/dict_com/spiders/words.json'
    words = get_data_from_json_file(file_json)

    start_urls = ["https://dict.com/ukrainisch-deutsch/{}".format(word) for i, word in enumerate(words) if i < 2]

    # start_urls = ['https://dict.com/ukrainisch-deutsch/haben', 'https://dict.com/ukrainisch-deutsch/gehen']

    def parse(self, response):
        self.logger.info("Login successful!")

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
            "word": word,
            "translation": translation if translation else None,
            "part_of_speech": part_of_speech if translation else None,
            "german_alternatives": german_alternatives
        }
        print(f"translation_xpath: -{word}|{translation}|{part_of_speech}|{german_alternatives}")
