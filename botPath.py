import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, ElementClickInterceptedException

class InstaFollower():
    def __init__(self, path, password, email, account):
        self.service = Service(path)
        self.driver = webdriver.Chrome(service=self.service)
        self.email = email
        self.password = password
        self.account = account

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        mail_btn = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
        mail_btn.send_keys(self.email)

        pass_btn = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_btn.send_keys(self.password)
        pass_btn.send_keys(Keys.ENTER)
        time.sleep(5)
        account_found = self.driver.find_element("xpath",
                                                 '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        account_found.send_keys(self.account)
        time.sleep(2)

        account_btn = self.driver.find_element("xpath",
                                               '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')
        account_btn.click()
        time.sleep(5)
        self.driver.get('https://www.instagram.com/chefsteps/followers/')
        time.sleep(10)

    def find_followers(self):
        time.sleep(4)
        self.follow()
        # f_body = self.driver.find_element("xpath", "//div[@class='_aano']")
        # while True:
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)
        #     time.sleep(4)

    def follow(self):
        buttons = self.driver.find_elements("css selector", 'button')
        for bttn in buttons:
            try:
                bttn.click()
                time.sleep(2)
            except:
                bttn.click()