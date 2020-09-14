import sys
sys.path.append('../')
from common.basedriver import BaseDriver


class TestBZhiHu(BaseDriver):

    def test_zhihu(self):

        remotedriver = BaseDriver()
        driver = remotedriver.createRemoteFFDriver()
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
