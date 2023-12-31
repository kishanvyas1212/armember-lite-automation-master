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
url = "http://localhost/test_kv1/"
def wait_for_element_present(driver, locator, timeout=10):
    try: 
        # try to find the element is located or not, if not then return None
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            
    except:
        pass
    return 
def wait_for_element_display(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
# locator = (By.XPATH,"test") pass the locator in this way for wait for element 

def action_perform(element, action,value):
    if action=='click':
        element.click()
    elif action=="send_keys":
        element.send_keys(value)
    return
    
    
def findelement(driver, locator,locatorpath,action=1,value=1):
    try:
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
    except Exception as e:
        print("Element is not found so please retry to move to next case")
        drivers.save_screenshot("screenshots/" + value +".png")
        drivers.quit()
           
             


def login_with_wordpress():
    end_point= "wp-login.php"
    username = "admin"
    password = "adminconnect"
    drivers.get(url + end_point)
    usernamef = findelement(drivers,"ID","user_login","send_keys",username)
    pwd = findelement(drivers,"ID","user_pass","send_keys",password)
    beforelogin = drivers.get_cookies()
    print("the number of the elements in the before cookie " + len(beforelogin))
    login = findelement(drivers,"NAME","wp-submit","click")
    armember=findelement(drivers,"XPATH",'//*[@id="toplevel_page_arm_manage_members"]/a/div[3]',"")
    print(armember)
    afterlogin = drivers.get_cookies()
    print("the number of the elements in the after cookie "+len(afterlogin))
    print("cookies before login")
    print(beforelogin)
    print("after login cookies")
    print(afterlogin)
    armember.click()
    

class login:
    def login_with_wordpress(data):
        drivers.get(url + data["end_point"])
        usernamef = findelement(drivers,"ID","user_login","send_keys",data["username"])
        pwd = findelement(drivers,"ID","user_pass","send_keys",data["password"])
        beforelogin = drivers.get_cookies()
        login = findelement(drivers,"NAME","wp-submit","click")
        usercookies = drivers.get_cookies()
        drivers.delete_all_cookies()
        return usercookies
    def login_with_armember(data):
        drivers.get(url + data["end_point"])
        usernamef = findelement(drivers,"NAME","user_login","send_keys",data["username"]) 
        pwd = findelement(drivers,"NAME","user_pass","send_keys",data["password"])   
        beforelogin = drivers.get_cookies()
        login = findelement(drivers,"NAME","armFormSubmitBtn","click")
        time.sleep(2)
        drivers.refresh()
        time.sleep(2)
        usercookies = drivers.get_cookies()
        print(usercookies)
        print(len(usercookies))
        return usercookies
    
class setup:
    
        # this is for armember registration check and setup check using bank
        # transport and paypal method but as of now i cann't check the paypal in local so only bank transfer
        before_cookies = drivers.get_cookies()
        def register(data,before_cookies):
            username_value = data["username"]
            firstname_value = data["first_name"]
            lastname_value = data["lastname_name"]
            
            locator = data["locator"]
            locatorpath = data["locatorpath"]
            action = data["action"]
                        
            for i in range(0, len(locator)):
                element = findelement(drivers,locator[i],locatorpath[i],action[i])
                time.sleep(1)
            
            after_cookies = drivers.get_cookies()
            return before_cookies,after_cookies
        
        
    
    
    

class validate:
    def verifyuser(cookie,data):
        if len(cookie) > 1:    
            cookie_value = cookie[3]["value"]
            if data["username"] in cookie_value : 
                print("login case is passed user:" + data["username"] + " is logged in successfully")
            else:
                print("it is not working")
                print(data["username"])
                print(cookie_value)
        else:
            error = wait_for_element_display((By.CLASS_NAME,"arm-df__fc--validation__wrap"))
            print("test case is passed ")
            print(error)
    def registerformverification():
        pass

data ={ "end_point": "wp-login.php",
        "username":"admin",
        "password":"adminconnect"
       }
data1 = {"end_point": "login",
        "username":"admin",
        "password":"adminconnect"
    
}
# login_ws = login.login_with_wordpress(data)
# drivers.refresh()
# print("user cookies: 1 ")
# print(login_ws)
# validate.verifyuser(login_ws,data)
# time.sleep(5)
# login_arm = login.login_with_armember(data1)
# validate.verifyuser(login_arm,data)

drivers.quit()