import pytest
from pageobject.baidupage import BaiduPage
from common.logger import Log
import sys


@pytest.fixture(scope='session')
def start_baidu(project_session_start):
    logger = Log()

    global driver
    logger.info('百度输入测试开始......{0}'.format(sys._getframe().f_code.co_name))
    driver = project_session_start
    driver.get('http://www.baidu.com')
    lg = BaiduPage(driver)
    yield lg
    logger.info('百度输入测试结束......{0}'.format(sys._getframe().f_code.co_name))



