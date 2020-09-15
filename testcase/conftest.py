import pytest
import os
import sys
from selenium import webdriver
from common.logger import Log
from common.getConfig import r_config
from common.getConfig import getkeys,r_config,conf_dir
from random import choice
from driver.remoteDriver import RemoteDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log()



@pytest.fixture(scope='session')
def project_session_start():
    # logger.info("==========开始 XX项目 执行测试===========")
    # global driver
    # driver = webdriver.Chrome(BASE_DIR+"\\chromedriver.exe")
    # driver.maximize_window()
    # yield driver
    # driver.quit()
    # logger.info("==========结束 XX项目 测试===========")

    global driver
    url = r_config(conf_dir, 'remoteurl', 'url')
    browsers = getkeys(conf_dir, 'browser')
    br = r_config(conf_dir, 'browser', choice(browsers))
    drivertype = r_config(conf_dir, 'drivertype', 'driver_type')
    if drivertype and drivertype == 'remote':
        driver = RemoteDriver(url, eval(br)).driver
    elif drivertype == 'chrome':
        chrome_option = ChromeOptions()
        chrome_option.add_argument('--headless')
        driver_destination = BASE_DIR+"\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_destination,
                                       chrome_options=chrome_option)
        logger.info('Driver is set as for browser "%s".' % (drivertype))
    elif drivertype == 'firefox':
        driver_destination = os.path.join(os.path.dirname(__file__), 'geckodriver')
        driver = webdriver.Firefox(executable_path=driver_destination)
        driver.maximize_window()
        logger.info('Driver is set as for browser "%s".' % (drivertype))
    elif drivertype == 'ie':
        driver = webdriver.Ie()
        logger.info('Driver is set as for browser "%s".' % (drivertype))

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()
    logger.info("==========结束 XX项目 测试===========")


@pytest.fixture(scope='module')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    global driver
    driver = webdriver.Chrome(BASE_DIR+"\\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("==========结束 XX模块 测试===========")


@pytest.fixture()
def project_func():
    print("project_func")



def pytest_configure(config):
    # 标签名集合
    marker_list = ['smoke', 'lucas']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)