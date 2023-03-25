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

    def parse_old(self, response):
        # word = response.css("h1.lex_main_headword::text").get()
        # translation = ", ".join(response.css("span.lex_ful_tran::text").getall())
        # entry = response.css("span.lex_ful_entr.l1::text").get()
        # pronunciation = response.css("span.lex_ful_pron::text").get()
        # morphology = response.css("span.lex_ful_morf::text").get()
        # form = response.css("span.lex_ful_form::text").get()

        word = response.xpath("//span[@class='lex_ful_entr l1']/text()").get()
        translation_xpath = "//span[@class='lex_ful_samp2']//text() | //span[@class='lex_ful_c']//text() | //span[@class='lex_ful_samp2s w l1']//text() | //span[@class='lex_ful_samp2t w l2']//text() | //span[@class='lex_ful_samp2s w l1']/w/text()"
        translation = response.xpath(translation_xpath).getall()



        morfology_xpath = "//span[@class='lex_ful_morf'][2]/text()"
        morfology = response.xpath(morfology_xpath).get()

        entry = 'entry'
        pronunciation = 'pronunciation'

        form = 'form'

        yield {
            "word": word,
            "translation": translation,
            "entry": entry,
            "pronunciation": pronunciation,
            "morphology": morfology,
            "form": form
        }

    def parse(self, response):
        word = response.xpath("//span[@class='lex_ful_entr l1']/text()").get()
        translation = {}
        translation_xpath = "//tr[contains(@class, 'lex_ful_tran w l2') and not(@class='lex_ful_tr more')]/td"
        logging.debug(f"translation_xpath: -{translation_xpath}")
        for td in response.xpath(translation_xpath):
            logging.info(f"td: -{td}")
            label = td.xpath("span[@class='lex_ful_labl']/text()").get()
            if label:
                label = label.strip(".")
                value = " ".join(td.xpath(".//w/text()").getall())
                translation[label] = value
        morfology_xpath = "//span[@class='lex_ful_morf']/text()"
        morfology = response.xpath(morfology_xpath).get() or None
        entry = 'entry'
        pronunciation = 'pronunciation'
        form = 'form'

        yield {
            "word": word,
            "translation": translation if translation else None,
            "entry": entry,
            "pronunciation": pronunciation,
            "morphology": morfology,
            "form": form
        }