

class Const:
    Linux_Drive = "https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip"

    Mac_Driver = "https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_mac64.zip"

    Windows_Driver = "https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip"

    driver_urls = {
        "Windows": Windows_Driver,
        "Darwin": Mac_Driver,
        "Linux": Linux_Drive
    }

    driver_path = {
        "Windows": "./chromedriver.exe",
        "Darwin": "./chromedriver",
        "Linux": "./chromedriver"
    }