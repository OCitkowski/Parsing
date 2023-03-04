import os, time, random, json

from dotenv import load_dotenv

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
from browser_options import CHROME_OPTIONS

load_dotenv()
password = os.getenv("PASSWORD")
user_name = os.getenv("USER_NAME")


class ChromeBrowser():
    """Chrome __browser"""
    __type = "ChromeBrowser"

    def __init__(self):
        self.__browser = None
        self.__chrome_options = Options()
        self._cookies_file_name = 'chrome'
        self._json_file_name = 'chrome'
        self.__max_time_sleep = 0
        self.__min_time_sleep = 0
        self.__hand_time_sleep = 0

    def __del__(self):
        if self.__browser:
            self.__close()

    def __str__(self):
        return f"Chrome __browser: {self.__browser} Timing: max = {self.__max_time_sleep}  min = {self.__min_time_sleep}  hand = {self.__hand_time_sleep}"

    @staticmethod
    def __verifity_time_sleep(time_sleep: int):
        if isinstance(time_sleep, int):
            return time_sleep
        else:
            raise TypeError

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
        return {'hand_time': self.__hand_time_sleep, 'min': self.__min_time_sleep, 'max': self.__max_time_sleep}

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
        return self._cookies_file_name

    @cookies_file_name.setter
    def cookies_file_name(self, file_name: str):
        self._cookies_file_name = self.__verifity_file_name(file_name)

    @cookies_file_name.deleter
    def cookies_file_name(self):
        self._cookies_file_name = ''

    @property
    def json_file_name(self):
        return self._json_file_name

    @json_file_name.setter
    def json_file_name(self, file_name: str):
        self._json_file_name = self.__verifity_file_name(file_name)

    @json_file_name.deleter
    def json_file_name(self):
        self._json_file_name = ''

    @property
    def chrome_options(self):
        chrome_options = []
        for i in self.__chrome_options.arguments:
            chrome_options.append(i)
        return chrome_options

    @chrome_options.setter
    def chrome_options(self, options):

        self.__chrome_options.add_argument("--disable-extensions")
        for option in options:
            self.__chrome_options.add_argument(option)

        self.__browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                          options=self.__chrome_options)

    @chrome_options.deleter
    def chrome_options(self):
        self.__chrome_options.arguments.clear()

    def set_cookies(self) -> bool:
        result = False
        try:
            self.__browser.delete_all_cookies()
            cookies = json.load(open(f"{self._cookies_file_name}.cookies", "r"))
            for cookie in cookies:
                try:
                    self.__browser.add_cookie(cookie)
                    result = True
                    print(cookie)
                except Exception as ex:
                    print(ex)
        except:
            self.__browser.refresh()
            result = False
        finally:
            print(f'set cookies is {result}')
            return result

    def save_cookies(self) -> bool:
        result = False
        try:

            with open(self._cookies_file_name + '.cookies', 'w') as write_file:
                json.dump(self.__browser.get_cookies(), write_file, ensure_ascii=False)
                result = True
            print(f'{self._cookies_file_name}.cookies save to root')
        except Exception as ex:
            print(f'{self._cookies_file_name}.cookies don`t save to root : {ex}')
        return result

    def save_data_in_json_file(self, data):
        result = False
        try:
            with open(self._json_file_name + '.json', 'w') as write_file:
                json.dump(data, write_file, ensure_ascii=False)
                result = True
            print(f'{self._json_file_name}.json save to root')
        except:
            print(f'{self._json_file_name}.json don`t save to root')
        return result

    def get_data_from_json_file(self):
        result = False
        try:
            with open(self._json_file_name + '.json', 'r') as read_file:
                result = json.load(read_file)
            print(f'{self._json_file_name}.json get data from json file')
        except:
            print(f'{self._json_file_name}.json don`t get data from json file')
        return result

    def open(self):
        return self.__browser

    def sleep(self):
        if self.__hand_time_sleep > 0:
            time.sleep(self.__hand_time_sleep)
        else:
            time.sleep(random.randrange(self.__min_time_sleep, self.__max_time_sleep))

    def xpath_exists(self, xpath):
        try:
            self.__browser.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def __close(self):
        if self._cookies_file_name:
            self.save_cookies()
        self.__browser.close()


