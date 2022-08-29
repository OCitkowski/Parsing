import os
import time, random, json

from inst_bot.auth_data import password, user_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from browser_options import CHROME_OPTIONS

from cr_graphy.crypt_password import generate_key, encrypt, decrypt, encrypt_in, decrypt_in


class ChromeBrowser():
    """Chrome __browser"""
    __type = "ChromeBrowser"
    __max_time_sleep = 0
    __min_time_sleep = 0
    __hand_time_sleep = 0

    __chrome_options = Options()

    def __init__(self):

        self.__browser = None
        self.__cookies_file_name = 'chrome'
        self.__json_file_name = 'chrome'
    def __del__(self):
        if self.__browser:
             self.__close()

    def __str__(self):
        return f"Chrome __browser: {self.__browser} Timing: max = {self.__max_time_sleep}  min = {self.__min_time_sleep}  hand = {self.__hand_time_sleep}"

    @staticmethod
    def __verifity_time_sleep(time_sleep:int):
        if isinstance(time_sleep, int):
            return time_sleep
        else: raise TypeError

    @staticmethod
    def __verifity_file_name(file_name: str):
        if isinstance(file_name, str):
            return file_name
        else:
            raise TypeError

    @staticmethod
    def print_type():
        print(ChromeBrowser.__type)

    def get_times_sleep(self) -> dict:
        return {'hand_time':self.__hand_time_sleep, 'min':self.__min_time_sleep, 'max':self.__max_time_sleep}

    def set_times_sleep(self, hand_time_sleep: int = 0, min_time_sleep: int = 0, max_time_sleep: int = 0):
        if self.__verifity_time_sleep(hand_time_sleep) > 0:
            self.__hand_time_sleep = hand_time_sleep
            self.__min_time_sleep = 0
            self.__max_time_sleep = 0

        if self.__verifity_time_sleep(hand_time_sleep) == 0 \
                and self.__verifity_time_sleep(min_time_sleep) <= self.__verifity_time_sleep(max_time_sleep):
            self.__min_time_sleep = min_time_sleep
            self.__max_time_sleep = max_time_sleep

    @property
    def cookies_file_name(self):
        return self.__cookies_file_name

    @cookies_file_name.setter
    def cookies_file_name(self, file_name:str):
        self.__cookies_file_name = self.__verifity_file_name(file_name)

    @cookies_file_name.deleter
    def cookies_file_name(self):
        self.__cookies_file_name = ''

    @property
    def json_file_name(self):
        return self.__json_file_name

    @json_file_name.setter
    def json_file_name(self, file_name: str):
        self.__json_file_name = self.__verifity_file_name(file_name)

    @json_file_name.deleter
    def json_file_name(self):
        self.__json_file_name = ''

    @property
    def chrome_options(self):
        chrome_options = []
        for i in self.__chrome_options.arguments:
            chrome_options.append(i)
        return chrome_options

    @chrome_options.setter
    def chrome_options(self, CHROME_OPTIONS:list):

        for option in CHROME_OPTIONS:
            self.__chrome_options.add_argument(option)

    @chrome_options.deleter
    def chrome_options(self):
        self.__chrome_options.arguments.clear()

    def set_cookies(self) -> bool:
        result = False
        try:
            self.__browser.delete_all_cookies()
            for cookie in json.load(open(f"{self.__cookies_file_name}.cookies", "r")):
                self.__browser.add_cookie(cookie)
            result = True
        except:
            self.__browser.refresh()
            result = False
        finally:
            print(f'set cookies is {result}')
            return result

    def save_cookies(self) -> bool:
        result = False
        try:
            with open(self.__cookies_file_name + '.cookies', 'w') as write_file:
                json.dump(self.__browser.get_cookies(), write_file, ensure_ascii=False)
                result = True
            print(f'{self.__cookies_file_name}.cookies save to root')
        except Exception as ex:
            print(f'{self.__cookies_file_name}.cookies don`t save to root : {ex}')
        return result

    def save_data_in_json_file(self, data):
        result = False
        try:
            with open(self.json_file_name + '.json', 'w') as write_file:
                json.dump(data, write_file, ensure_ascii=False)
                result = True
            print(f'{self.json_file_name}.json save to root')
        except:
            print(f'{self.json_file_name}.json don`t save to root')
        return result

    def get_data_from_json_file(self):
        result = False
        try:
            with open(self.json_file_name + '.json', 'r') as read_file:
                result = json.load(read_file)
            print(f'{self.json_file_name}.json get data from json file')
        except:
            print(f'{self.json_file_name}.json don`t get data from json file')
        return result


    def open(self) -> object:
        self.__browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__chrome_options)
        self.set_cookies()

    def sleep(self):
        if self.__hand_time_sleep > 0:
            time.sleep(self.__hand_time_sleep)
        else:
            time.sleep(random.randrange(self.__min_time_sleep, self.__max_time_sleep))
    def __close(self):
        self.save_cookies()
        self.__browser.close()

class InstagramBot(ChromeBrowser):
    """Instagram Bot"""
    def __init__(self, username, password, ):
        super(InstagramBot, self).__init__()
        self.username = username
        self.password = password
        self.__link_by_default = 'https://www.instagram.com/'
        self.__cookies_file_name = self.username + '_cookies'
        self.__json_file_name = self.username + '_data'

    def open_in_instagram(self) -> object:

        if not self.link_by_default == None:
            self.browser.get(self.link_by_default)
            self.sleep()

    def login_in_instagram(self):

        if len(self.browser.find_elements('name', 'username')) > 0:

            try:
                self.browser.delete_all_cookies()
                username_input = self.browser.find_element('name', 'username')
                username_input.clear()
                username_input.send_keys(user_name)
                self.sleep()
                password_input = self.browser.find_element('name', 'password')
                password_input.clear()
                password_input.send_keys(password)
                self.sleep()
                password_input.send_keys(Keys.ENTER)
                self.sleep()
                self.save_cookies_by_user_id(self.browser, self.cookies_file_name)

            except Exception as ex:
                print(ex)

            # try:
            #     turn_on_button = self.__browser.find_element(By.XPATH,
            #                                           '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            #     turn_on_button.click()
            # except NoSuchElementException:
            #     print('sorry? but do not found turn_on button`s')


if __name__ == '__main__':
    br = ChromeBrowser()
    br.chrome_options = CHROME_OPTIONS
    br.set_times_sleep(hand_time_sleep=1, min_time_sleep=2, max_time_sleep=5)
    for i in br.chrome_options:
        print(i)
    br.cookies_file_name = 'cookiesxxx'
    br.json_file_name = 'json'

    br.open()
    br.sleep()
    # br.save_cookies()

    print(br.__dict__)





