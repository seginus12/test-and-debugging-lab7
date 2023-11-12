from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()


class SeleniumTests:
    def __init__(self, username, password, browser):
        if browser == "Chromium":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Wrong browser")
        self.username = username
        self.password = password
        self.url = "https://vk.com/"

        self.driver.get(url=self.url)

    def login(self):
        phone_field = self.driver.find_element(by=By.ID, value="index_email")
        phone_field.send_keys(self.username)
        login_button = self.driver.find_element(by=By.CLASS_NAME, value="VkIdForm__signInButton")
        login_button.click()
        sleep(1)
        # If not password auth method
        '''
        other_method = self.driver.find_element(by=By.XPATH, value="//button[@data-test-id='other-verification-methods']")
        other_method.click()
        sleep(1)
        password_method = self.driver.find_element(by=By.XPATH, value="//div[@data-test-id='verificationMethod_password']")
        password_method.click()
        sleep(1)
        '''
        password_field = self.driver.find_element(by=By.NAME, value="password")
        password_field.send_keys(self.password)
        sleep(1)
        password_field = self.driver.find_element(by=By.CLASS_NAME, value="vkuiButton--lvl-primary")
        password_field.click()

    def search(self):
        self.login()
        sleep(2)
        music_button = self.driver.find_element(by=By.XPATH, value="//a[@href='/audios664606037']")
        music_button.click()
        sleep(2)
        music_search_field = self.driver.find_element(by=By.ID, value="audio_search")
        music_search_field.send_keys("трава у дома")
        sleep(2)
        music_search_button = self.driver.find_element(by=By.CLASS_NAME, value="ui_search_button_search")
        music_search_button.click()

    def create_post(self):
        self.login()
        sleep(5)
        profile_button = self.driver.find_element(by=By.XPATH, value="//a[@href='/dusolcev' and @class='LeftMenuItem-module__item--XMcN9']")
        profile_button.click()
        sleep(5)
        post_field = self.driver.find_element(by=By.ID, value="post_field")
        post_field.send_keys("Привет Андрей")
        sleep(1)
        send_post_button = self.driver.find_element(by=By.ID, value="send_post")
        send_post_button.click()

    def rate_post(self):
        self.login()
        sleep(5)
        profile_button = self.driver.find_element(by=By.XPATH, value="//a[@href='/dusolcev' and @class='LeftMenuItem-module__item--XMcN9']")
        profile_button.click()
        sleep(2)
        profile_button = self.driver.find_element(by=By.CLASS_NAME, value="PostButtonReactions--icon-active")
        profile_button.click()


test = SeleniumTests(username=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'), browser="Firefox")
test.login()

