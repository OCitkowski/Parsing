import scrapy
import logging


def get_words_from_file(full_file_name: str = None) -> list:
    words = []

    if full_file_name == None:
        return words

    file_txt = open(full_file_name, "r+")

    while True:
        row = file_txt.readline()
        if row == '':
            break
        else:
            new_word = row.split("|")[0]
            words.append(new_word)

    return words


class DictSpider(scrapy.Spider):
    name = "dict"
    allowed_domains = ["dict.com"]
    words = get_words_from_file('new.txt')

    start_urls = ["https://dict.com/ukrainisch-deutsch/{}".format(word) for word in words]

    def parse(self, response):
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


if __name__ == '__main__':
    get_words_from_json_file(full_file_name='deck.json')
