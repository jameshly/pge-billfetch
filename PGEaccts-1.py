"""
This python program should go through the PG&E website and automatically
    download all the bills from each account
"""
 import time, os, glob
 from selenium import webdriver
 from selenium.webdriver.common.keys import Keys
 from selenium.webdriver import ActionChains
 from selenium.webdriver.support.ui import WebDriverWait
 from selenium.webdriver.support import expected_conditions as EC
 from datetime import datetime,timedelta
 import os.path
 from selenium import webdriver
 from pyvirtualdisplay import Display

def wait_until_visible_then_click(element):
"""function that defines how to wait until something"""
    element = WebDriverWait(driver,5,poll_frequency=.2).until(
        EC.visibility_of(element))
    element.click()
def bill_download(driver):
def find_accounts(driver):
def login(driver):
"""log into PG&E"""
    driver.get("https://www.pge.com/")
    user = ("username")
    passwd = ("password")
    usr = driver.find_element_by_id("username")
    usr.send_keys(user)
    pwd = driver.find_element_by_id("password")
    pwd.send_keys(passwd)
    driver.find_element_by_id("home_login_submit").click()
def init():
"""preps the driver"""
    mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.dir", downloadpath)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    #disables confirmation dialog for pdf files
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    fp.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(firefox_profile =fp)
    return driver
def main():
    """main method so pylint doesn't yell at me"""
    downloadpath = "downloadlocation"
    login(init())
if __name__ == "__main__":
    main()
