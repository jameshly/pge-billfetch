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

downloadpath = ""

#start the display
display = Display(visible=0, size=(1920, 1080))
display.start()
#mime_types here basically means to specify pdf files
mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.dir", downloadpath)
fp.set_preference("browser.download.manager.showWhenStarting", False)
#disables confirmation dialog for pdf files
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True)
#function that defines how to wait until something
def wait_until_visible_then_click(element):
    element = WebDriverWait(driver,5,poll_frequency=.2).until(
        EC.visibility_of(element))
    element.click()
driver = webdriver.Firefox(firefox_profile =fp)
driver.get("https://www.pge.com/")
#this was written before I remembered getpass().
user = "INSERT USERNAME HERE"
passwd = "INSERT PASSWORD HERE"
elems = driver.find_element_by_id("username")
elems.send_keys(user)
elems = driver.find_element_by_id("password")
elems.send_keys(passwd)
time.sleep(1)
elems.send_keys(Keys.RETURN)
print "logging in..."
driver.implicitly_wait(10)

#finds account lists
accounts = []
dropdown = driver.find_element_by_id("accountListElement")
lis = dropdown.find_elements_by_tag_name("li")
for li in lis:
    act = li.find_element_by_tag_name("a")
    accounts.append(act.get_attribute('innerHTML')[0:12])
#downlaods bills HERE
for account in accounts:
    try:
	time.sleep(10)
        driver.get("https://m.pge.com/index.html#myaccount/dashboard/billing/history/" + account)#yay for convienent URLs
        time.sleep(10)
        hrefs = driver.find_elements_by_id("utag-view-pay-view-bill-pdf")
        for href in hrefs:
    		try:
                	wait_until_visible_then_click(href)
                	print "downloading bill... for account#: " + account
                	time.sleep(15)
    		except:
    			print "Account# " + account + " does not work, please try again later. Moving on..."
                continue
    except:
        print "Account # " + account + " didn't work..."
        continue
#organize each pdf to a specified folder
os.chdir(downloadpath)
for file in glob.glob("*.pdf"):
	print (file)[0:4]
	os.rename(downloadpath + file, downloadpath+(file)[0:4]+"/"+file) #[0:4] gives me the last 4 digits of the account number or easier folder organization
driver.quit()
