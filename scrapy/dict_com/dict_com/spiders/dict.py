import scrapy
import logging
import json


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
    _json_file_name = ''

    start_urls = ["https://dict.com/ukrainisch-deutsch/{}".format(word) for i, word in enumerate(words) if i < 10]

    def get_data_from_json_file(self):
        words = []
        try:
            with open(self._json_file_name + '.json', 'r') as read_file:
                template = json.load(read_file)
                self.logger.info(f"{self._json_file_name}.json get data from json file")
                for i in template["translation"]
                words.append()

        except:
            self.logger.info(f"{self._json_file_name}.json don`t get data from json file")

            # заміна значення "translation" у шаблонному файлі
            with open("template.json") as f:
                template = json.load(f)
            template["translation"] = item["translation"]
            with open("template.json", "w") as f:
                json.dump(template, f, indent=4)

        return words

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'email': 'your_email',
                'password': 'your_password'
            },
            callback=self.after_login
        )

    def after_login(self, response):

        # Перевірка, що авторизація пройшла успішно
        if "Welcome" in str(response.body):
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

        else:
            self.logger.error("Login failed")


class LoginSpider(scrapy.Spider):
    name = 'login_spider'
    allowed_domains = ['dict.com']
    start_urls = ['https://dict.com/ukrainisch-deutsch/noch']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'email': 'your_email',
                'password': 'your_password'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # Перевірка, що авторизація пройшла успішно
        if "Welcome" in str(response.body):
            self.logger.info("Login successful!")
        else:
            self.logger.error("Login failed")


if __name__ == '__main__':
    pass
    # get_words_from_json_file(full_file_name='deck.json')
