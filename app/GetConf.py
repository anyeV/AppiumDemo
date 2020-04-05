import subprocess
import os
import re


class GetConf(object):

    def __init__(self, apk_path=None):
        self.apk_path = apk_path

    def get_devices_id(self):
        '''
        :return: 设备名，设备系统版本号
        '''
        order_str = 'adb devices'
        _devices = subprocess.check_output(order_str).decode("utf-8")
        dv_name = _devices.split("\r\n")[1].split("\t")[0]
        dv_order_str = 'adb shell getprop'
        devices_info = subprocess.check_output(dv_order_str)
        dv_version = re.search("\[ro\.build\.version\.release\]: \[(.+?)\]", str(devices_info))
        return dv_name, dv_version.group(1)

    def get_apk_info(self):
        '''
        :return: package_name, launcher_activity_name
        '''
        if not self.apk_path:
            files_path = os.path.dirname(os.getcwd()) + "\\testedObj\\"
            apk_path = files_path + sorted(os.listdir(files_path), reverse=True)[0]
        else:
            apk_path = self.apk_path
        order_str = 'aapt dump badging ' + apk_path
        apk_info = subprocess.check_output(order_str).decode("utf-8")
        launcher_activity_name = re.search("launchable-activity: name='(.+?)'", apk_info)
        apk_package_name = re.search("package: name='(.+?)'", apk_info)
        return apk_package_name.group(1), launcher_activity_name.group(1)

    def get_info(self):
        '''
        :return: appium参数
        '''
        dv_name, dv_version, = self.get_devices_id()
        app_package, app_activity = self.get_apk_info()
        return {
            "platformName": "Android",
            "deviceName": dv_name,
            "platformVersion": dv_version,
            "appPackage": app_package,
            "appActivity": app_activity,
            "noSign": False,
            "noReset": False,
            "autoGrantPermissions": True
        }
