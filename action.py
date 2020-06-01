import sys
import time
import re
import shutil
import requests
import os


class Action:
    def __init__(self):
        pass

    def download_all_image(self):
        # 保存先ディレクトリを確認
        self.cehck_directory()
        #最後までスクロールしながら保存
        self.scroll_to_last()

    def save(self, url):
        try:
            te = "/"
            file_name = f"./{self.user_id}/{url.split(te)[4].split('?')[0]}.jpg"
            r = requests.get(url, stream=True)
            with open(file_name, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            print(f"save image to {file_name}")
        except Exception as e:
            print(e)

    def save_files(self, urls):
        for url in urls:
            try:
                self.save(url)
            except Exception as e:
                print(e)

    def scroll_to_last(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.save_files(self.get_all_url(self.driver.page_source))
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        try:
            os.remove("./debug.log")
        except FileNotFoundError:
            pass
        print("Finish downloading image")

    def get_all_url(self, page_source, type_="image"):
        try:
            if type_ == "image":
                imgs = re.findall(r"https://pbs.twimg.com/media/.{15}\?format=jpg&amp;name=[0-9a-zx]*", str(page_source))
                urls = {
                    re.sub(r"&amp;name=.*", r"&name=large", url) for url in imgs
                }
            return urls
        except Exception:
            return []

    def cehck_directory(self):
        if not os.path.isdir(f"./{self.user_id}/"):
            print(f"creating dir ./{self.user_id}/")
            os.mkdir(f"./{self.user_id}/")
