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

    # print(f' {soup.find("p", class_="story").findAll("a", class_="sister")} ')
    #
    # print(f' {soup.find("a", {"class" : "sister", "id" : "link1"}).text} ')
    #
    # for i in soup.findAll("a", {"class": "sister"}):
    #     print(f' ****** {i.text} ')

    with open("index.html") as file:
        html_index = file.read()
        # print(src)
    soup_lxml = BeautifulSoup(html_index, "lxml")

    print(f' {soup_lxml.find("div", class_="user__birth__date").next_element.next_element } ')
    print(f' {soup_lxml.find("div", class_="user__birth__date").next_element.next_element.parent.text} ')



# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find() .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)
#
# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)
#
# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find(class_="user__name").find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
#     print(item.text)

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

# .find_parent() .find_parents()

# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)

# .next_element .previous_element
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# .find_next_sibling() .find_previous_sibling()
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

# links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#
#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]
#
#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)

# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)

# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)