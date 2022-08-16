from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cr_graphy.crypt import write_key, load_key, encrypt, decrypt
import time, random, os
from selenium.webdriver.common.by import By
import pickle, json
from inst_bot.copy_auth import *


def crypt_auth(file_name):
    key_name = 'bot' + '.key'
    # file_name = 'test' + '.py'
    prefix = 're_'

    if os.path.isfile(key_name):
    # print('Key is exists')
        pass
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
    user_phone ='555777'
    # options
    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(executable_path = path, options = options)
    browser.get(site_path)
    time.sleep(random.randrange(2, 4))

    # cookies
    if not os.path.isfile(f"{user_phone}_cookies"):

        try:
            browser.delete_all_cookies()

            username_input = browser.find_element('name', 'username')
            username_input.clear()
            username_input.send_keys(user_name)

            time.sleep(random.randrange(2, 4))

            password_input = browser.find_element('name', 'password')
            password_input.clear()
            password_input.send_keys(password)

            time.sleep(random.randrange(3, 5))

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(50, 60))

            # pickle.dump(browser.get_cookies(), open(f"{user_phone}_cookies", "wb"))
            json.dump(browser.get_cookies(), open(f"{user_phone}_cookies", "w"))


            time.sleep(random.randrange(3, 5))
            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()
    else:
        # print(json.load(open(f"{user_phone}_cookies", "rb")))

        browser.delete_all_cookies()
        # for cookie in pickle.load(open(f"{user_phone}_cookies", "rb")):

        for cookie in json.load(open(f"{user_phone}_cookies", "r")):

                browser.add_cookie(cookie)

        time.sleep(5)
        browser.refresh()
        time.sleep(60)

        #




def hashtag_search(hashtag):
    browser = webdriver.Chrome(path)
    browser.get(site_path)
    time.sleep(random.randrange(2, 4))

    try:
        username_input = browser.find_element('name', 'username')
        username_input.clear()
        username_input.send_keys(user_name)

        time.sleep(random.randrange(2, 4))

        password_input = browser.find_element('name', 'password')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(3, 5))

        password_input.send_keys(Keys.ENTER)

        time.sleep(random.randrange(20, 25))
        # browser.close()
        # browser.quit()

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(5)

            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

                hrefs = browser.find_elements(By.TAG_NAME, "a")
                posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            print(hrefs)
            print(posts_urls)
            # posts_urls = []
            # for item in hrefs:
            #     href = item.get_attribute('href')
            #
            #     if "/p/" in href:
            #         posts_urls.append(href)
            #         print(href)

            for url in posts_urls:
                try:
                    browser.get(url)
                    time.sleep(3)
                    print('??????????')
                    like_button = browser.find_element(By.XPATH,
                                                       '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()

                    time.sleep(random.randrange(80, 100))
                    print('++++++++++')
                except Exception as ex:
                    print(f'------- {ex}')

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

    finally:
        browser.close()
        browser.quit()


if __name__ == '__main__':

    if os.path.isfile('re_auth_data.py'):
        crypt_auth('auth_data.py')

    login()
    # hashtag_search('surfing')
    crypt_auth('auth_data.py')
