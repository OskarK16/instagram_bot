print("Hello world!")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from botPath import InstaFollower

CHROME_DRIVER_PATH = "C:\\Users\\Admin\\Desktop\\chromedriver.exe"
SERVICE = Service(CHROME_DRIVER_PATH)
EMAIL = "thuners27@gmail.com"
PASSWORD = "kurnikowa"
SIMILAR_ACCOUNT = "chefsteps"

bot = InstaFollower(CHROME_DRIVER_PATH, PASSWORD, EMAIL, SIMILAR_ACCOUNT)
bot.login()
# bot.find_followers()
bot.follow()