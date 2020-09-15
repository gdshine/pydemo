import pytest
from common import getConfig
from random import choice
from common.logger import Log
from time import sleep
from pageobject.baidupage import BaiduPage


@pytest.fixture()
def login():
    username = "gaohui"
    passwd = "123456"
    return "登录名：{0}，密码：{1}".format(username, passwd)


@pytest.fixture()
def getBrowser():
    url = getConfig.r_config(getConfig.conf_dir, 'remoteurl', 'url')
    browser = getConfig.getkeys(getConfig.conf_dir, 'browser')
    br = getConfig.r_config(getConfig.conf_dir, 'browser',choice(browser))
    print(br)
    return {'url':url,'browser':br}


# @pytest.fixture(scope='class')
# def start_module(project_module_start):
#     '''
#     每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
#     :param project_module_start:  每个模块单独打开一次浏览器
#     :return: driver lg
#     '''
#     Log().info("==========开始执行测试用例集===========")
#     global driver
#     driver = project_module_start
#     driver.get("http://www.baidu.com")
#
#     yield driver
#     Log().info("==========结束执行测试用例集===========")
#     driver.quit()


@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver lg
    '''
    Log().info("==========开始执行测试用例集===========")
    global driver
    driver = project_session_start
    Log().info("----------------------------------------------------------------------------------" + str(driver))
    driver.get("http://qa.jdh.com.cn/jdh")
    # lg = BaiduPage(driver)
    yield driver
    Log().info("==========结束执行测试用例集===========")


@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    sleep(3)