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
            # self.save_cookies_by_user_id(cookies_file_name=self.cookies_file_name)
            self.__browser.close()

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

    @cookies_file_name.setter
    def json_file_name(self, file_name: str):
        self.__json_file_name = self.__verifity_file_name(file_name)

    @cookies_file_name.deleter
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

    def start_chrome_browser(self) -> object:
        self.__browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__chrome_options)

    def sleep(self):
        if self.__hand_time_sleep > 0:
            time.sleep(self.hand_time_sleep)
        else:
            time.sleep(random.randrange(self.__min_time_sleep, self.__max_time_sleep))

if __name__ == '__main__':
    br = ChromeBrowser()
    br.chrome_options = CHROME_OPTIONS
    br.set_times_sleep(hand_time_sleep=0, min_time_sleep=3, max_time_sleep=7)
    for i in br.chrome_options:
        print(i)
    br.cookies_file_name = 'chrome.cookies'
    print(br.cookies_file_name)
    br.start_chrome_browser()
    br.sleep()
    print(br)
    print(br.get_times_sleep())
