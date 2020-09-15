from pageobject.baidupage import BaiduPage
import pytest


@pytest.mark.usefixtures('start_baidu')
class Testbaidu():

    # def test_one(self):
    #     baidupage = BaiduPage()
    #     try:
    #         baidupage.get('http://www.baidu.com')
    #         baidupage.inputtext()
    #         baidupage.clickbutton()
    #     finally:
    #         baidupage.quit()

    @pytest.mark.parametrize('mes',('selenium','request'))
    def test_two(self,mes,start_baidu):
        driver = start_baidu
        try:
            driver.inputtext1(mes)
            driver.clickbutton()
        finally:
            print('end......')
            driver.get_screenshot_as_file('d:/test.png')
