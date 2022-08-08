from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import password, user_name
import time, random

def login(password, user_name):

    browser = webdriver.Chrome('/home/fox/PycharmProjects/python_parsing/inst_bot/chromedriver')

    browser.get('https://www.instagram.com/')
    time.sleep(random.randrange( 3, 5))

    username_input = browser.find_element('name', 'username')
    username_input.clear()
    username_input.send_keys('xdfgjfgdhj')

    time.sleep(random.randrange(3, 5))

    password_input = browser.find_element('name', 'password')
    password_input.clear()
    password_input.send_keys('xdfgjfgdhj')

    time.sleep(random.randrange(3, 5))

    password_input.send_keys(Keys.ENTER)

    username_input = browser.find_element('name', 'username')
    username_input.clear()


    time.sleep(random.randrange(3, 5))
    browser.close()
    browser.quit()

login(password, user_name)