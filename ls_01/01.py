html_text = """<html><head><title>The Dormouse's story</title></head>
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
    soup = BeautifulSoup(html_text, 'html.parser')
    # soup = BeautifulSoup(html_text, "lxml")

    print(f' {soup.find("p", class_="story").findAll("a", class_="sister")} ')

    print(f' {soup.find("a", {"class" : "sister", "id" : "link1"}).text} ')

    for i in soup.findAll("a", {"class": "sister"}):
        print(f' ****** {i.text} ')

    with open("index.html") as file:
        html_index = file.read()
        # print(src)
    soup_lxml = BeautifulSoup(html_index, "lxml")



