from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver = "C:\\Users\\USER\\Desktop\\CITAS_Selenium\\chromedriver.exe"

s = Service(chromedriver)

chrome_options = webdriver.ChromeOptions() #Make sure chromedriver.exe is in the same directory as the script or this gets ugly)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--auto-open-devtools-for-tabs")

driver = webdriver.Chrome(service=s, options=chrome_options)
driver.implicitly_wait(60)

driver.get("url")

#SHADOW DOM w/iframe - only use CSS selectors where By.CSS_SELECTOR is used, do not use XPATH or other types
shadow_host = driver.find_element(By.CSS_SELECTOR,"first shadow root element")
time.sleep(15)
shadow_root = shadow_host.shadow_root
shadow_content = shadow_root.find_element(By.CSS_SELECTOR, "second shadow root element")
iframe = shadow_content.find_element(By.CSS_SELECTOR, "iframe element")
driver.switch_to.frame(iframe)
req = driver.find_element(By.ID, "id of what you want to read")
val = req.get_attribute("value") #gets the content of the value tag
print(val)
driver.close()
exit()
