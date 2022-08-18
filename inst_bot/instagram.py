import time, random, os, json
from cr_graphy.crypt import write_key, load_key, encrypt, decrypt
from inst_bot.auth_data import password, user_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


class InstagramBot():
    """Instagram Bot"""

    def __init__(self, username, password, headless: bool = False, start_maximized: bool = True):

        self.username = username
        self.password = password
        self.link_by_default = 'https://www.instagram.com/'
        self.auth_file_name = 'auth_data.py'
        self.key_file_name = username + '_bot_instagram.key'
        self.prefix = 're_'
        self.time_sleep = 5
        self.min_time_sleep = 3

        self.browser = self.open_in_instagram(headless, start_maximized)
        self.is_cookies = self.set_cookies_by_user_id(username)


    def crypt_auth(self):

        if os.path.isfile(self.key_file_name):
            # print('Key is exists')
            pass
        else:
            write_key(self.key_file_name)
            print(f'Creating the {self.key_file_name} full success')

        key = load_key(self.key_file_name)

        if os.path.isfile(self.prefix + self.auth_file_name):
            decrypt(self.auth_file_name, key, self.prefix)
            os.remove('re_' + self.auth_file_name)
        else:
            encrypt(self.auth_file_name, key, self.prefix)


    def close_browser(self):

        # if not os.path.isfile(self.prefix + self.auth_file_name):
        #     self.crypt_auth()
        self.save_cookies_by_user_id(user_id=self.username)
        self.browser.close()
        self.browser.quit()


    def sleep_browser(self, hend_time_sleep:int = 0):

        if hend_time_sleep > 0:
            time.sleep(hend_time_sleep)
        elif self.min_time_sleep == 0:
            time.sleep(self.time_sleep)
        else:
            time.sleep(random.randrange(self.min_time_sleep, self.time_sleep))


    def open_in_instagram(self, headless, start_maximized):

        chrome_options = Options()

        if headless:
            chrome_options.add_argument('--headless')
        elif start_maximized:
            chrome_options.add_argument('--start-maximized')

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--data-path=/tmp/data-path')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--homedir=/tmp')
        chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

        # for ChromeDriver version 79.0.3945.16 or over
        # don`t show as web_drive
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        if not self.link_by_default == None:
            browser.get(self.link_by_default)
            self.sleep_browser()
        return browser


    def login_in_instagram(self):

        if len(self.browser.find_elements('name', 'username')) > 0:

            try:
                self.browser.delete_all_cookies()
                username_input = self.browser.find_element('name', 'username')
                username_input.clear()
                username_input.send_keys(user_name)
                self.sleep_browser()
                password_input = self.browser.find_element('name', 'password')
                password_input.clear()
                password_input.send_keys(password)
                self.sleep_browser()
                password_input.send_keys(Keys.ENTER)
                self.sleep_browser()
                self.save_cookies_by_user_id(self.browser, user_id)

            except Exception as ex:
                print(ex)

            # try:
            #     turn_on_button = self.browser.find_element(By.XPATH,
            #                                           '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            #     turn_on_button.click()
            # except NoSuchElementException:
            #     print('sorry? but do not found turn_on button`s')


    def set_cookies_by_user_id(self, user_id: str = None) -> bool:
        result = False
        try:
            self.browser.delete_all_cookies()
            for cookie in json.load(open(f"{user_id}_cookies", "r")):
                self.browser.add_cookie(cookie)
            result = True
        except:
            self.browser.refresh()
            result = False
        finally:
            print(f'set cookies is {result}')
            return result


    def save_cookies_by_user_id(self, user_id: str = None) -> bool:
        result = False
        try:
            json.dump(self.browser.get_cookies(), open(f"{user_id}_cookies", "w"))
            result = True
        except:
            result = False
        finally:
            print(f'save cookies is {result}')
            return result


if __name__ == '__main__':
    user_id = '66665'
    hashtag = 'vinnytsia'

    instagram = InstagramBot(user_name, password)

    print(instagram.__dict__)
    instagram.login_in_instagram()
    instagram.sleep_browser(8)
    instagram.close_browser()



