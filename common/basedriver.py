from selenium import webdriver


class BaseDriver():
    def createRemoteChromDriver(self):
        chrome_capabilities = {
            "browserName": "chrome",
            "version": "80.0.3987.106",  # 注意版本号一定要写对
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True,
        }
        driver = webdriver.Remote('http://192.168.174.128:5555/wd/hub', desired_capabilities=chrome_capabilities)
        return driver

    def createRemoteFFDriver(self):
        chrome_capabilities = {
            "browserName": "firefox",
            "version": "73.0",  # 注意版本号一定要写对
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True,
        }
        driver = webdriver.Remote('http://192.168.174.128:5555/wd/hub', desired_capabilities=chrome_capabilities)
        return driver

