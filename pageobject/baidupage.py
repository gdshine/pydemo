from driver.remoteDriver import RemoteDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaiduPage(RemoteDriver):

    logout_loc = (By.XPATH, '//a[text()="退出"]')

    def ispresent(self):
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(BaiduPage.logout_loc))
            return True
        except:
            return False


