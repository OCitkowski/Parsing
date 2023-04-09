# Scrapy settings for dict_com project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "dict_com"

SPIDER_MODULES = ["dict_com.spiders"]
NEWSPIDER_MODULE = "dict_com.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "dict_com (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "dict_com.middlewares.DictComSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "dict_com.middlewares.DictComDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "dict_com.pipelines.DictComPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# I added
# FEED_FORMAT = "csv"
# FEED_URI = "data.csv"
LOG_FILE = "scrapy.log"
LOG_LEVEL = "DEBUG"
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

ITEM_PIPELINES = {
    'dict_com.pipelines.JsonWriterPipeline': 800,  # look to pipelines.py
}

# В даному коді вказується, що Scrapy повинен використовувати браузерний агент, який схожий на Google Chrome, і не
# враховувати robots.txt. Також включено обробку кукісів, що дозволить зберігати дані авторизації.
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True
DOWNLOAD_DELAY = 5

DOWNLOADER_MIDDLEWARES = {
    'dict_com.middlewares.ProxyMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 544,
}

HTTP_PROXY_ENABLED = False
HTTP_PROXY_LIST = [
    # 'http://proxy1.example.com:8080',
    # '8.219.176.202:8080',
    # '46.101.239.193:80',
    # '64.225.8.191:9987',
    # '8.219.97.248:80',
    # '217.76.50.200:8000',
    # '103.152.9.131:80',
    # '182.16.12.30:8088',
    # '45.62.167.249:80',
    # '20.191.183.149:3129',
    # '210.148.141.4:8080',
    # '40.119.236.22:80',
    # '178.33.3.163:8080',
    # '64.225.4.63:9998',
    # '146.59.192.125:3128',
    # '190.109.205.253:999',
    # '110.164.208.125:8888',
    # '194.67.91.153:80',
    # '117.54.114.99:80',
    # '182.93.85.225:8080',
    # '89.43.10.141:80',
    # '117.54.114.96:80',
    # '20.210.113.32:80',
    # '35.246.142.152:80',
    # '170.80.202.252:999',
    # '138.197.102.119:80',
    # '156.17.193.1:80',
    # '95.183.140.89:80',
    # '97.74.92.60:80',
    # '102.223.20.217:80',
    # '51.68.124.241:80',
    # '51.75.141.46:80',
    # '82.79.213.118:9812',
    # '47.74.71.208:2080',
    # '167.71.191.74:80',
    # '61.29.96.146:8000',
    # '51.68.181.108:80',
    # '78.28.152.111:80',
    # '34.100.152.46:80',
    # '210.148.141.1:8080',

    '54.39.183.55:3128',
    '54.39.187.70:3128',
    '54.39.187.70:3128',
    '158.101.113.18:80',
    '54.39.183.55:3128',
    '64.225.8.132:9983',
    '165.227.81.188:9995',
    '46.41.141.111:8080',
    '5.189.184.6:80',
    '177.66.192.221:80',
    '23.236.70.37:45787',
    '46.101.126.180:42911',
    '103.225.87.5:45787',
    '8.219.176.202:8080',
    '43.250.172.225:45787',
    '13.71.80.61:80',
    '43.249.11.151:45787',
    '23.236.65.241:45787',
    '121.54.190.25:45787',
    '167.172.96.117:45711',
    '158.69.53.132:5566',
    '34.219.156.153:80',
    '167.172.172.234:33607',
    '157.230.241.133:35621',
    '43.250.172.211:45787',
    '8.218.247.144:80',
    '34.133.61.49:8118',
    '68.183.230.116:37961',
    '45.251.138.171:45787',
    '103.42.183.106:45787',
]
