from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import password, user_name, path, site_path
import time, random

def login():

    browser = webdriver.Chrome(path)
    browser.get(site_path)
    time.sleep(random.randrange( 3, 5))

    try:
        username_input = browser.find_element('name', 'username')
        username_input.clear()
        username_input.send_keys(user_name)

        time.sleep(random.randrange(3, 5))

        password_input = browser.find_element('name', 'password')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(3, 5))

        password_input.send_keys(Keys.ENTER)

        time.sleep(random.randrange(30, 50))
        browser.close()
        browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


if __name__ == '__main__':
    login()