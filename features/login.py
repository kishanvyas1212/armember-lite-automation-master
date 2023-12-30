from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver #by this we can access the webdriver which is inbuild method of selenium
from selenium.webdriver.chrome.service import Service   #This is selenium 4 new feature in which we import service 
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
ser_Obj = Service("C:\\Users\\91635\\Desktop\\drivers\\chromedriver.exe")
# ser_Obj = Service("C:\\Users\\91635\\Desktop\\drivers\\geckodriver.exe")
drivers = webdriver.Chrome(service= ser_Obj)
drivers.implicitly_wait(60)

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def action_perform(element, action,value):
    if action=='click':
        element.click()
    elif action=="send_keys":
        element.send_keys(value)
    return
    
    
def findelement(driver, locator,locatorpath,action=1,value=1):
    if locator=="ID" or locator=="id":
        element = driver.find_element(By.ID, locatorpath )
        if action!="" or action!="1" or action=="click" or action=="send_keys":
            action_perform(element,action,value)
        return element
    elif locator=="XPATH" or locator=="xpath":
        element = driver.find_element(By.XPATH,locatorpath)
        if action!="" or action!="1" or action=="click" or action=="send_keys":
            action_perform(element,action,value)
        return element
    elif locator=="name" or locator=="NAME":
        element = driver.find_element(By.NAME,locatorpath)
        if action!="" or action!="1" or action=="click" or action=="send_keys":    
            action_perform(element,action,value)
        return element


url = "http://localhost/test_kv1/"
end_point= "wp-login.php"
username = "admin"
password = "adminconnect"
drivers.get(url + end_point)
drivers.implicitly_wait(10)
usernamef = findelement(drivers,"ID","user_login","send_keys",username)
pwd = findelement(drivers,"ID","user_pass","send_keys",password)
beforelogin = drivers.get_cookies()
login = findelement(drivers,"NAME","wp-submit","click")
armember=findelement(drivers,"XPATH",'//*[@id="toplevel_page_arm_manage_members"]/a/div[3]',"")
print(armember)
afterlogin = drivers.get_cookies()
print("cookies before login")
print(beforelogin)
print("after login cookies")
print(afterlogin)
armember.click()
time.sleep(10)

drivers.quit()
