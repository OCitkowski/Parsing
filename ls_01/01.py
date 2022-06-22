html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""



if __name__ == '__main__':

    from bs4 import BeautifulSoup

    # soup = BeautifulSoup(html_doc, 'html.parser')
    soup = BeautifulSoup(html_doc, "lxml")

    print(f' {soup.find("p", class_="story").findAll("a", class_="sister")} ')

    # print(f' {soup.find("p", href_="http://example.com/elsie")} ')


    # print(f' {soup.findAll("href")}')

    # print('"Khal Drogo\'s favorite word is \"athjahakar\""')

    # print(soup.prettify())
    # print(f' {soup.title} , {soup.string} , {soup.name} , {soup.text} ')