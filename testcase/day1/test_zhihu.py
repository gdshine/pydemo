import sys
sys.path.append('../')
from driver.remoteDriver import RemoteDriver


class TestBZhiHu(RemoteDriver):

    def test_zhihu(self,getBrowser):

        remotedriver = RemoteDriver(getBrowser['url'], eval(getBrowser['browser']))
        driver = remotedriver.driver
        try:
            driver.get('http://www.baidu.com')
            driver.find_element_by_id('kw').send_keys('selenium')
            driver.find_element_by_id('su').click()
            driver.maximize_window()
            driver.get_screenshot_as_file(r'd:/baidu4.png')
            print(driver.title)
            assert driver.title == '百度一下，你就知道'
        finally:
            driver.quit()
            print("test ending......")
