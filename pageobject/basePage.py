from driver.remoteDriver import RemoteDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from common.logger import Log
from common.getConfig import r_config,conf_dir,getkeys
from selenium import webdriver
from random import choice
import os
logger = Log()


class Page():

    def __init__(self,driver):
        self.driver = driver

    def get_screenshot_as_file(self,name):
        self.driver.get_screenshot_as_file(name)