import webbrowser

from ddddocr import DdddOcr
from selenium import webdriver

# driver = webdriver.Edge()  # "./chromedriver_win32/chromedriver.exe"


class OpenWeb:
    # def __init__(self):
    #     self.driver = webdriver.Edge()  # "./chromedriver_win32/chromedriver.exe"

    def open_cloud_web(self):

        driver = webdriver.Edge()  # "./chromedriver_win32/chromedriver.exe"
        # 1. 打开浏览器访问网页
        driver.get(url="http://www.0531yun.com/")

        driver.maximize_window()
        # 2. 输入账号和密码
        acc = driver.find_element(value="acc")
        acc.send_keys("h211222yqhz")
        driver.find_element(value="pwd").send_keys("A123456@")

        # 3. 输入验证码，识别并添加
        code = driver.find_element(value="imgValidCode")
        code_png = code.screenshot("code.png")
        ocr = DdddOcr(old=True)
        with open(file="code.png", mode="rb") as f:
            image = f.read()
        res = ocr.classification(image)
        driver.find_element(value="code").send_keys(res)
        #  4. 点击登陆按钮
        driver.find_element(value="login_btn").click()
      # webbrowser.open('https://www.0531yun.com/index.html')
        print("The end")