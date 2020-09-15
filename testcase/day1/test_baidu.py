import sys,pytest
sys.path.append('../')
from driver.remoteDriver import RemoteDriver
from pageobject.baidupage import BaiduPage
from common.logger import Log


class TestBaidu():

    # @pytest.mark.run(order=2)
    def test_one(self,getBrowser):
        Log().info("test one start......")
        remotedriver = RemoteDriver(getBrowser['url'],eval(getBrowser['browser']))
        driver = remotedriver.driver
        try:
            driver.get('http://www.baidu.com')
            driver.find_element_by_id('kw').send_keys('selenium')
            driver.find_element_by_id('su').click()
            driver.maximize_window()
            driver.get_screenshot_as_file(r'd:/baidu1.png')
            Log().info(f"test one {driver.title}")

            assert driver.title == '百度一下，你就知道'
        finally:
            driver.quit()
            print("test ending......")

    @pytest.mark.run(order=1)
    def test_two(self,getBrowser):

        remotedriver = RemoteDriver(getBrowser['url'],eval(getBrowser['browser']))
        driver = remotedriver.driver
        try:
            driver.get('http://www.baidu.com')
            driver.find_element_by_id('kw').send_keys('robot')
            driver.find_element_by_id('su').click()
            driver.maximize_window()
            driver.get_screenshot_as_file(r'd:/baidu2.png')
            assert driver.title == '百度一下，你就知道'
        except Exception:
            driver.get_screenshot_as_file(r'd:/err.png')
            raise
        finally:
            driver.quit()
            print("test ending......")

    # @pytest.mark.run(order=3)
    def test_third(self,getBrowser):

        remotedriver = RemoteDriver(getBrowser['url'],eval(getBrowser['browser']))
        driver = remotedriver.driver
        try:
            driver.get('http://www.baidu.com')
            driver.find_element_by_id('kw').send_keys('requests')
            driver.find_element_by_id('su').click()
            driver.maximize_window()
            driver.get_screenshot_as_file(r'd:/baidu3.png')
        finally:
            driver.quit()

            print("test ending......")


    # @pytest.mark.parametrize("login", conftest.test_login, indirect=True)
    # @pytest.mark.run(order=4)
    def test_01(self,login):
        print("测试用例1：%s" % login)

    def test_02(self,getBrowser):

        remotedriver = RemoteDriver(getBrowser['url'],eval(getBrowser['browser']))
        # driver = remotedriver.driver
        try:
            remotedriver.get('http://www.baidu.com')
            remotedriver.find_element('id', 'kw').send_keys('test')
            remotedriver.find_element('id', 'su').click()
            remotedriver.maximize_window()
            remotedriver.set_page_load_timeout(1)
            remotedriver.get_screenshot_as_file('d:/test.png')
        finally:
            remotedriver.close()
            print("test ending......")

    def test_03(self,getBrowser):

        # remotedriver = RemoteDriver(getBrowser['url'],eval(getBrowser['browser']))
        # driver = remotedriver.driver
        baidu = BaiduPage(getBrowser['url'],eval(getBrowser['browser']))
        try:
            baidu.get('http://www.baidu.com')
            baidu.find_element('id', 'kw').send_keys('test')
            baidu.find_element('id', 'su').click()
            baidu.maximize_window()
            baidu.set_page_load_timeout(1)
            baidu.get_screenshot_as_file('d:/test.png')
        finally:
            baidu.close()
            Log().info("test ending......")
            print("test ending......")