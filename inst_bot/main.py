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
from browser_options import CHROME_OPTIONS, CHROME_OPTIONS_HEAD

from cr_graphy.crypt_password import generate_key, encrypt, decrypt, encrypt_in, decrypt_in


class ChromeBrowser():
    """Chrome browser"""
    __type = "ChromeBrowser"
    __max_time_sleep = 0
    __min_time_sleep = 0
    __hand_time_sleep = 0

    __start_headless = False
    __start_maximized = True

    __chrome_options = Options()

    def __init__(self):

        self.browser = None
        self.link_by_default = 'https://www.google.com/'
        self.cookies_file_name = 'chrome'
        self.json_file_name = 'chrome'
    def __del__(self):
        if self.browser:
            # self.save_cookies_by_user_id(cookies_file_name=self.cookies_file_name)
            self.browser.close()

    def __str__(self):
        return f"Chrome browser: {self.link_by_default}  headless = {self.__start_headless}  maximized = {self.__start_maximized} Timing: max = {self.__max_time_sleep}  min = {self.__min_time_sleep}  hand = {self.__hand_time_sleep}"

    @staticmethod
    def print_type():
        print(ChromeBrowser.__type)

    @classmethod
    def __check_value_by_int(cls, value):
        if isinstance(value, int):
            return True
        else:
            raise ValueError

    def set_times_sleep(self, hand_time_sleep: int = 0, min_time_sleep: int = 0, max_time_sleep: int = 0):
        if self.__check_value_by_int(hand_time_sleep) and hand_time_sleep > 0:
            self.__hand_time_sleep = hand_time_sleep
            self.__min_time_sleep = 0
            self.__max_time_sleep = 0

        if self.__check_value_by_int(hand_time_sleep) \
                and hand_time_sleep == 0 \
                and self.__check_value_by_int(min_time_sleep) \
                and self.__check_value_by_int(max_time_sleep) \
                and max_time_sleep >= min_time_sleep:
            self.__hand_time_sleep = 0
            self.__min_time_sleep = min_time_sleep
            self.__max_time_sleep = max_time_sleep

    @property
    def chrome_options(self):
        chrome_options = []
        for i in self.__chrome_options.arguments:
            chrome_options.append(i)
        return chrome_options

    @chrome_options.setter
    def chrome_options(self, start_headless: bool = False, start_maximized: bool = True) -> object:

        self.__start_headless = start_headless
        self.__start_maximized = start_maximized

        for option_head in CHROME_OPTIONS_HEAD:
            if self.__start_headless and option_head == '--headless':
                self.__chrome_options.add_argument(option_head)
            elif self.__start_maximized and option_head == '--start-maximized':
                self.__chrome_options.add_argument(option_head)

        for option in CHROME_OPTIONS:
            self.__chrome_options.add_argument(option)

    @chrome_options.deleter
    def chrome_options(self):
        self.__chrome_options.arguments.clear()

    def start_chrome_browser(self) -> object:
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__chrome_options)
        return browser


if __name__ == '__main__':
    br = ChromeBrowser()
    br.chrome_options = False, False
    br.set_times_sleep(min_time_sleep=2, max_time_sleep=5)
    for i in br.chrome_options:
        print(i)
    br.start_chrome_browser()
    print(br)
