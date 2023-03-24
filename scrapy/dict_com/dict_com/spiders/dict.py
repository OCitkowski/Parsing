import scrapy


class DictSpider(scrapy.Spider):
    name = "dict"
    allowed_domains = ["dict.com"]
    start_urls = ["https://dict.com/ukrainisch-deutsch/{}".format(word) for word in ["Hallo", "der", "das"]]

    def parse(self, response):
        word = response.css("h1.lex_main_headword::text").get()
        translation = ", ".join(response.css("span.lex_ful_tran::text").getall())
        entry = response.css("span.lex_ful_entr.l1::text").get()
        pronunciation = response.css("span.lex_ful_pron::text").get()
        morphology = response.css("span.lex_ful_morf::text").get()
        form = response.css("span.lex_ful_form::text").get()

        yield {
            "word": word,
            "translation": translation,
            "entry": entry,
            "pronunciation": pronunciation,
            "morphology": morphology,
            "form": form
        }
