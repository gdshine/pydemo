import pytest
import os
import sys
from selenium import webdriver
from common.logger import Log
from common.getConfig import r_config


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'myconfig.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log()

driver = None


@pytest.fixture(scope='session')
def project_session_start():
    logger.info("==========开始 XX项目 执行测试===========")
    global driver
    driver = webdriver.Chrome(BASE_DIR+"\\chromedriver.exe")
    driver.maximize_window()
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