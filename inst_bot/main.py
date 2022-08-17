import time, random, os, json
from cr_graphy.crypt import write_key, load_key, encrypt, decrypt
from inst_bot.copy_auth import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException


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


def login(time_sleep: int = 3, close_browser: bool = False, proxy='85.26.146.169:80'):
    user_phone = '555777'

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    # chrome_options.add_argument('--single-process')
    # chrome_options.add_argument('--data-path=/tmp/data-path')
    # chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get("https://www.whatismyip.com/my-ip-information/")
    time.sleep(random.randrange(2, 4))
    browser.get(site_path)
    time.sleep(random.randrange(2, 4))

    # cookies
    if not os.path.isfile(f"{user_phone}_cookies"):

        try:
            browser.delete_all_cookies()

            username_input = browser.find_element('name', 'username')
            username_input.clear()
            username_input.send_keys(user_name)

            time.sleep(random.randrange(3, 5))

            password_input = browser.find_element('name', 'password')
            password_input.clear()
            password_input.send_keys(password)

            time.sleep(random.randrange(3, 5))

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(50, 60))

            json.dump(browser.get_cookies(), open(f"{user_phone}_cookies", "w"))

            time.sleep(random.randrange(3, 5))
            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()
    else:
        browser.delete_all_cookies()

        for cookie in json.load(open(f"{user_phone}_cookies", "r")):
            browser.add_cookie(cookie)

        time.sleep(random.randrange(3, 5))
        browser.refresh()
        time.sleep(random.randrange(3, 5))

        try:
            turn_on_button = browser.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            turn_on_button.click()

        except NoSuchElementException:
            print('sorry? but do not finded button`s')

        finally:
            time.sleep(time_sleep)

            if close_browser:
                browser.close()
                browser.quit()
            else:
                return browser


def hashtag_search(browser, hashtag, close_browser: bool = False, Unlike: bool = False):
    try:
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(3)

        for i in range(1, 4):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

            hrefs = browser.find_elements(By.TAG_NAME, "a")
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

        print(hrefs)
        print(posts_urls)

        for url in posts_urls:
            try:
                time_sleep = 5
                browser.get(url)
                time.sleep(time_sleep)
                like_button = browser.find_element(By.XPATH,
                                                   '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')

                print(f' start')
                print(f'accessible_name - {like_button.accessible_name}')
                if like_button.accessible_name == 'Like' and not Unlike:
                    like_button.click()
                    print(f' +')
                elif like_button.accessible_name != 'Like' and Unlike:
                    like_button.click()
                    print(f' -')
                print(f'accessible_name - {like_button.accessible_name}')
                print(f' end')
                # print(
                #     f'id - {like_button.id} /text - {like_button.text} /get_attribute - {like_button.get_attribute("aria-label")}')

                follow_button = browser.find_element(By.LINK_TEXT, 'Follow')
                print(follow_button.text)

                time.sleep(random.randrange(time_sleep, time_sleep + 2))
                browser.refresh()
                print(f' {url} - like OK')

            except NoSuchElementException:
                print('sorry? but do not n\'Like n\' finded button`s')

    except Exception as ex:
        print(f' (sorry? but do not finded link`s ) /  {ex} ')
        browser.close()
        browser.quit()

    finally:
        if close_browser:
            browser.close()
            browser.quit()


if __name__ == '__main__':

    if os.path.isfile('re_auth_data.py'):
        crypt_auth('auth_data.py')
    browser = login(5, False, '91.226.97.113:80')
    hashtag_search(browser, 'vinnytsia', False, True)
    crypt_auth('auth_data.py')
