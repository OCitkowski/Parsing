# Під хром в убунту не працює
import time, random, os, json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


PROXY = '195.137.167.109:80'
# PROXY = '185.123.101.203:1347'

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={PROXY}')

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# browser.get("https://www.google.com")
browser.get("https://www.whatismyip.com/my-ip-information/")

time.sleep(random.randrange(20, 24))

