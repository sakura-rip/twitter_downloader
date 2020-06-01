from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import sys
from selenium.webdriver.chrome.options import Options
from action import Action
import requests
import json
import os
import time


class TwitterGetter(Action):
    """
    Unofficial Twitter tool
    for get download image
    """
    def __init__(self, user_id, path):
        self.user_id = user_id
        self.twitter_url = f"https://twitter.com/{user_id}"
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--log-level=3')
        print("starting")
        self.driver = Chrome(options=options, executable_path=path)
        # ユーザーが存在するか確認
        self.is_user_id()
        # 非公開ユーザーかどうか確認
        self.is_user_protected()

        Action.__init__(self)

    def is_user_id(self):
        print("Check if the account exists")
        self.driver.get(self.twitter_url)
        time.sleep(3)
        if f"(@{self.user_id.lower()}) / twitter" not in self.driver.title.lower():
            sys.exit("no such as user in twitter")
        print("done")

    def is_user_protected(self):
        pro = self.driver.find_elements_by_tag_name("svg")
        for x in pro:
            try:
                if x.get_attribute('aria-label') == "非公開アカウント":
                    sys.exit("this user is protected")
            except:
                pass
        print("target user is not protected")

if __name__ == "__main__":
    path = "C:/Program Files/chromedriver/chromedriver.exe"
    twitter = TwitterGetter(input("please input target user id :"), path)
    twitter.download_all_image()
