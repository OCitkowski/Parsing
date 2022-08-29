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

from cr_graphy.crypt_password import generate_key, encrypt, decrypt, encrypt_in, decrypt_in


class ChromeBrowser():
    """Chrome __browser"""
    __type = "ChromeBrowser"
    link_by_default = 'https://www.google.com/'
    cookies_file_name = 'chrome'
    json_file_name = 'chrome'
    time_sleep = 7
    min_time_sleep = 5
    hand_time_sleep = 0

    def __init__(self, headless: bool = False, start_maximized: bool = True):

        self.headless = headless
        self.start_maximized = start_maximized
        self.browser = None

    def __del__(self):
        if self.browser:
            self.save_cookies_by_user_id(cookies_file_name=self.cookies_file_name)
            self.browser.close()

    def __str__(self):
        return f"Chrome __browser: {self.link_by_default}  Timing: sleep = {self.time_sleep}  min = {self.min_time_sleep}  hand = {self.hand_time_sleep}"

    @staticmethod
    def print_type():
        print(ChromeBrowser.__type)

    def close(self):

        self.save_cookies_by_user_id(cookies_file_name=self.cookies_file_name)
        self.browser.close()
        self.browser.quit()

    def sleep(self):

        if self.hand_time_sleep > 0:
            time.sleep(self.hand_time_sleep)
        elif self.min_time_sleep == 0:
            time.sleep(self.time_sleep)
        else:
            time.sleep(random.randrange(self.min_time_sleep, self.time_sleep))

    def open(self, headless: object, start_maximized: object) -> object:

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

        # if not self.link_by_default == None:
        #     __browser.get(self.link_by_default)
        #     self.sleep()
        return browser

    def set_cookies_by_user_id(self, cookies_file_name: str = None) -> bool:
        result = False
        try:
            self.browser.delete_all_cookies()
            for cookie in json.load(open(f"{cookies_file_name}.cookies", "r")):
                self.browser.add_cookie(cookie)
            result = True
        except:
            self.browser.refresh()
            result = False
        finally:
            print(f'set cookies is {result}')
            return result

    def save_cookies_by_user_id(self, cookies_file_name: str = None) -> bool:
        result = False
        try:
            json.dump(self.browser.get_cookies(), open(f"{cookies_file_name}.cookies", "w"))
            result = True
        except:
            result = False
        finally:
            print(f'save cookies is {result} in cookies_file_name')
            return result

    def xpath_exists(self, xpath):
        try:
            self.browser.find_element(By.XPATH, xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

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


class InstagramBot(ChromeBrowser):
    """Instagram Bot"""

    def __init__(self, username, password, ):

        super(InstagramBot, self).__init__()
        self.username = username
        self.password = password

        self.link_by_default = 'https://www.instagram.com/'
        self.cookies_file_name = self.username + '_cookies'
        self.json_file_name = self.username + '_data'

        self.is_cookies = self.set_cookies_by_user_id(self.cookies_file_name)
        self.open_in_instagram()

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

    def get_post_links_by_hashtag(self, hashtag, quantity_links: int = 40, time_sleep: int = 3):
        posts_urls = []
        try:
            self.browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            self.sleep()
            actions = ActionChains(self.browser)
            while len(posts_urls) < quantity_links:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                actions.send_keys(Keys.PAGE_DOWN).perform()
                self.sleep()
                hrefs = self.browser.find_elements(By.TAG_NAME, "a")
                posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
        except Exception as ex:
            print(f' (sorry? but do not found link`s ) /  {ex} ')
            return []
        finally:
            return posts_urls

    def get_collecting_data_from_posts_by_links(self, posts_urls: list):
        result = {}

        for url_post in posts_urls:
            post_list = {}
            try:
                self.browser.get(url_post)
                self.sleep()
                path_like = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div/span'

                if self.xpath_exists(path_like):
                    like = self.browser.find_element(By.XPATH, path_like)
                    post_list['like'] = like.text
                # TODO else video....

                self.sleep()
                hrefs = self.browser.find_elements(By.TAG_NAME, "a")
                hashtags = []
                for href in hrefs:
                    if len(href.text) and href.text[0] == '#' and href.text[1] != r'\\':
                        hashtags.append(href.text)
                time_post = self.browser.find_element(By.TAG_NAME, "time").get_attribute('datetime')
                self.sleep()

                post_list['hrefs'] = hashtags
                post_list['time_post'] = time_post
                result[url_post] = post_list
                print('OK - ' + url_post)

            except NoSuchElementException as ex:
                print('failed to process - ' + url_post)
                print(ex)
            finally:
                pass
        return result

    def like_the_posts_in_instagram(self, posts_urls, Unlike: bool = False):

        for post_url in posts_urls:
            try:
                self.browser.get(post_url)
                self.sleep()
                like_button = self.browser.find_element(By.XPATH,
                                                        '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
                if like_button.accessible_name == 'Like' and not Unlike:
                    like_button.click()
                    self.browser.refresh()
                    print(f'like for {post_url}')
                elif like_button.accessible_name != 'Like' and Unlike:
                    like_button.click()
                    self.browser.refresh()
                    print(f'Unlike for {post_url}')
                self.sleep()

            except NoSuchElementException as ex:
                print(ex)

    def follow_the_posts_in_instagram(self, posts_urls, UnFollow: bool = False):
        for post_url in posts_urls:
            try:
                self.browser.get(post_url)
                self.sleep()
                follow_button = self.browser.find_element(By.XPATH,
                                                          '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
                if follow_button.text != 'Following' and not UnFollow:
                    follow_button.click()
                    self.browser.refresh()
                    print(f'follow for {post_url}')
                elif follow_button.text == 'Following' and UnFollow:
                    follow_button.click()
                    unfollow_button = self.browser.find_element(By.XPATH, '//*[contains(text(), "Unfollow")]')
                    unfollow_button.click()
                    self.browser.refresh()
                    print(f'Unfollow for {post_url}')
                self.sleep()
            except NoSuchElementException as ex:
                print(ex)

    def search_best_post_by_like_in_file(self, number_of_best_posts: int = 3):
        best_posts = []
        data = self.get_data_from_json_file()
        for item in data:
            if 'like' in data[item].keys():
                # print(f'{data[item]["like"]} / {type(data[item]["like"] )}')
                if len(best_posts) >= number_of_best_posts:
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


def encrypt_in_file(full_file_name):
    password = input('Enter your password -')
    result = False

    if not os.path.isfile("salt.salt"):
        key = generate_key(password, salt_size=16, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)

    encrypt_in(full_file_name, key)

    return result


def decrypt_in_file(full_file_name):
    password = input('Enter your password -')
    result = False

    if not os.path.isfile("salt.salt"):
        print('Don`t have salt!!!')
    else:
        key = generate_key(password, load_existing_salt=True)

    decrypt_in(full_file_name, key)

    return result

if __name__ == '__main__':

    # full_file_name = 'xxx.py'
    # encrypt_in_file(full_file_name)
    # decrypt_in_file(full_file_name)
    # InstagramBot(username=user_name, password=password).print_type()
    # insta = InstagramBot(username=user_name, password=password)
    # print(dir(insta))
    # insta.close()
    # insta.headless = True
    # insta.__browser = insta.open()

    # insta.__str__()
    # # for item in  insta.__dict__:
    # #     print(item)
    # insta.sleep()
    # insta.login_in_instagram()
    # insta.sleep()
    # post_links = insta.get_post_links_by_hashtag('funnycats', 50)
    # insta.json_file_name = "funnycats"
    # insta.save_data_in_json_file(post_links)
    # data = insta.get_data_from_json_file()
    # data_from_posts = insta.get_collecting_data_from_posts_by_links(data)
    # insta.json_file_name = "data_funnycats"
    # # insta.save_data_in_json_file(data_from_posts)
    # # insta.follow_the_posts_in_instagram(data, UnFollow=True)
    # insta.search_best_post_by_like_in_file(5)
    crbr = ChromeBrowser()
    # for i in dir(crbr):
    print(ChromeBrowser.__dict__)
    print(crbr.__dict__)

    # print(dir(crbr))