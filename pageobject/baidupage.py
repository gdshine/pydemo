from driver.remoteDriver import RemoteDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.logger import Log
from pageobject.basePage import Page
from locator.baidu.index import IndexPage
from common.handleby import WebHandlerBy
from testdata.baidu.index import BaiduIndexInput
import sys
logger = Log()


class BaiduPage(Page):

    logout_loc = (By.XPATH, '//a[text()="退出"]')

    def ispresent(self):
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(BaiduPage.logout_loc))
            return True
        except:
            logger.error('退出按钮没有出现{0}'.format(sys._getframe().f_code.co_name))
            return False

    def inputtext(self):
        search_input = self.driver.find_element_by_id(IndexPage.search_input)
        search_input.send_keys(BaiduIndexInput.search_input)

    def clickbutton(self):
        search_input = self.driver.find_element_by_id(IndexPage.search_button)
        search_input.click()

    def inputtext1(self,mes):
        search_input = self.driver.find_element_by_id(IndexPage.search_input)
        search_input.send_keys(mes)