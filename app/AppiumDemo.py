from appium import webdriver
from app.GetConf import GetConf
from app.ClickThread import ClickThread


class AppiumDemo(object):

    def __init__(self, wait_second=10):
        gc = GetConf()
        self.conf = gc.get_info()
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.conf)
        self.driver.implicitly_wait(wait_second)
        ct = ClickThread(self.driver)
        ct.start()

    def is_exist(self):
        self.driver.is_app_installed(self.conf["appPackage"])

    def install_app(self):
        self.driver.install_app(self.conf["appPackage"])

    def remove_app(self):
        self.driver.remove_app(self.conf["appPackage"])

    def click_element(self, elm_type, elm):
        source = self.driver.page_source
        if elm in source:
            self.driver.find_element_by_android_uiautomator('{0}("{1}")'.format(elm_type, str(elm))).click()
            print("点击%s" % elm)
        else:
            print("元素%s不存在" % elm)
