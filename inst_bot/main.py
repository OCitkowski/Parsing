from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import password, user_name
import time, random

def login(password, user_name):

    browser = webdriver.Chrome('/home/fox/PycharmProjects/python_parsing/inst_bot/chromedriver')

    browser.get('https://www.instagram.com/')
    time.sleep(random.randrange( 3, 5))

    browser.close()
    browser.quit()

login(password, user_name)