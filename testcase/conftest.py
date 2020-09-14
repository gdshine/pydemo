import pytest
from common import getConfig
from random import choice
test_login = [{
    "username": "18712345678",
    "passwd": "111111"
}]


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