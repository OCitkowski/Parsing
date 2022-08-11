from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cr_graphy.crypt import write_key, load_key, encrypt, decrypt
import time, random, os

from inst_bot.copy_auth import *


def crypt_auth(file_name):

    key_name = 'bot' + '.key'
    # file_name = 'test' + '.py'
    prefix = 're_'

    if os.path.isfile(key_name):
        print('Key is exists')
    else:
        write_key(key_name)
        print(f'Creating the {key_name} full success')

    key = load_key(key_name)

    if os.path.isfile(prefix + file_name):

        decrypt(file_name, key, prefix)
        os.remove('re_' + file_name)

    else:
        encrypt(file_name, key, prefix)

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

    if os.path.isfile('re_auth_data.py'):
        crypt_auth('auth_data.py')

    login()
    crypt_auth('auth_data.py')
    #
    # if os.path.isfile('auth_data.py'):
    #     crypt_auth('auth_data.py')