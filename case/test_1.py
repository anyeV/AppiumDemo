from app.AppiumDemo import AppiumDemo
from time import sleep


class Test:

    def __init__(self):
        self.ar = AppiumDemo()

    def do_run(self):
        sleep(20)
        self.ar.click_element("text", "我知道了")


if __name__ == "__main__":
    Test().do_run()
