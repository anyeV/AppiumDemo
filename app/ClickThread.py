import threading
import time


class ClickThread(threading.Thread):

    def __init__(self, driver, click_elms=None):
        super(ClickThread, self).__init__()
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.driver = driver
        if click_elms and isinstance(click_elms, list):
            self.click_elms = click_elms
        else:
            self.click_elms = ["继续", "确定", "允许", "知道了"]

    def run(self):
        while self.__running.isSet():
            self.click_btn()
            time.sleep(1)

    def pause(self):
        '''
        阻塞线程
        :return:
        '''
        self.__flag.clear()

    def resume(self):
        '''
        恢复线程
        :return:
        '''
        self.__flag.set()

    def stop(self):
        '''
        停止线程
        :return:
        '''
        self.__flag.set()
        self.__running.clear()

    def click_btn(self):
        '''
        按钮点击
        :return:
        '''
        source = self.driver.page_source
        for clk_elm in self.click_elms:
            if clk_elm in source:
                try:
                    self.driver.find_element_by_xpath(
                        "//android.widget.Button[contains(@text,'{0}')]".format(str(clk_elm)))
                except:
                    print("可以根据需要来更改停止线程的时机")
                    self.stop()
