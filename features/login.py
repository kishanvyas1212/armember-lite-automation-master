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
url = "http://localhost/test_lite1"
def wait_for_element_present(locator, timeout=2):
    try: 
        # try to find the element is located or not, if not then return None
        WebDriverWait(drivers, timeout).until(EC.presence_of_element_located((By.CLASS_NAME,locator)))
            
    except:
        pass
    return 
def wait_for_element_display(driver, locator, timeout=10):
    return WebDriverWait(drivers, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,locator)))
    # print(locator)
    # return drivers.find_elements(By.CLASS_NAME,locator)
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
        drivers.save_screenshot("screenshots/" + str(value) +".png")
        drivers.quit()
              
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
        def register(data,before_cookies=before_cookies):
            drivers.get(url+"/register")
            username_value = data["username"]
            firstname_value = data["first_name"]
            lastname_value = data["lastname_name"]
            user_email_value = data["user_email"]
            user_pass_pwd = data["user_pass"]
            
            locator = data["locator"]
            locatorpath = data["locatorpath"]
            action = data["action"]
            error_locator = data["error"]       
            redirection_url = data["redirect_url"] 
            check_validation = data["check_validation"]
            # for i in range(0, len(locator)):
            #     element = findelement(drivers,locator[i],locatorpath[i],action[i])
            #     time.sleep(1)
            #     if i == (i-1):
            #         validate.registerformverification(username_value,user_email_value,error_locator)
            usernameadd = findelement(drivers,locator[0],locatorpath[0],action[0],username_value)
            first_name = findelement(drivers,locator[1],locatorpath[1],action[1],firstname_value)
            lastname_add = findelement(drivers,locator[2],locatorpath[2],action[2],lastname_value)
            email_add = findelement(drivers,locator[3],locatorpath[3],action[3],user_email_value)
            pass_add = findelement(drivers,locator[4],locatorpath[4],action[4],user_pass_pwd)
            time.sleep(1)
            if check_validation == 1:
                validation = validate.registerformverification(username_value,user_email_value,error_locator)
                if validation[0] == 0:
                    submit_form = findelement(drivers,locator[5],locatorpath[5],action[5])
                else:
                    print("add error handling, if use the csv or spread sheet to move forward then add the required code")
                    if "username" in validation[1].text:
                        print("the used username is already exist")
                        drivers.quit()
                    elif "email" in validation[1].text :
                        print("the used email is already exist")
                        drivers.quit()
            else:
                submit_form = findelement(drivers,locator[5],locatorpath[5],action[5])
            time.sleep(10)
            drivers.refresh()
            time.sleep(1)
            after_cookies = drivers.get_cookies()
            # check the redirection validation
            redirection = validate.redirection_validation(redirection_url)
            if redirection[0] == 1:
                print("redirected to " + redirection_url + " which is working properly")
            elif redirection[0] ==0:
                print("redirection is not working proeprly, it redirected to " + redirection[1] + " and which is not same as the expected url " + redirection_url)
            return before_cookies,after_cookies
        
        
    
    
    

class validate:
    def verifyuser(cookie_list,data):
        if len(cookie_list) > 1:
            desired_name = "wordpress_logged_in_d0ae86309cda26b347aa32d9ce217696"
            cookie_value = next((cookie for cookie in cookie_list if desired_name in cookie['name'] ), None) 
            if data["username"] in cookie_value["value"] : 
                print("login case is passed user:" + data["username"] + " is logged in successfully")
            else:
                print("it is not working")
                print(data["username"])
                print(cookie_value)
        else:
            error = wait_for_element_display(drivers,(By.CLASS_NAME,"arm-df__fc--validation__wrap"))
            print("test case is passed ")
            print(error)
    def registerformverification(username_value,user_email,locator):
       
        # in this we can check only two field validation, username and user email, so need to check this two only
        # below code to check the error message
        print(locator + "1")
        try: 
            error_msg =  wait_for_element_display(drivers,locator)
            # print(type(error_msg))
            # print(error_msg)
        
        except: 
            print(locator)
            print("no error is displayed it works properly")
            return 0, "no error is found"
        else: 
            return 1,error_msg
    def redirection_validation(expected_url):
        redirected_url = drivers.current_url
        if redirected_url == expected_url:
            print("it redirects properly, the redirection works properly")
            return 1, redirected_url
        else:
            print("redirection is not working properly")
            return 0, redirected_url
        
        

# data ={ "end_point": "wp-login.php",
#         "username":"admin",
#         "password":"adminconnect"
#        }
# data1 = {"end_point": "login",
#         "username":"admin",
#         "password":"adminconnect"
    
# }
# login_ws = login.login_with_wordpress(data)
# drivers.refresh()
# print("user cookies: 1 ")
# print(login_ws)
# validate.verifyuser(login_ws,data)
# time.sleep(5)
# login_arm = login.login_with_armember(data1)
# validate.verifyuser(login_arm,data)
register_data = {
    "username": "armember14",
    "first_name" :"armember14",
    "lastname_name" : "armember14",
    "user_email":"armember14@gmail.com",
    "user_pass":"armember14",
    "error" : "arm-df__fc--validation__wrap",
    "locator": ["NAME","NAME","NAME","NAME","NAME","NAME"],
    "locatorpath":["user_login","first_name","last_name","user_email","user_pass","armFormSubmitBtn"],
    "action":["send_keys","send_keys","send_keys","send_keys","send_keys","click"],
    "redirect_url" : "http://localhost/test_lite1/edit_profile/",
    "check_validation":0
}
register = setup.register(register_data)
print(register)
validate.verifyuser(register[1],register_data)
drivers.quit()