class InstagramBot(ChromeBrowser):
    """Instagram Bot"""
    __type = "Instagram"

    def __init__(self, username, password, ):
        super().__init__()
        self.username = username
        self.password = password
        self.__link_by_default = 'https://www.instagram.com/'

    def open_in_instagram(self):
        self.__browser = self.open()
        if not self.__link_by_default == None:
            self.__browser.get(self.__link_by_default)
            self.set_cookies()
            self.__browser.refresh()
            self.sleep()

    def __turn_on_button(self):
        try:
            # turn_on_button = self.__browser.find_element(By.XPATH,
            #                                              '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]')
            turn_on_button = self.__browser.find_element(By.XPATH,
                                                         '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[3]/button[1]')

            # turn_on_buttons = self.__browser.find_elements(By.LINK_TEXT, 'Log in')
            turn_on_button.click()
            print('turn of button')
        except NoSuchElementException:
            print('sorry... but do not found LOG_IN button')

    def login_in_instagram(self):

        if len(self.__browser.find_elements('name', 'username')) > 0:

            try:
                self.__browser.delete_all_cookies()
                username_input = self.__browser.find_element('name', 'username')
                username_input.clear()
                username_input.send_keys(user_name)
                self.sleep()
                password_input = self.__browser.find_element('name', 'password')
                password_input.clear()
                password_input.send_keys(password)
                self.sleep()
                password_input.send_keys(Keys.ENTER)
                self.sleep()
                self.save_cookies()
            except Exception as ex:
                print(ex)

        self.__turn_on_button()

    def get_post_links_by_hashtag(self, hashtag: str = None, quantity_links: int = 40, time_sleep: int = 3):
        posts_urls = []

        if hashtag == None:
            return None
        try:
            self.__browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            self.sleep()
            actions = ActionChains(self.__browser)
            while len(posts_urls) < quantity_links:
                self.__browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                actions.send_keys(Keys.PAGE_DOWN).perform()
                self.sleep()
                hrefs = self.__browser.find_elements(By.TAG_NAME, "a")
                posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
        except Exception as ex:
            print(f' (sorry? but do not found link`s ) /  {ex} ')
            return []
        finally:
            return posts_urls

    def get_collecting_data_from_posts_by_links(self, posts_urls: list):
        result = {}
        i = 1
        for url_post in posts_urls:
            post_list = {}
            try:
                self.__browser.get(url_post)
                self.sleep()
                path_like = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div/span'

                if self.xpath_exists(path_like):
                    like = self.__browser.find_element(By.XPATH, path_like)
                    post_list['like'] = like.text
                # TODO else video....

                self.sleep()
                hrefs = self.__browser.find_elements(By.TAG_NAME, "a")
                hashtags = []
                for href in hrefs:
                    if len(href.text) and href.text[0] == '#' and href.text[1] != r'\\':
                        hashtags.append(href.text)
                time_post = self.__browser.find_element(By.TAG_NAME, "time").get_attribute('datetime')
                self.sleep()

                post_list['hrefs'] = hashtags
                post_list['time_post'] = time_post
                result[url_post] = post_list
                print(f'№ - {i}    OK - {url_post}')

            except NoSuchElementException as ex:
                print('failed to process - ' + url_post)
                print(ex)
            finally:
                i += 1
        return result

    def like_the_posts_in_instagram(self, posts_urls, Unlike: bool = False):

        for post_url in posts_urls:
            try:
                self.__browser.get(post_url)
                self.sleep()
                like_button = self.__browser.find_element(By.XPATH,
                                                          '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
                if like_button.accessible_name == 'Like' and not Unlike:
                    like_button.click()
                    self.__browser.refresh()
                    print(f'like for {post_url}')
                elif like_button.accessible_name != 'Like' and Unlike:
                    like_button.click()
                    self.__browser.refresh()
                    print(f'Unlike for {post_url}')
                self.sleep()

            except NoSuchElementException as ex:
                print(ex)

    def follow_the_posts_in_instagram(self, posts_urls, UnFollow: bool = False):
        for post_url in posts_urls:
            try:
                self.__browser.get(post_url)
                self.sleep()
                follow_button = self.__browser.find_element(By.XPATH,
                                                            '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
                if follow_button.text != 'Following' and not UnFollow:
                    follow_button.click()
                    self.__browser.refresh()
                    print(f'follow for {post_url}')
                elif follow_button.text == 'Following' and UnFollow:
                    follow_button.click()
                    unfollow_button = self.__browser.find_element(By.XPATH, '//*[contains(text(), "Unfollow")]')
                    unfollow_button.click()
                    self.__browser.refresh()
                    print(f'Unfollow for {post_url}')
                self.sleep()
            except NoSuchElementException as ex:
                print(ex)

    def get_best_post_by_like_in_file(self, quantity_of_best_posts: int = 3):
        best_posts = []
        data = self.get_data_from_json_file()
        for item in data:
            if 'like' in data[item].keys():
                # print(f'{data[item]["like"]} / {type(data[item]["like"] )}')
                if len(best_posts) >= quantity_of_best_posts:
                    for best_post in best_posts:
                        if float(data[best_post]["like"].replace(",", "")) < float(data[item]["like"].replace(",", "")):
                            # print(f'remove from best_posts {best_post} {data[best_post]["like"]}/ append to best_posts {item} {data[item]["like"]} / {data[best_post]["like"] < data[item]["like"]}')
                            best_posts.remove(best_post)
                            best_posts.append(item)
                            break
                else:
                    best_posts.append(item)
                    # print('add to best_posts ' + item)

        for post in best_posts:
            print(f'{data[post]}')

            # TODO for video


if __name__ == '__main__':
    # try:
    full_file_name = '_x.py'
    # decrypt_in_file(full_file_name)
    insta = InstagramBot(username=user_name, password=password)
    insta.cookies_file_name = user_name + '_insta'
    insta.set_times_sleep(hand_time_sleep=0, min_time_sleep=3, max_time_sleep=7)
    insta.chrome_options = CHROME_OPTIONS
    # print(insta.__dict__)
    # print(f' ***   {insta.chrome_options}')
    insta.open_in_instagram()
    insta.login_in_instagram()

    # insta.json_file_name = user_name + '_insta_by_hashtag'
    # hashtag = 'funny'
    # hashtag_data = insta.get_post_links_by_hashtag(hashtag, 10)
    # insta.save_data_in_json_file(hashtag_data)
    # data = insta.get_data_from_json_file()
    # collecting_data_from_posts = insta.get_collecting_data_from_posts_by_links(data)
    # insta.json_file_name = user_name + '_insta_collecting_data'
    # insta.save_data_in_json_file(collecting_data_from_posts)
    # insta.like_the_posts_in_instagram(hashtag_data, )
    # insta.follow_the_posts_in_instagram(hashtag_data, UnFollow=True)
    # insta.get_best_post_by_like_in_file()
    insta.sleep()

    # print(insta)
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    # encrypt_in_file(full_file_name)
